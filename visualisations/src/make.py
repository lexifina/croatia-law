"""Rebuild visualisations/hrvatsko-pravo-u-20-grafikona.html from this repository.

    python visualisations/src/make.py [--repo PATH] [--ref REF] [--skip-extract]

Steps (all read-only on the repository; scratch output goes to visualisations/src/.build/):
  1. the history of REF (default origin/main), streamed: author domain, Kind and In-force-basis of every commit,
     counted, never held                                                                   -> .build/meta.json
  2. the tables, read from git objects: registry/data/acts.json (streamed into one compact line per act),
     registry/data/laws.csv, data/zakoni.json, data/held.json, data/ispravci.csv, data/ustavni-sud-ukidanja.csv
                                                                                           -> .build/repo/
  3. the tree of REF, streamed: files per folder, the articles of every law (one file per article), and the
     blob ids of the texts the charts read                                                 -> .build/tree.json
  4. those texts, fetched in batches in a partial (blobless) clone, some 16,000 small files in all:
     - the first three articles of every law (does it name EU acts?)                       -> .build/t-eu.jsonl
     - the acts on the minimum wage, the local income tax rates, the boundary of the maritime domain,
       the laws authorising the Government to regulate by decree, the conversion to the kuna and the euro
                                                                                           -> .build/t-*.jsonl
     - the official election results of izbori/                                            -> .build/t-izbori.jsonl
     - every version of the Constitution, from the commits that touch ustav/               -> .build/ustav.jsonl
  5. prep.py turns those into .build/data.json; build.py fills page.tpl.html with it.
Works in a blobless or --no-checkout clone: everything is read from git objects, and nothing large is held in memory.
"""
import argparse, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument('--repo', default=os.path.abspath(os.path.join(HERE, '..', '..')))
ap.add_argument('--ref', default=None, help='default: origin/main if present, else HEAD')
ap.add_argument('--out', default=os.path.join(HERE, '..', 'hrvatsko-pravo-u-20-grafikona.html'))
ap.add_argument('--skip-extract', action='store_true', help='reuse .build/ from a previous run (prep and build only)')
a = ap.parse_args()
B = os.path.join(HERE, '.build')
R = os.path.join(B, 'repo')
os.makedirs(R, exist_ok=True)
NOLAZY = dict(os.environ, GIT_NO_LAZY_FETCH='1')
GIT = ['git', '-C', a.repo, '-c', 'core.quotepath=off']


def git(*args):
    return subprocess.run([*GIT, *args], check=True, capture_output=True, env=NOLAZY).stdout


def has(ref):
    return subprocess.run([*GIT, 'rev-parse', '--verify', '-q', ref], capture_output=True, env=NOLAZY).returncode == 0


ref = a.ref or ('origin/main' if has('origin/main') else 'HEAD')
sha = git('rev-parse', ref).decode().strip()
print('ref', ref, sha, flush=True)


def fetch_missing(oids, batch=4000):
    """batched fetches of the blobs a partial clone does not have yet (one request per batch, not per blob)"""
    oids = sorted(set(oids))
    chk = subprocess.run([*GIT, 'cat-file', '--batch-check'], input=''.join(o + '\n' for o in oids).encode(),
                         capture_output=True, env=NOLAZY).stdout.decode().split('\n')
    missing = [l.split()[0] for l in chk if l.endswith(' missing')]
    for i in range(0, len(missing), batch):
        part = missing[i:i + batch]
        print('fetching', len(part), 'blobs', f'({i + len(part)} of {len(missing)})', flush=True)
        subprocess.run([*GIT, '-c', 'fetch.negotiationAlgorithm=noop', 'fetch', 'origin', '--no-tags', '--no-write-fetch-head',
                        '--recurse-submodules=no', '--filter=blob:none', '--stdin'], input=''.join(m + '\n' for m in part).encode(), check=False)


def read_blobs(items):
    """yield (path, bytes) for (oid, path) pairs, one blob at a time"""
    p = subprocess.Popen([*GIT, 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=NOLAZY)
    for oid, path in items:
        p.stdin.write((oid + '\n').encode()); p.stdin.flush()
        head = p.stdout.readline().split()
        if len(head) < 3:
            sys.exit('cannot read ' + path)
        data = p.stdout.read(int(head[2])); p.stdout.read(1)
        yield path, data
    p.stdin.close(); p.wait()


def blob_to_file(path, out):
    """one table from the tree of REF into .build/repo/, streamed to disk"""
    oid = git('rev-parse', f'{ref}:{path}').decode().strip()
    fetch_missing([oid])
    with open(out, 'wb') as f:
        p = subprocess.Popen([*GIT, 'cat-file', 'blob', oid], stdout=subprocess.PIPE, env=NOLAZY)
        for chunk in iter(lambda: p.stdout.read(1 << 16), b''):
            f.write(chunk)
        p.wait()


def tree(r, *paths):
    """(path, oid) of every file of the tree of r under paths, streamed"""
    lt = subprocess.Popen([*GIT, 'ls-tree', '-r', '-z', r, '--', *paths], stdout=subprocess.PIPE, env=NOLAZY)
    buf = b''
    for chunk in iter(lambda: lt.stdout.read(1 << 16), b''):
        buf += chunk
        *ents, buf = buf.split(b'\0')
        for e in ents:
            meta, path = e.split(b'\t', 1)
            yield path.decode('utf-8'), meta.split()[2].decode()
    lt.wait()


def acts_stream(f):
    """registry/data/acts.json is pretty-printed, one key per line: yield one act at a time (depth-aware)"""
    buf, depth = None, 0
    for line in f:
        s = line.strip()
        if buf is None:
            if s == '{' and depth == 1:
                buf, depth = ['{'], 2
            elif s.startswith('"acts": ['):
                depth = 1
            continue
        buf.append(line)
        depth += (1 if s.endswith('[') or s.endswith('{') else 0) - (1 if s.startswith('}') or s.startswith(']') else 0)
        if depth == 1:
            yield json.loads(''.join(buf).rstrip().rstrip(','))
            buf = None


# titles that pick the texts a chart reads (the same rules as prep.py)
RX_MW = re.compile(r'minimaln\w* plać', re.I)
RX_TAX = re.compile(r'poreznih stopa|stopa poreza na dohodak|stope poreza na dohodak', re.I)
RX_PD = re.compile(r'granic\w* pomorskog dobra', re.I)
RX_OV = re.compile(r'o ovlasti Vlade', re.I)
RX_SAB = re.compile(r'raspuštanju (?:Hrvatskoga|Zastupničkog)|sazivanju prvog zasjedanja (?:Hrvatskoga|Zastupničkog)', re.I)   # the Sabor dissolved, and its first sitting
RATES = {'odluka/1994/685', 'odluka/2022/1302'}   # the conversion of the dinar to the kuna, and of the kuna to the euro

if not a.skip_extract:
    # 1. the history, streamed. Every act of Narodne novine enters as one commit credited to the act itself (its id is the
    #    author e-mail's local part) and carrying its own trailers; a commit that changes another act carries Affecting:.
    #    One line per act (its own first commit) -> nn-acts.jsonl; everything else is only counted.
    TR = ['Kind', 'Published', 'In-force', 'Source', 'Act', 'Law', 'In-force-basis', 'Files', 'Affecting', 'Enacted']
    fmt = '%x1e%ae%x1f%an%x1f%ad%x1f' + '%x1f'.join(f'%(trailers:key={k},valueonly,unfold,separator=;)' for k in TR)
    lg = subprocess.Popen([*GIT, 'log', ref, '--date=short', '--format=' + fmt], stdout=subprocess.PIPE, env=NOLAZY)
    meta = {'sha': sha, 'ref': ref, 'commits': 0, 'by_domain': {}, 'by_kind': {}, 'basis_eu': {}, 'basis_euro': {}, 'last_in_force': ''}
    first = {}

    def take(rec):
        rec = rec.decode('utf-8', 'replace').strip('\r\n')
        if not rec:
            return
        f = (rec.split('\x1f') + [''] * 13)[:13]
        ae, an, ad = f[0], f[1], f[2]
        tr = {k: f[3 + i].strip().replace('\n', ' ') for i, k in enumerate(TR)}
        meta['commits'] += 1
        dom = ae.split('@')[-1]
        meta['by_domain'][dom] = meta['by_domain'].get(dom, 0) + 1
        k = tr['Kind'] or '-'
        meta['by_kind'][k] = meta['by_kind'].get(k, 0) + 1
        basis = tr['In-force-basis']
        if 'joined the European Union' in basis:
            meta['basis_eu'][ad] = meta['basis_eu'].get(ad, 0) + 1
        if 'the euro became' in basis:
            meta['basis_euro'][ad] = meta['basis_euro'].get(ad, 0) + 1
        if dom in ('narodne-novine.invalid', 'croatia-law.invalid'):
            if ad > meta['last_in_force'] and ad <= '2026-12-31':
                meta['last_in_force'] = ad
            if tr['Affecting'] or k in ('publisher', 'correction', 'documentation'):
                return
            slug = ae.split('@')[0]
            old = first.get(slug)
            if old is None or ad < old['ad']:
                first[slug] = {'slug': slug, 'ad': ad, 'author': an, 'kind': k, 'pub': tr['Published'], 'inf': tr['In-force'], 'src': tr['Source'],
                               'act': tr['Act'], 'law': tr['Law'], 'basis': tr['In-force-basis'][:160], 'files': tr['Files'].split(';')[0].strip(), 'enacted': tr['Enacted']}

    buf = b''
    for chunk in iter(lambda: lg.stdout.read(1 << 16), b''):
        buf += chunk
        *recs, buf = buf.split(b'\x1e')
        for r in recs:
            take(r)
    take(buf)
    lg.wait()
    with open(os.path.join(B, 'nn-acts.jsonl'), 'w', encoding='utf-8', newline='\n') as out:
        for slug in sorted(first):
            out.write(json.dumps(first[slug], ensure_ascii=False) + '\n')
    meta['head_date'] = git('log', '-1', '--format=%cs', ref).decode().strip()
    print('commits', meta['commits'], '| acts entered by their own commit', len(first), flush=True)
    FOLD = {'ugovor': 'medunarodni', 'ku': 'kolektivni-ugovor'}

    def folder_of(slug):
        m = re.match(r'^([a-z-]+?)-(\d{4})-(\d+)$', slug)
        return f'{FOLD.get(m.group(1), m.group(1))}/{m.group(2)}/{m.group(3)}' if m else None

    def title_of(x):
        return x['act'] or re.sub(r'\s*\(NN \d+/\d{4}\)\s*$', '', x['law']) or x['author']

    # 2. the tables
    blob_to_file('registry/data/acts.json', os.path.join(R, 'acts.json'))
    blob_to_file('registry/data/laws.csv', os.path.join(R, 'laws.csv'))
    blob_to_file('data/zakoni.json', os.path.join(R, 'zakoni.json'))
    blob_to_file('data/held.json', os.path.join(R, 'held.json'))
    blob_to_file('data/ispravci.csv', os.path.join(R, 'ispravci.csv'))
    blob_to_file('data/ustavni-sud-ukidanja.csv', os.path.join(R, 'ustavni-sud-ukidanja.csv'))
    want = {'mw': set(), 'tax': set(), 'pd': set(), 'ov': set(), 'sabor': set()}
    n = 0
    with open(os.path.join(R, 'acts.json'), encoding='utf-8') as f, open(os.path.join(B, 'acts.jsonl'), 'w', encoding='utf-8', newline='\n') as out:
        for x in acts_stream(f):
            ab = [[r.get('date', ''), r.get('how', ''), r.get('ref', ''), (r.get('title') or '')[:90]] for r in (x.get('amended_by') or [])]
            row = {k: x.get(k) for k in ('slug', 'path', 'kind', 'year', 'title', 'status', 'from', 'latest', 'portal')}
            row['ab'] = ab
            row['nc'] = len(x.get('cited_by') or [])
            out.write(json.dumps(row, ensure_ascii=False) + '\n')
            n += 1
            t = x.get('title') or ''
            if RX_MW.search(t): want['mw'].add(x['path'])
            if RX_TAX.search(t) and x.get('kind') == 'odluka' and (x.get('year') or '') >= '2023': want['tax'].add(x['path'])
            if RX_PD.search(t): want['pd'].add(x['path'])
            if RX_OV.search(t) and x.get('kind') == 'zakon': want['ov'].add(x['path'])
            if RX_SAB.search(t) and x.get('kind') == 'odluka': want['sabor'].add(x['path'])
    os.remove(os.path.join(R, 'acts.json'))
    for z in json.load(open(os.path.join(R, 'zakoni.json'), encoding='utf-8')):
        if RX_OV.search(z['title']): want['ov'].add(z['path'])
    # the acts the registry list does not hold yet (appended later): pick them from their own commits
    for slug, x in first.items():
        f, t = folder_of(slug), title_of(x)
        if not f:
            continue
        if RX_MW.search(t): want['mw'].add(f)
        if RX_TAX.search(t) and f.startswith('odluka/') and f.split('/')[1] >= '2023': want['tax'].add(f)
        if RX_PD.search(t): want['pd'].add(f)
        if RX_OV.search(t) and f.startswith('zakon/'): want['ov'].add(f)
        if RX_SAB.search(t) and f.startswith('odluka/'): want['sabor'].add(f)
    law_folders = {folder_of(s) for s in first if s.startswith('zakon-')}
    del first
    print('acts', n, {k: len(v) for k, v in want.items()}, flush=True)

    # 3. the tree, streamed
    tops, articles, units, courts = {}, {}, set(), {}
    sel = {k: [] for k in ('eu', 'mw', 'tax', 'pd', 'ov', 'sabor', 'rates', 'izbori')}
    TXT = re.compile(r'(clanak-\d+[a-z]?|tekst|prilog(-\d+)?)\.md$')
    for path, oid in tree(ref):
        parts = path.split('/')
        tops[parts[0]] = tops.get(parts[0], 0) + 1
        if len(parts) < 3:
            continue
        folder = '/'.join(parts[:3])
        fn = parts[-1]
        if parts[0] == 'zakon' and len(parts) == 4 and fn.startswith('clanak-'):
            articles[folder] = articles.get(folder, 0) + 1
            if fn in ('clanak-001.md', 'clanak-002.md', 'clanak-003.md'):
                sel['eu'].append((oid, path))
        if parts[0] == 'local' and len(parts) >= 4:
            units.add(parts[1])
        if parts[0] == 'caselaw' and fn == 'README.md':
            c = parts[1]
            courts[c] = courts.get(c, 0) + 1
        if parts[0] == 'izbori' and fn == 'tekst.md':
            sel['izbori'].append((oid, path))
        if len(parts) == 4 and TXT.search(fn):
            for k in ('mw', 'tax', 'pd', 'ov', 'sabor'):
                if folder in want[k]:
                    sel[k].append((oid, path))
            if folder in RATES:
                sel['rates'].append((oid, path))
    # laws repealed as a whole leave the tree (their last version is empty): read them from the parent of the commit that removed them
    removed, gone = {}, {}
    h = None
    for line in git('log', ref, '--diff-filter=D', '--no-renames', '--name-only', '--format=@@%H', '--', 'zakon').decode('utf-8', 'replace').splitlines():
        if line.startswith('@@'):
            h = line[2:]
        elif line.strip():
            gone.setdefault('/'.join(line.split('/')[:3]), h)       # the latest commit that removed the folder's files
    for f in sorted((law_folders - set(articles)) & set(gone)):
        h = gone[f]
        for path, oid in tree(h + '^', f):
            fn = path.rsplit('/', 1)[-1]
            if fn.startswith('clanak-'):
                removed[f] = removed.get(f, 0) + 1
                if fn in ('clanak-001.md', 'clanak-002.md', 'clanak-003.md'):
                    sel['eu'].append((oid, path))
            if f in want['ov'] and TXT.search(fn):
                sel['ov'].append((oid, path))
    articles.update(removed)
    print('laws read from before their repeal', len(removed), flush=True)
    json.dump({'tops': tops, 'zakon_articles': articles, 'removed_laws': sorted(removed), 'local_units': len(units), 'courts': courts},
              open(os.path.join(B, 'tree.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    print('tree', sum(tops.values()), 'files;', {k: len(v) for k, v in sel.items()}, flush=True)

    # 4. the texts
    fetch_missing([o for v in sel.values() for o, _ in v])
    for k, items in sel.items():
        with open(os.path.join(B, f't-{k}.jsonl'), 'w', encoding='utf-8', newline='\n') as out:
            for path, data in read_blobs(sorted(items, key=lambda x: x[1])):
                out.write(json.dumps({'p': path, 't': data.decode('utf-8', 'replace')}, ensure_ascii=False) + '\n')
    # every version of the Constitution: the commits that touch ustav/, and the articles of each
    vers = []
    for line in git('log', ref, '--reverse', '--date=short', '--format=%H%x09%ad%x09%an%x09%(trailers:key=Kind,valueonly,separator=;)', '--', 'ustav').decode('utf-8').splitlines():
        h, ad, an, kind = (line.split('\t') + ['', '', '', ''])[:4]
        files = [(o, p) for p, o in tree(h, 'ustav') if re.match(r'ustav/(clanak-\d+[a-z]?|izvorisne-osnove)\.md$', p)]
        vers.append((h, ad, an, kind.strip(), files))
    fetch_missing([o for v in vers for o, _ in v[4]])
    with open(os.path.join(B, 'ustav.jsonl'), 'w', encoding='utf-8', newline='\n') as out:
        for h, ad, an, kind, files in vers:
            if not files:
                continue
            txt = {p: d.decode('utf-8', 'replace') for p, d in read_blobs(files)}
            out.write(json.dumps({'sha': h, 'date': ad, 'author': an, 'kind': kind, 'files': txt}, ensure_ascii=False) + '\n')
    print('constitution versions', len(vers), flush=True)
    json.dump(meta, open(os.path.join(B, 'meta.json'), 'w', encoding='utf-8'), ensure_ascii=False)

# 5. prep + build
env = dict(os.environ, HEAD_SHA=sha)
subprocess.run([sys.executable, '-X', 'utf8', os.path.join(HERE, 'prep.py'), B], check=True, env=env)
subprocess.run([sys.executable, '-X', 'utf8', os.path.join(HERE, 'build.py'), os.path.join(B, 'data.json'), os.path.abspath(a.out)], check=True)
