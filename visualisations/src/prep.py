"""Compute every number of the 20 charts from what make.py extracted into .build/ -> .build/data.json.

    python prep.py <.build folder>

Every rule that classifies by words is here, with word boundaries; whatever no rule recognises is counted as "other".
Run it again and it prints the checks it makes (samples of each class, totals against the README's counts).
"""
import csv, datetime as dt, difflib, json, math, os, re, statistics, sys
from collections import Counter, defaultdict

B = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '.build')
R = os.path.join(B, 'repo')
META = json.load(open(os.path.join(B, 'meta.json'), encoding='utf-8'))
TREE = json.load(open(os.path.join(B, 'tree.json'), encoding='utf-8'))
D, PF = {}, {}
LAST_FULL = 2025          # the last full year; 2026 is partial
TODAY = META['head_date']
csv.field_size_limit(10 ** 8)


def d8(s):
    return dt.date.fromisoformat(s[:10])


def jl(name):
    with open(os.path.join(B, name), encoding='utf-8') as f:
        for line in f:
            yield json.loads(line)


def texts(name):
    """{act folder: text of its article files, in file order}"""
    by = defaultdict(list)
    for x in jl(name):
        by[x['p'].rsplit('/', 1)[0]].append((x['p'], x['t']))
    return {k: '\n'.join(t for _, t in sorted(v)) for k, v in by.items()}


ELI = re.compile(r'/eli/(sluzbeni|medunarodni)/(\d{4})/(\d+)/(\d+)')


def eli(url):
    m = ELI.search(url or '')
    return (m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))) if m else None


def clean(t):
    return re.sub(r'\s+', ' ', (t or '').replace('­', '')).strip()


# ------------------------------------------------------------------ the acts
# Every act of Narodne novine enters the history as one commit credited to the act itself, with its own trailers
# (Published, In-force, Source = its ELI address): make.py kept that commit for each act -> nn-acts.jsonl. The registry
# list (registry/data/acts.json) adds the status and the later acts that amend, repeal or replace each act, for the acts
# it already holds (it was written before the last batches were appended).
REG = {x['slug']: x for x in jl('acts.jsonl')}
OFF = {'zakon', 'uredba', 'pravilnik', 'odluka', 'naredba', 'naputak', 'uputa', 'statut', 'ostalo', 'program', 'plan', 'poslovnik', 'popis',
       'tarifa', 'kodeks', 'izmjene-i-dopune', 'metodologija', 'opci-uvjeti', 'zakljucak', 'cjenik', 'sabor', 'smjernice'}
FOLD = {'ugovor': 'medunarodni', 'ku': 'kolektivni-ugovor'}
acts, seen, seen_slug = [], set(), set()
INTL = []     # treaties (the international part)
NOTOFF = Counter()
for x in jl('nn-acts.jsonl'):
    m = re.match(r'^([a-z-]+?)-(\d{4})-(\d+)$', x['slug'])
    if not m or 'narodne-novine.nn.hr' not in x['src']:
        NOTOFF['other source'] += 1
        continue
    k = m.group(1)
    e = eli(x['src'])
    yr = e[1] if e else int(m.group(2))
    title = clean(x['act'] or re.sub(r'\s*\(NN \d+/\d{4}\)\s*$', '', x['law']) or re.sub(r'\s*\(NN \d+/\d{4}\)\s*$', '', x['author']))
    reg = REG.get(x['slug'], {})
    rec = {'src': 'r', 'kind': k, 'y': yr, 'iss': e[2] if e else None, 'doc': e[3] if e else int(m.group(3)),
           'pub': x['pub'] or None, 'inf': x['inf'] or None, 'title': title, 'status': reg.get('status') or '', 'reg': bool(reg),
           'ab': reg.get('ab') or [], 'path': f'{FOLD.get(k, k)}/{m.group(2)}/{m.group(3)}', 'slug': x['slug'], 'basis': x['basis']}
    if k == 'ugovor':
        INTL.append(rec)
    elif k in OFF:
        acts.append(rec)
        seen.add((yr, rec['doc'])); seen_slug.add(x['slug'])
    else:
        NOTOFF[k] += 1
print('not in the official-part table:', dict(NOTOFF))
ZAK = json.load(open(os.path.join(R, 'zakoni.json'), encoding='utf-8'))
nz = 0
for z in ZAK:
    e = eli(z['url'])
    if not e or (e[1], e[3]) in seen or z['kind'] != 'zakon':
        continue
    seen.add((e[1], e[3])); nz += 1
    acts.append({'src': 'z', 'kind': 'zakon', 'y': e[1], 'iss': e[2], 'doc': e[3], 'pub': z.get('published') or None,
                 'inf': z.get('in_force') or None, 'title': clean(z['title']), 'status': z.get('status') or '', 'reg': True,
                 'ab': [[r.get('date', ''), r.get('how', ''), r.get('ref', ''), (r.get('title') or '')[:90]] for r in (z.get('amended_by') or [])],
                 'path': z['path'], 'slug': z['slug'], 'basis': ''})
# the publication day of each issue of Narodne novine, from the acts dated in the history and in the registry
ISSUE = defaultdict(Counter)
for a in acts:
    if a['pub'] and a['iss']:
        ISSUE[(a['y'], a['iss'])][a['pub']] += 1
for r in csv.DictReader(open(os.path.join(R, 'laws.csv'), encoding='utf-8')):
    e = eli(r['url'])
    if e and r['published']:
        ISSUE[(e[1], e[2])][r['published']] += 1
HELD = json.load(open(os.path.join(R, 'held.json'), encoding='utf-8'))['acts']
nh, held_nodate = 0, 0
for h in HELD:
    e = eli(h['official_url'])
    if not e or (e[1], e[3]) in seen or h['act'] in seen_slug:
        continue
    seen.add((e[1], e[3])); nh += 1
    iss = ISSUE.get((e[1], e[2]))
    pub = iss.most_common(1)[0][0] if iss else None
    held_nodate += pub is None
    acts.append({'src': 'h', 'kind': h['kind'], 'y': e[1], 'iss': e[2], 'doc': e[3], 'pub': pub, 'inf': None,
                 'title': clean(h['title']), 'status': 'held', 'reg': False, 'ab': [], 'path': '', 'slug': h['act'], 'reason': h['reason'], 'basis': ''})
print('acts of the official part', len(acts), '| from the earlier build', nz, '| held', nh, '(no issue date for', held_nodate, ')')

AMEND = re.compile(r'^(?:[A-ZČĆŽŠĐ][\w-]*\s+){0,2}?o\s+(?:[IVX]+\.\s+)?(?:izmjen\w*|dopun\w*|izmjeni)\b|^(?:Izmjen\w*|Dopun\w*)\b', re.I)
REPEAL = re.compile(r'\bo prestanku (?:važenja|primjene)\b', re.I)


def is_amend(t):
    return bool(AMEND.search(t))


for a in acts:
    a['am'] = is_amend(a['title'])
    a['rep'] = (not a['am']) and bool(REPEAL.search(a['title']))
laws = [a for a in acts if a['kind'] == 'zakon']
print('laws', len(laws), '| amending', sum(a['am'] for a in laws), '| repeal only', sum(a['rep'] for a in laws))
for t in [a['title'] for a in laws if a['am']][:3] + [a['title'] for a in acts if a['kind'] == 'odluka' and a['am']][:3]:
    print('   amending:', t[:110])
PF['acts'] = len(acts)
PF['laws'] = len(laws)
PF['held'] = nh
PF['zak'] = nz

# ------------------------------------------------------------------ c01: volume by kind
KG = {'zakon': 'zakon', 'uredba': 'uredba', 'pravilnik': 'pravilnik', 'odluka': 'odluka'}
c01 = defaultdict(lambda: Counter())
for a in acts:
    c01[a['y']][KG.get(a['kind'], 'ostalo')] += 1
    if a['src'] == 'h':
        c01[a['y']]['held'] += 1
D['c01'] = [{'y': y, **c01[y]} for y in sorted(c01) if 1990 <= y <= 2026]
full = [r for r in D['c01'] if 1991 <= r['y'] <= LAST_FULL]
print('c01 mean a year 1991-2025', round(statistics.mean(sum(v for k, v in r.items() if k not in ('y', 'held')) for r in full)))

# ------------------------------------------------------------------ c02: amending acts, by kind and five-year period
def period(y):
    return f'{y // 5 * 5}'


c02 = {}
for k in ['zakon', 'uredba', 'pravilnik', 'odluka']:
    p = defaultdict(lambda: [0, 0])
    for a in acts:
        if a['kind'] == k and 1990 <= a['y'] <= 2026:
            p[period(a['y'])][0] += 1
            p[period(a['y'])][1] += a['am']
    c02[k] = [[pp, *p[pp]] for pp in sorted(p)]
D['c02'] = c02
for k, v in c02.items():
    print('c02', k, sum(x[2] for x in v), 'of', sum(x[1] for x in v))

# ------------------------------------------------------------------ the subject of a law: its own name, or the name of the law it amends
ADJ = [('Općeg poreznog', 'Opći porezni'), ('Kaznenog', 'Kazneni'), ('Carinskog', 'Carinski'), ('Obiteljskog', 'Obiteljski'), ('Ovršnog', 'Ovršni'),
       ('Stečajnog', 'Stečajni'), ('Prekršajnog', 'Prekršajni'), ('Pomorskog', 'Pomorski'), ('Ustavnog', 'Ustavni'), ('Izbornog', 'Izborni')]


def nominative(obj):
    """'Zakona o porezu na dohodak' -> 'Zakon o porezu na dohodak'; 'Kaznenog zakona' -> 'Kazneni zakon'"""
    obj = re.sub(r'\s*\((?:[^()]*)\)\s*$', '', obj).strip(' .,')
    obj = re.split(r',? (?:i|te) (?=Zakona\b|[A-ZČĆŽŠ]\w+og zakona\b)', obj)[0]      # several laws amended at once: the first
    m = re.match(r'^Zakonika\b(.*)$', obj)
    if m:
        return 'Zakonik' + m.group(1)
    m = re.match(r'^Zakona\b(.*)$', obj)
    if m:
        return 'Zakon' + m.group(1)
    for g, n in ADJ:
        if obj.startswith(g + ' '):
            rest = obj[len(g) + 1:]
            rest = re.sub(r'^zakonika\b', 'zakonik', re.sub(r'^zakona\b', 'zakon', rest))
            return n + ' ' + rest
    m = re.match(r'^([A-ZČĆŽŠĐ]\w+)(og|eg) (zakona|zakonika)\b(.*)$', obj)
    if m:
        return m.group(1) + 'i ' + m.group(3).replace('zakona', 'zakon').replace('zakonika', 'zakonik') + m.group(4)
    return obj


AMOBJ = re.compile(r'^Zakon\w*\s+o\s+(?:[IVX]+\.\s+)?(?:izmjen\w*|dopun\w*|izmjeni)(?:\s+(?:i|te)\s+(?:dopun\w*|izmjen\w*))?\s+(.+)$', re.I)


REPOBJ = re.compile(r'^Zakon\w*\s+o\s+(?:prestanku\s+važenja|stavljanju\s+izvan\s+snage|prestanku\s+primjene)\s+(?:odredab\w+\s+)?(.+)$', re.I)


def subject(title):
    t = title
    for _ in range(3):
        m = AMOBJ.match(t) or REPOBJ.match(t)
        if not m:
            break
        t = nominative(m.group(1))
    return t


def base_key(name):
    return re.sub(r'[^a-zčćžšđ0-9 ]', '', name.lower()).replace('  ', ' ').strip()


# ------------------------------------------------------------------ c03: what the laws are about
TOPICS = [
    ('rat', r'\bbranitelj\w*|\bdomovinsk\w*\s+rat\w*|\bratn\w+ (?:vojn\w+|štet\w*)|\bcivilni\w* stradal\w*|\bžrtv\w+ (?:rata|fašisti\w*)|\bnestal\w+ osob\w*|\bzatočen\w*|\bprognanik\w*|\bizbjeglic\w*'),
    ('porez', r'\bporez\w*|\bpore[zs]n\w*|\bproračun\w*|\bdoprinos\w*|\bcarin\w*|\btrošarin\w*|\bpristojb\w*|\bfiskal\w*|\bdržavn\w+ potpor\w*|\bračunovodstv\w*|\breviz\w*|\bjavn\w+ dug\w*|\bzaduživanj\w*|\bfinanciranj\w+ (?:jedinica|lokaln)\w*|\bjavnih prihoda\b|\bprirez\w*|\bjavn\w+ davanj\w*'),
    ('zdravstvo', r'\bzdravstv\w*|\blijek\w*|\bljekarn\w*|\bbolni\w*|\bbolest\w*|\bmedicin\w*|\bzaraz\w*|\bpacijent\w*|\bkrv[i]?\b|\btransplant\w*|\bpresađivanj\w*|\bljudsk\w+ (?:organ|tkiv|stanic)\w*|\bopojn\w+ drog\w*|\bdrog\w*|\bpsihijatrij\w*|\bduševn\w*|\bmentaln\w*|\bstomatolog\w*|\bliječni\w*|\bprimalj\w*|\bsestrinst\w*|\bpsihoterapij\w*|\bcijepljenj\w*|\bkemikalij\w*|\bbiocid\w*|\bgenetsk\w*|\bfizioterap\w*|\btjelesn\w+ oštećenj\w*|\bkontaminant\w*|\bpredmet\w+ opće upo\w+|\boplodnj\w*'),
    ('rad', r'(?<!udruženog )\brad[aui]?\b|\bradn\w+ (?:odnos|vrijem|staž|mjest)\w*|\bradnik\w*|\bzapošljavanj\w*|\bzaposlen\w*|\bmirovin\w*|\bmirovinsk\w*|\bsocijaln\w*|\bdoplatk\w*|\bdoplatak\b|\brodilj\w*|\broditeljsk\w*|\bdjec\w+|\bdječj\w*|\bplać\w*|\binvalid\w*|\bnezaposlen\w*|\bstrajk\w*|\bkolektivn\w+ ugovor\w*|\bsindikat\w*|\bumirovljeni\w*|\bosobn\w+ asistencij\w*|\binkluzivn\w*|\bnjegovatelj\w*|\bhumanitarn\w+ pomoć\w*|\bregistr\w+ osiguranik\w*|\bslijep\w*|\bgluh\w*'),
    ('drzava', r'\bustavn\w+ sud\w*|\bizbor\w*|\bbirač\w*|\breferendum\w*|\bsabor\w*|\bvlad[aeiu]\b|\bvladi\b|\bministarstv\w*|\bdržavn\w+ (?:služb|uprav|službenik|dužnosni|informacijsk)\w*|\bjavn\w+ (?:služb|dužnosni)\w*|\buprav[aeiu]\b|\bupravi\b|\blokaln\w+|\bpodručn\w+ \(regionaln\w+\)|\bžupanij\w*|\bgradov\w*\b|\bGrad\w* Zagreb\w*|\bopćin\w*|\bsamouprav\w*|\bdržavljanstv\w*|\bgrb\w*\b|\bzastav\w*|\bhimn\w*|\bblagdan\w*|\bpučk\w+ pravobranitelj\w*|\bpravobranitelj\w*|\bnacionaln\w+ manjin\w*|\bvjersk\w+ zajednic\w*|\budrug\w*|\budruženj\w+ građana|\bdruštven\w+ organizac\w*|\bpolitičk\w+ (?:strank|organizac|aktivnost)\w*|\bpravu na pristup informacijama|\bprebivališt\w*|\bosobn\w+ (?:iskaznic|ime)\w*|\bmatičn\w+|\bsukob\w* interesa|\bodlikovanj\w*|\bstatistik\w*|\barhiv\w*|\bistražn\w+ povjerenstv\w*|\bjavn\w+ okupljanj\w*|\bvanjsk\w+ poslov\w*|\bHrvat\w+ izvan\b|\bnagrad\w*|\bstrateškog planiranja|\bregionaln\w+ razvoj\w*|\bpodručj\w+ posebne državne skrbi|\bpotpomognut\w+ područ\w*|\bjavn\w+ pravobranila\w*|\bračunanj\w+ vremena|\bzaštit\w+ (?:osobnih )?podataka|\bpodatak\w*|\bpodataka\b|\bgrađansk\w+ inicijativ\w*|\botoc\w*|\botok\w*'),
    ('pravosudje', r'\bsud\w*\b|\bsudsk\w*|\bsudova\b|\bkazn\w*|\bkrivičn\w*|\bprekršaj\w*|\bpostupk\w*|\bpostupak\b|\bodvjetni\w*|\bjavn\w+ bilježni\w*|\bovrh\w*|\bovršn\w*|\bstečaj\w*|\bzatvor\w*|\bdržavn\w+ odvjetni\w*|\bpravosu\w*|\bamnesti\w*|\bpomilovanj\w*|\bmirenj\w*|\bparnič\w*|\bsudac\w*|\bsudaca\b|\bvještač\w*|\btumač\w*|\bprobacij\w*|\bžrtv\w+ kaznen\w*|\bbesplatn\w+ pravn\w+ pomoć\w*|\bzaštit\w+ svjedok\w*|\bmučenj\w*'),
    ('gradjansko', r'\bobvezn\w+ odnos\w*|\bvlasništv\w*|\bstvarn\w+ prav\w*|\bobitelj\w*|\bnasljeđ\w*|\btrgovačk\w+ društv\w*|\bzemljišn\w+ knjig\w*|\bnajm\w*|\bzakup\w*|\bstanov\w*|\bstanarsk\w*|\bstamben\w*|\bstanogradnj\w*|\bsudsk\w+ registr\w*|\bzaklad\w*|\bpotrošač\w*|\bautorsk\w+ prav\w*|\bpatent\w*|\bžig\w*|\bintelektualn\w*|\bindustrijsk\w+ (?:vlasništv|dizajn)\w*|\bvlasnik\w*|\bnaknad\w+ za imovinu|\bdenacionalizac\w*|\bpovrat\w* imovin\w*|\bzgrad\w*|\bnekretnin\w*|\bgeodetsk\w*|\bkatast\w*|\bmjenic\w*|\bčekov\w*|\bmeđunarodn\w+ privatn\w+ prav\w*|\bimovinsk\w+ odnos\w*|\bizvlaštenj\w*'),
    ('financije', r'\bbank\w*|\bkreditn\w+ instituc\w*|\btržišt\w+ kapitala|\bosiguranj[aeu]\b|\bosiguranj\w+ (?:i reosiguranj|društv)\w*|\binvesticijsk\w*|\bfond\w*|\bvrijednosn\w+ papir\w*|\bplatn\w+ (?:prometa|usluga|sustav\w*)|\bdevizn\w*|\bnovčan\w+ (?:sustav|jedinic|tržišt)\w*|\bleasing\w*|\bfaktoring\w*|\bštedn\w*|\bnarodn\w+ bank\w*|\bpranj\w+ novca|\bkriptoimovin\w*|\bburz\w*|\buvođenj\w+ eura|\bpreuzimanj\w+ dioničk\w*|\bFinancijsk\w+ agencij\w*|\bindeks\w*|\bgarancijsk\w*|\bkredit\w*'),
    ('okolis', r'\bokoliš\w*|\bprirod[aeiu]\b|\bprirode\b|\botpad\w*|\bvod[aeiu]\b|\bvodama\b|\bvodn\w*|\bšum[aeiu]?\b|\bšuma\w*|\bprostorn\w*|\bgradnj\w*|\bgrađevin\w*|\bgraditeljstv\w*|\benerg\w*|\belektroprivred\w*|\bplin\w*|\bnaft\w*|\brudarstv\w*|\bklim\w*|\bzrak\w*|\bbuk\w*|\bnuklearn\w*|\bradijac\w*|\bzračenj\w*|\bkomunaln\w*|\bpomorsk\w+ dobr\w*|\bmor[aeu]\b|\bmorsk\w*|\bnacionaln\w+ park\w*|\bpark\w* prirode|\bobnov\w*|\bpotres\w*|\bzaštićen\w+ područ\w*|\bgeološk\w*|\btoplinsk\w*|\belektričn\w+ energij\w*|\bobnovljiv\w*|\bugljikovodik\w*|\bkulturn\w+ dobar\w*|\bhidrograf\w*|\bmeteorološk\w*|\bhidrološk\w*|\belementarn\w+ nepogod\w*|\bnezakonito izgrađen\w*|\bgroblj\w*|\bdivlj\w+ vrst\w*|\bživ[ia]\b'),
    ('promet', r'\bpromet\w*|\bcest\w*|\bželjezni\w*|\bpomorsk\w*|\bplovidb\w*|\bzračn\w*|\bluk[aeiu]\b|\blučk\w*|\bvozil\w*|\btelekomunikac\w*|\belektroničk\w+ komunikac\w*|\bpoštansk\w*|\bpošt[aeiu]\b|\bprijevoz\w*|\bautocest\w*|\bbrodov\w*|\bbrodar\w*|\bpilot\w*|\bzrakoplov\w*|\bmost\w*|\bpruga\b|\bPlovput\w*'),
    ('poljo', r'\bpoljoprivred\w*|\bribarstv\w*|\bribolov\w*|\bakvakultur\w*|\bhran[aeiu]\b|\bhrane\b|\bprehramben\w*|\bveterin\w*|\bstočarstv\w*|\bsjemen\w*|\bbilj\w*|\bvin[aou]\b|\bvinogradarstv\w*|\blov\w*\b|\blovstv\w*|\bšumarstv\w*|\bgnoj\w*|\bpesticid\w*|\bmlijek\w*|\bmes[aou]\b|\bduhan\w*|\bpčel\w*|\bekološk\w+ proizvod\w*|\bzadrug\w*|\bagrar\w*|\bživotinj\w*|\bneobrađen\w+ drv\w*|\bdrvenast\w*|\btuč[aeiu]\b|\bstoke\b|\bpremij\w+ za\b'),
    ('obrana', r'\bobran\w*|\boružan\w*|\bvojn\w*|\bvojsk\w*|\bpolicij\w*|\bunutarnj\w+ poslov\w*|\bunutrašnj\w+ poslov\w*|\bsigurnosn\w*|\bsigurnost\w*|\btajn\w*|\bstran\w+ (?:državljan|ac)\w*|\bstranac\w*|\bazil\w*|\bgranic\w*|\boružj\w*|\beksploziv\w*|\bcivilni\w* zaštit\w*|\bcivilne zaštite|\bvatrogas\w*|\bzaštit\w+ i spašavanj\w*|\bzaštit\w+ osoba i imovine|\bmin[aeu]\b|\bminsk\w*|\brazminir\w*|\bkriz\w*|\bobavještajn\w*|\bterorizm\w*|\bdetektiv\w*|\bprivatn\w+ zaštit\w*|\bmigrac\w*|\bputn\w+ isprav\w*|\bmeđunarodn\w+ i privremen\w+ zaštit\w*|\bbiometrijsk\w*|\bcivilnoj službi'),
    ('gosp', r'\btrgovin\w*|\bturiz\w*|\bturističk\w*|\bugostitelj\w*|\bgospodarsk\w*|\bgospodarstv\w*|\bprivred\w*|\bkoncesij\w*|\bjavn\w+ nabav\w*|\btržišn\w+ natjecanj\w*|\bprivatizac\w*|\bpretvorb\w*|\bpoduzeć\w*|\bsanacij\w*|\bcijen\w*|\bmjeriteljstv\w*|\bnorm\w*|\bakreditac\w*|\bulaganj\w*|\bpoduzetni\w*|\bkomor\w*|\bslobodn\w+ zon\w*|\bpoticanj\w*|\bpoticaj\w*|\bstrateškim investicijama|\bjavno-privatn\w*|\bgospodarenj\w*|\btehničk\w+ zahtjev\w*|\bproizvod\w*|\bigr\w+ na sreću|\bkockanj\w*|\blutrij\w*|\bobrt\w*|\binvesticij\w*|\bkonkurentnost\w*|\bplemenit\w+ kovin\w*|\boglašavanj\w*|\brobn\w+ zalih\w*|\binspekcij\w*|\bpotpor\w* za očuvanje'),
    ('obrazovanje', r'\bobrazovanj\w*|\bškol\w*|\bodgoj\w*|\bznanost\w*|\bznanstven\w*|\bsveučili\w*|\bkultur[aeiu]\b|\bkulturn\w*|\bmuzej\w*|\bknjižni\w*|\bspomeni\w*|\bsport\w*|\bšport\w*|\bmedij\w*|\bradio\w*|\btelevizij\w*|\budžbeni\w*|\bumjetnost\w*|\bumjetnič\w*|\bkazališt\w*|\bjezik\w*|\bstudent\w*|\bučenik\w*|\bnastav\w*|\bakademij\w*|\bknjig\w*|\bnakladništv\w*|\barhitekton\w*|\bfilm\w*|\baudiovizual\w*|\bmladi\w*|\bhrvatsk\w+ radiotelevizij\w*|\binovac\w*|\bučilišt\w*|\bkvalifikac\w*|\bprosvjetn\w*|\bmobilnost\w*|\binformiranj\w*'),
]
TOPICS_RX = [(k, re.compile(rx, re.I)) for k, rx in TOPICS]


def topic(name):
    s = name
    s = re.sub(r'^(Ustavni\s+)?Zakon\w*\s+o\s+', '', s)
    for k, rx in TOPICS_RX:
        if rx.search(s):
            return k
    return 'ostalo'


c03 = defaultdict(Counter)
samples = defaultdict(list)
for a in laws:
    if not (1990 <= a['y'] <= 2026):
        continue
    s = subject(a['title'])
    tp = topic(s)
    a['topic'] = tp
    c03[tp][period(a['y'])] += 1
    if len(samples[tp]) < 400:
        samples[tp].append(s)
tot03 = sum(sum(v.values()) for v in c03.values())
D['c03'] = {'periods': sorted({period(y) for y in range(1990, 2027)}), 'topics': [[k, dict(c03[k]), sum(c03[k].values())] for k in [t for t, _ in TOPICS] + ['ostalo']]}
for k, v in sorted(c03.items(), key=lambda x: -sum(x[1].values())):
    n = sum(v.values())
    print(f'c03 {k:12s} {n:5d} {100 * n / tot03:4.1f}%  e.g.', ' | '.join(samples[k][i] for i in (0, len(samples[k]) // 3, 2 * len(samples[k]) // 3, -1))[:260])

# ------------------------------------------------------------------ c04: the Sabor's calendar: laws by month of publication
c04 = defaultdict(lambda: [0] * 12)
nolaw = 0
for a in laws:
    if not a['pub']:
        nolaw += 1
        continue
    y, m = int(a['pub'][:4]), int(a['pub'][5:7])
    if 1990 <= y <= 2026:
        c04[y][m - 1] += 1
D['c04'] = [[y, c04[y]] for y in sorted(c04)]
mo = [sum(c04[y][i] for y in c04 if y <= LAST_FULL) for i in range(12)]
print('c04 laws by month', mo, '| Jul+Dec share', round(100 * (mo[6] + mo[11]) / sum(mo), 1), '| no date', nolaw)

# ------------------------------------------------------------------ c05: the Government amending laws by decree, under the Sabor's authority
DECREE_LAW = re.compile(r'^Uredb\w*\s+o\s+(?:izmjen\w*|dopun\w*|izmjeni)(?:\s+(?:i|te)\s+(?:dopun\w*|izmjen\w*))?\s+(?:Zakona|Zakonika|[A-ZČĆŽŠĐ]\w+(?:og|eg)\s+(?:\w+\s+)?(?:zakona|zakonika))\b')
dl = [a for a in acts if a['kind'] == 'uredba' and DECREE_LAW.search(a['title'])]
MONTHS_G = ['siječnja', 'veljače', 'ožujka', 'travnja', 'svibnja', 'lipnja', 'srpnja', 'kolovoza', 'rujna', 'listopada', 'studenoga', 'prosinca']
MG = {m: i + 1 for i, m in enumerate(MONTHS_G)}
MG.update({'studenog': 11, 'studenoga': 11, 'prosinca': 12})
OV = texts('t-ov.jsonl')
periods = []       # [from, to, law] authorised periods read from each yearly law
for path, t in sorted(OV.items()):
    t = clean(t)
    for d1, m1, y1, d2, m2, y2 in re.findall(r'od (\d{1,2})\.\s*(\w+)\s*(\d{4})?\.?\s*(?:godine\s*)?do (\d{1,2})\.\s*(\w+)\s*(\d{4})\.', t):
        if m1 not in MG or m2 not in MG:
            continue
        yy1 = int(y1) if y1 else int(y2)
        periods.append([f'{yy1}-{MG[m1]:02d}-{int(d1):02d}', f'{int(y2)}-{MG[m2]:02d}-{int(d2):02d}', path])
periods.sort()
# from 1999 every yearly law also authorises the Government "from the day the Sabor is dissolved or its term ends until the
# first sitting of the newly elected Sabor": those windows run from each dissolution decision's day of effect to the
# first sitting its convening decision names
dis_clause = sorted(p for p, t in OV.items() if re.search(r'od dana raspuštanja', clean(t)))
SAB = texts('t-sabor.jsonl')
dissolved, sittings = [], []
for a in acts:
    if a['path'] not in SAB:
        continue
    t = clean(SAB[a['path']])
    if re.search(r'raspuštanju', a['title'], re.I):
        dissolved.append(a['inf'] or a['pub'])
    else:
        m = re.search(r'Sazivam prvo zasjedanje [^0-9]*?(\d{1,2})\.\s*(\w+)\s*(\d{4})', t)
        if m and m.group(2) in MG:
            sittings.append(f'{m.group(3)}-{MG[m.group(2)]:02d}-{int(m.group(1)):02d}')
dissolved.sort(); sittings.sort()
dwin = []
for d in dissolved:
    nxt = next((s for s in sittings if s > d), None)
    if nxt and d >= '1999-01-01':
        dwin.append([d, nxt])
OVLAWS = sorted({a['path'] for a in acts if re.search(r'o ovlasti Vlade', a['title'])})
print('c05 decrees amending laws', len(dl), '| recess periods read', len(periods), 'from', len({p[2] for p in periods}), 'of', len(OVLAWS), 'yearly laws |',
      len(dis_clause), 'laws with the dissolution clause | dissolution windows', dwin, '| sittings', sittings)


def in_window(day):
    if any(w[0] <= day < w[1] for w in dwin):
        return 'dissolved'
    if any(p[0] <= day <= p[1] for p in periods):
        return 'recess'
    return ''


c05 = []
for a in sorted(dl, key=lambda a: a['pub'] or ''):
    day = a['pub']
    if not day:
        continue
    c05.append([day, a['title'][:160], in_window(day), a['src'] == 'h'])
D['c05'] = {'decrees': c05, 'periods': [p[:2] for p in periods], 'dwin': dwin,
            'laws': [[a['y'], a['path'], a['title'][:140], a['inf'] or a['pub']] for a in acts if re.search(r'o ovlasti Vlade', a['title'])]}
cov = [d for d in c05 if d[0] >= '2000-12-15']
print('c05 since the first dated periods:', len(cov), 'decrees,', Counter(d[2] for d in cov), '| outside:', [(d[0], d[1][:60]) for d in cov if not d[2]][:14])
amended_by_decree = Counter(subject(re.sub(r'^Uredb\w*', 'Zakon', d[1])) for d in c05)
print('c05 laws most often amended by decree', amended_by_decree.most_common(8))
D['c05']['top'] = amended_by_decree.most_common(10)

# ------------------------------------------------------------------ c06: how long new laws are (one file per article)
ART = TREE['zakon_articles']
c06 = defaultdict(list)
longest = []
for a in laws:
    if a['am'] or a['rep'] or a['src'] == 'h':
        continue
    n = ART.get(a['path'], 0)
    if not n:
        continue
    c06[a['y']].append(n)
    longest.append([n, a['y'], a['title'][:120], a['path']])
longest.sort(reverse=True)


def q(v, p):
    v = sorted(v)
    k = (len(v) - 1) * p
    f, c = math.floor(k), math.ceil(k)
    return v[f] + (v[c] - v[f]) * (k - f)


D['c06'] = {'years': [[y, len(v), q(v, .5), q(v, .25), q(v, .75), max(v)] for y, v in sorted(c06.items()) if 1990 <= y <= 2026],
            'longest': longest[:12]}
dec = lambda lo, hi: statistics.median([n for y, v in c06.items() if lo <= y <= hi for n in v])
D['c06']['dec'] = [[lo, hi, dec(lo, hi), sum(len(v) for y, v in c06.items() if lo <= y <= hi)] for lo, hi in [(1990, 1999), (2000, 2009), (2010, 2019), (2020, 2026)]]
print('c06 median articles by decade', D['c06']['dec'], '| longest', longest[:3])

# ------------------------------------------------------------------ c07: when laws take effect, counted from publication
def lag_cat(pub, inf):
    g = (d8(inf) - d8(pub)).days
    if g < 0:
        return None
    if g == 0: return 'd0'
    if g == 1: return 'd1'
    if g < 8: return 'd2'
    if g == 8: return 'd8'
    if inf[5:] == '01-01': return 'jan1'
    if inf[8:] == '01': return 'm1'
    return 'later'


c07 = defaultdict(Counter)
neg = 0
for a in laws:
    if a['src'] == 'h' or not a['pub'] or not a['inf']:
        continue
    c = lag_cat(a['pub'], a['inf'])
    if c is None:
        neg += 1
        continue
    c07[period(a['y'])][c] += 1
    c07['y' + str(a['y'])][c] += 1
D['c07'] = {'periods': [[p, dict(c07[p])] for p in sorted(k for k in c07 if not k.startswith('y'))],
            'years': [[int(k[1:]), dict(v)] for k, v in sorted(c07.items()) if k.startswith('y')]}
print('c07 periods', [(p, dict(v)) for p, v in D['c07']['periods']], '| before publication', neg)

# ------------------------------------------------------------------ c08: the busiest days of entry into force
days = defaultdict(Counter)
stems = defaultdict(Counter)
for a in acts:
    if a['src'] == 'h' or not a['inf']:
        continue
    days[a['inf']][KG.get(a['kind'], 'ostalo')] += 1
    stems[a['inf']][' '.join(a['title'].split()[:5])] += 1
top = sorted(days.items(), key=lambda kv: -sum(kv[1].values()))[:15]
D['c08'] = [{'d': d, **dict(c), 'stems': stems[d].most_common(3)} for d, c in top]
D['c08_basis'] = {'eu': META['basis_eu'], 'euro': META['basis_euro']}
for r in D['c08'][:8]:
    print('c08', r['d'], sum(v for k, v in r.items() if k not in ('d', 'stems')), r['stems'][:2])

# ------------------------------------------------------------------ c09: the most amended laws
names = defaultdict(lambda: {'am': Counter(), 'new': []})
for a in laws:
    if a['am']:
        s = subject(a['title'])
        names[base_key(s)]['am'][a['y']] += 1
        names[base_key(s)].setdefault('label', s)
for a in laws:
    if not a['am'] and not a['rep']:
        k = base_key(a['title'])
        if k in names:
            names[k]['new'].append([a['y'], a['pub'] or '', a['title']])
            names[k]['label'] = a['title']
rank = sorted(names.items(), key=lambda kv: -sum(kv[1]['am'].values()))
D['c09'] = [{'name': v['label'], 'by': {str(y): n for y, n in sorted(v['am'].items())}, 'n': sum(v['am'].values()), 'new': sorted(v['new'])} for k, v in rank[:22]]
for r in D['c09'][:12]:
    print('c09', r['n'], r['name'], [n[0] for n in r['new']])

# ------------------------------------------------------------------ c10: how soon a new law is first amended (Kaplan-Meier, by decade)
END = d8(META['last_in_force'])


def first_event(a):
    am, ex = None, None
    for date, how, ref, t in a['ab']:
        if not date:
            continue
        if t.lower().startswith('ispravak') or 'ustavnog suda' in t.lower():
            continue
        if 'amend' in how:
            am = min(am or date, date)
        if 'repeal' in how or 'replace' in how:
            ex = min(ex or date, date)
    return am, ex


km_rows = defaultdict(list)
for a in laws:
    if a['am'] or a['rep'] or not a['reg'] or not a['inf'] or not a['pub']:
        continue
    start = d8(a['pub'])
    am, ex = first_event(a)
    if am and (not ex or am <= ex):
        km_rows[a['y'] // 10 * 10].append(((d8(am) - start).days / 365.25, 1))
    else:
        stop = d8(ex) if ex else END
        km_rows[a['y'] // 10 * 10].append((max(0.0, (stop - start).days / 365.25), 0))


def km(rows, horizon=12):
    rows = sorted(rows)
    n, s, out, i = len(rows), 1.0, [[0, 1.0, len(rows)]], 0
    at_risk = n
    while i < len(rows):
        t = rows[i][0]
        d = c = 0
        while i < len(rows) and rows[i][0] == t:
            d += rows[i][1]; c += 1 - rows[i][1]; i += 1
        if d:
            s *= (1 - d / at_risk)
            out.append([round(t, 3), round(s, 4), at_risk])
        at_risk -= d + c
        if t > horizon:
            break
    return out


D['c10'] = {}
for dcd, rows in sorted(km_rows.items()):
    curve = km(rows)
    med = next((p[0] for p in curve if p[1] <= .5), None)
    s1 = next((p[1] for p in reversed(curve) if p[0] <= 1), 1)
    s2 = next((p[1] for p in reversed(curve) if p[0] <= 2), 1)
    s5 = next((p[1] for p in reversed(curve) if p[0] <= 5), 1)
    D['c10'][str(dcd)] = {'n': len(rows), 'events': sum(r[1] for r in rows), 'curve': curve, 'median': med, 's1': s1, 's2': s2, 's5': s5,
                          'maxt': max(r[0] for r in rows)}
    print('c10', dcd, len(rows), 'laws,', sum(r[1] for r in rows), 'amended; median years', med and round(med, 2), '| unamended after 1, 2, 5 years', round(s1, 3), round(s2, 3), round(s5, 3))

# ------------------------------------------------------------------ c11: what still stands, by period of publication
def st_cat(s):
    if s == 'in force': return 'inforce'
    if s.startswith('amended'): return 'amended'
    if s.startswith('replaced'): return 'replaced'
    if s.startswith('repealed'): return 'repealed'
    if s.startswith('cited'): return 'cited'
    return 'other'


c11 = defaultdict(Counter)
for a in laws:
    if a['am'] or a['rep'] or not a['reg']:
        continue
    c11[period(a['y'])][st_cat(a['status'])] += 1
D['c11'] = [[p, dict(c11[p])] for p in sorted(c11)]
print('c11', D['c11'])

# ------------------------------------------------------------------ c12: corrections (ispravci)
IS = list(csv.DictReader(open(os.path.join(R, 'ispravci.csv'), encoding='utf-8')))
BYREF = {(a['y'], a['doc']): a for a in acts}


def corrected_act(r):
    """the act a correction corrects, by its Narodne novine number (year and document)"""
    try:
        y = int(r['corrects_nn'].split('/')[1])
        return BYREF.get((y, int(r['corrects_doc'])))
    except (ValueError, IndexError):
        return None


PUB = {}
for r in IS:
    a = corrected_act(r)
    if a and a['pub']:
        PUB[r['corrects_slug'] or f"{r['corrects_nn']}#{r['corrects_doc']}"] = a['pub']
CK = {'zakon': 'zakon', 'uredba': 'uredba', 'pravilnik': 'pravilnik', 'odluka': 'odluka'}
c12y = defaultdict(Counter)
lagb = defaultdict(Counter)
corrected = defaultdict(set)
LB = [(7, 'w1'), (30, 'm1'), (91, 'm3'), (365, 'y1'), (10 ** 6, 'more')]
lags = defaultdict(list)
for r in IS:
    y = int(r['correction_date'][:4])
    k = CK.get(r['corrects_kind'], 'ostalo')
    c12y[y][k] += 1
    ca = corrected_act(r)
    if ca and ca['pub']:
        g = (d8(r['correction_date']) - d8(ca['pub'])).days
        if g >= 0:
            lags[k].append(g)
            lagb[k if k in ('zakon',) else 'other'][next(lb for lim, lb in LB if g <= lim)] += 1
    if ca:
        corrected[ca['kind']].add((ca['y'], ca['doc']))
nlaw_corr = len(corrected['zakon'])
by_period_corr = defaultdict(lambda: [0, 0])
for a in laws:
    by_period_corr[period(a['y'])][0] += 1
    by_period_corr[period(a['y'])][1] += (a['y'], a['doc']) in corrected['zakon']
D['c12'] = {'years': [{'y': y, **c12y[y]} for y in sorted(c12y)], 'lag': {k: dict(v) for k, v in lagb.items()},
            'median': {k: statistics.median(v) for k, v in lags.items() if v}, 'n': len(IS), 'laws_corrected': nlaw_corr,
            'laws': len(laws), 'matched': sum(1 for r in IS if corrected_act(r)), 'periods': [[p, *v] for p, v in sorted(by_period_corr.items())]}
print('c12', len(IS), 'corrections | laws corrected', nlaw_corr, 'of', D['c12']['laws'], '| median days', {k: v for k, v in D['c12']['median'].items()}, '| lag', D['c12']['lag'])

# ------------------------------------------------------------------ c13: the Constitution, version by version
WORD = re.compile(r'[\wČĆŽŠĐčćžšđ]+(?:[-–][\wČĆŽŠĐčćžšđ]+)*', re.U)


def const_words(files):
    def key(p):
        m = re.search(r'clanak-(\d+)([a-z]?)', p)
        return (0, 0, '') if 'izvorisne' in p else (1, int(m.group(1)), m.group(2))
    txt = '\n'.join(re.sub(r'^#+ .*$', '', files[p], flags=re.M) for p in sorted(files, key=key))
    return WORD.findall(txt)


vers = [v for v in jl('ustav.jsonl') if v['author'].startswith('NN ')]
c13 = []
prev = None
PHR = {'zupanijski': r'Županijsk\w+ dom\w*', 'eu': r'Europsk\w+ unij\w*', 'brak': r'životna zajednica žene i muškarca', 'vlada': r'\bVlad\w+\b',
       'predsjednik': r'Predsjedni\w+ Republike', 'referendum': r'\breferendum\w*'}
for v in vers:
    w = const_words(v['files'])
    arts = sum(1 for p in v['files'] if 'clanak-' in p)
    full = ' '.join(v['files'].values())
    ph = {k: len(re.findall(rx, full)) for k, rx in PHR.items()}
    row = {'date': v['date'], 'nn': v['author'], 'kind': v['kind'], 'words': len(w), 'arts': arts, 'ph': ph, 'add': 0, 'del': 0}
    if prev is not None:
        sm = difflib.SequenceMatcher(None, prev, w, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op in ('replace', 'delete'):
                row['del'] += i2 - i1
            if op in ('replace', 'insert'):
                row['add'] += j2 - j1
    prev = w
    c13.append(row)
D['c13'] = c13
for r in c13:
    print('c13', r['date'], r['nn'], r['words'], 'words', r['arts'], 'articles, +', r['add'], '-', r['del'], r['ph'])

# ------------------------------------------------------------------ c14: the Constitutional Court repealing provisions
UK = list(csv.DictReader(open(os.path.join(R, 'ustavni-sud-ukidanja.csv'), encoding='utf-8')))


def act_type(r):
    act, gz = r['act'].strip(), r['gazette']
    if re.search(r'\b(?:Općin\w*|Grad[a]?|Županij\w*|Kotar\w*|SO\s|Skupštin\w+ općin\w*|Izvršn\w+ vijeć\w*|općin\w+|grada\b|županije\b|mjesn\w+ zajednic\w*)\b', act) or (gz and not gz.startswith('Narodne novine')):
        return 'local'
    if re.match(r'(?i)(Ustavn\w+ )?zakon\w*|\w+(og|eg) zakon\w*|zakon\w*$|\w+ zakon\w*', act) or re.search(r'(?i)\bzakon(a|u|ik|ika)?\b', act.split(' ')[0] if act else ''):
        return 'law'
    if re.match(r'(?i)uredb\w*', act):
        return 'decree'
    if re.match(r'(?i)(pravilnik|naredb|naputak|naputk|uput|odluk|rješenj|program|plan|poslovnik|statut|zaključ|tarif)', act):
        return 'reg'
    return 'other'


dec14 = {}
for r in UK:
    c = r['case_no']
    t = act_type(r)
    if c not in dec14:
        dec14[c] = {'y': int(r['published'][:4]), 'types': Counter(), 'acts': set(), 'act': r['act'][:120], 'action': r['action'], 'd': r['published']}
    dec14[c]['types'][t] += 1
    dec14[c]['acts'].add(r['act'].strip()[:120])
c14y = defaultdict(Counter)
law_hits = Counter()
for c, v in dec14.items():
    t = 'law' if v['types']['law'] else v['types'].most_common(1)[0][0]
    v['t'] = t
    c14y[v['y']][t] += 1
    if v['types']['law']:
        for an in v['acts']:
            if act_type({'act': an, 'gazette': ''}) == 'law':
                nm = an[:1].upper() + an[1:]
                nm = nominative(nm) if re.match(r'^(?:Zakona|Zakonika|\w+(?:og|eg) zakona)\b', nm) else nm
                nm = subject(nm)
                if re.search(r'Ustavnom sudu', nm):          # the Court's own act, cited as the basis of the decision
                    continue
                law_hits[nm] += 1
recent = []        # the decisions since 2015 that struck out provisions of laws: the law (in the nominative) and the provisions
for r in UK:
    if r['published'] < '2015' or act_type(r) != 'law':
        continue
    nm = r['act'].strip()
    nm = nm[:1].upper() + nm[1:]
    nm = nominative(nm) if re.match(r'^(?:Zakona|Zakonika|\w+(?:og|eg) zakona)\b', nm) else nm
    nm = subject(nm)
    if re.search(r'Ustavnom sudu', nm):
        continue
    arts = clean(r['articles'])
    arts = arts if re.match(r'^(?:članak|članci|čl\.|dio|točk|stavak)', arts, re.I) else ''
    if not any(x[1] == r['case_no'] and x[2] == nm for x in recent):
        recent.append([r['published'], r['case_no'], nm, arts if len(arts) <= 110 else arts[:arts.rfind(' ', 0, 108)] + ' …', r['action']])
D['c14'] = {'years': [{'y': y, **c14y[y]} for y in sorted(c14y)], 'n': len(dec14), 'points': len(UK), 'recent': sorted(recent, reverse=True),
            'laws': law_hits.most_common(12), 'list': sorted([[v['d'], c, v['t'], v['act'], v['action']] for c, v in dec14.items()])}
print('c14 recent', len(recent), recent[:4])
print('c14 decisions', len(dec14), 'points', len(UK), Counter(v['t'] for v in dec14.values()), law_hits.most_common(5))

# ------------------------------------------------------------------ c15: turnout in the elections to the Sabor
IZ = {x['p'].rsplit('/', 1)[0]: x['t'] for x in jl('t-izbori.jsonl')}
TITLES = {a['path']: a['title'] for a in jl('acts.jsonl') if a['kind'] == 'izbori'}
ROM = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10, 'XI': 11, 'XII': 12}
N_ = r'(\d{1,3}(?:\.\d{3})+|\d+)'
c15 = defaultdict(dict)
c15xi = {}
miss = []
for path, t in IZ.items():
    title = TITLES.get(path, '')
    y = int(path.split('/')[1])
    if not re.search(r'Sabor', title, re.I) or re.search(r'Europsk|predsjednik|Državnoodvjetničk', title, re.I):
        continue
    m = re.search(r'\bu\s+([IVX]+)\.\s+izbornoj jedinici', title, re.I)
    if not m:
        continue
    unit = ROM.get(m.group(1).upper())
    tt = clean(t)
    reg = re.search(r'Od ukupno\s+' + N_ + r'\s+biračа?', tt) or re.search(r'Od ukupno\s+' + N_ + r'\s+birač', tt)
    vot = re.search(r'prema (?:glasačkim )?listićima\)?\s+(?:glasovalo\s+(?:je\s+)?)?' + N_ + r'\s+birač', tt) or re.search(r'glasovalo je \(prema (?:glasačkim )?listićima\)\s+' + N_, tt)
    if not reg or not vot:
        miss.append(path)
        continue
    R_, V_ = int(reg.group(1).replace('.', '')), int(vot.group(1).replace('.', ''))
    if unit <= 10:
        c15[y][unit] = [R_, V_]
    elif unit == 11:
        c15xi[y] = [R_, V_]
D['c15'] = {str(y): {str(u): v for u, v in sorted(us.items())} for y, us in sorted(c15.items())}
D['c15_xi'] = {str(y): v for y, v in sorted(c15xi.items())}
print('c15 district XI', D['c15_xi'])
for y, us in sorted(c15.items()):
    print('c15', y, len(us), 'units', round(100 * sum(v[1] for v in us.values()) / sum(v[0] for v in us.values()), 2), '%')
print('c15 not read', miss)

# ------------------------------------------------------------------ c16: laws whose first three articles name EU acts
EU = texts('t-eu.jsonl')
RX_TR = re.compile(r'(?:u\s+(?:hrvatsko|hrvatski)\s+(?:zakonodavstvo|pravni\s+(?:sustav|poredak))|u\s+(?:zakonodavstvo|pravni\s+(?:sustav|poredak))\s+Republike\s+Hrvatske)\s+(?:se\s+)?(?:preuzima\w*|prenos\w*|uključuj\w*)|\bDirektiv\w*\b', re.I)
RX_REG = re.compile(r'\bUredb\w*\s+\((?:EU|EZ|EEZ|Euratom)\)|\bUredb\w*\s+(?:Vijeća|Komisije|Europskog\s+parlamenta)\b|\bprovedb\w*\s+Uredb\w*\s+\(|\bprovedb\w*\s+(?:propisa|uredbi)\s+Europske\s+unije', re.I)
RX_AQ = re.compile(r'pravn\w+\s+stečevin\w+\s+Europske\s+unije|pravnom\s+stečevinom', re.I)
c16 = defaultdict(lambda: [0, 0, 0, 0])
eu_ex = defaultdict(list)
for a in laws:
    if a['src'] == 'h' or a['path'] not in EU:
        continue
    t = EU[a['path']]
    tr, rg, aq = bool(RX_TR.search(t)), bool(RX_REG.search(t)), bool(RX_AQ.search(t))
    r = c16[a['y']]
    r[0] += 1
    if tr or rg or aq:
        r[1] += 1
        r[2] += tr
        r[3] += rg and not tr
        if len(eu_ex[a['y']]) < 2:
            eu_ex[a['y']].append(a['title'][:90])
D['c16'] = [[y, *c16[y]] for y in sorted(c16) if 1990 <= y <= 2026]
n_after = [r for r in D['c16'] if 2014 <= r[0] <= LAST_FULL]
print('c16 laws with text', sum(r[1] for r in D['c16']), '| naming EU acts', sum(r[2] for r in D['c16']), '| 2013', [r for r in D['c16'] if r[0] == 2013],
      '| 2014-2025 share', round(100 * sum(r[2] for r in n_after) / sum(r[1] for r in n_after), 1), '| first years', [(r[0], r[2]) for r in D['c16'] if r[2]][:6], eu_ex[2005], eu_ex[2007])

# ------------------------------------------------------------------ c17: international treaties, by the other party
CTRY = [
    ('SI', r'\bSlovenij\w*|\bSlovensk\w*'), ('HU', r'\bMađarsk\w*'), ('DE', r'\bNjemačk\w*'), ('BA', r'\bBosn\w*\s+i\s+Hercegovin\w*|\bBiH\b'),
    ('US', r'Sjedinjen\w+\s+Američk\w+\s+Država|\bAmeričk\w+\s+Država'), ('RS', r'\bSrbij\w*|Savezn\w+\s+Republik\w+\s+Jugoslavij\w*|Srbij\w+\s+i\s+Crn\w+\s+Gor\w*'),
    ('ME', r'\bCrn\w+\s+Gor\w*'), ('BG', r'\bBugarsk\w*'), ('RU', r'\bRusk\w+\s+Federacij\w*'), ('MK', r'\bMakedonij\w*'), ('TR', r'\bTursk\w*'),
    ('IT', r'\bTalijansk\w*|\bItalij\w*'), ('CZ', r'\bČešk\w*'), ('PL', r'\bPoljsk\w*'), ('SE', r'\bŠvedsk\w*'), ('UA', r'\bUkrajin\w*'),
    ('CN', r'\bKin[aeiu]\b|Narodn\w+\s+Republik\w+\s+Kin\w*'), ('SK', r'\bSlovačk\w*'), ('AT', r'\bAustrij\w*'), ('MD', r'\bMoldov\w*'), ('XK', r'\bKosov\w*'),
    ('AL', r'\bAlbanij\w*'), ('PT', r'\bPortugal\w*'), ('IL', r'\bIzrael\w*'), ('IR', r'\bIran\w*'), ('LT', r'\bLitv\w*'), ('IN', r'\bIndij\w*'),
    ('LV', r'\bLatvij\w*'), ('FR', r'\bFrancusk\w*'), ('GB', r'Ujedinjen\w+\s+Kraljev\w+|Velik\w+\s+Britanij\w*'), ('ID', r'\bIndonezij\w*'),
    ('NL', r'\bNizozemsk\w*'), ('EE', r'\bEstonij\w*'), ('KR', r'\bKorej\w*'), ('BE', r'\bBelgij\w*'), ('FI', r'\bFinsk\w*'), ('BY', r'\bBjelarus\w*'),
    ('QA', r'\bKatar\w*'), ('AZ', r'\bAzerbajdžan\w*'), ('RO', r'\bRumunjsk\w*'), ('VA', r'Svet\w+\s+Stolic\w*'), ('NO', r'\bNorvešk\w*'),
    ('GR', r'\bHelensk\w*|\bGrčk\w*'), ('EG', r'\bEgipt\w*|\bEgipat\b'), ('ES', r'\bŠpanjolsk\w*'), ('LU', r'\bLuksemburg\w*'), ('DK', r'\bDansk\w*'),
    ('SM', r'San\s+Marin\w*'), ('JO', r'\bJordan\w*'), ('TH', r'\bTajland\w*'), ('CY', r'\bCipr\w*'), ('CH', r'\bŠvicarsk\w*'), ('KW', r'\bKuvajt\w*'),
    ('AM', r'\bArmenij\w*'), ('MA', r'\bMarok\w*'), ('JP', r'\bJapan\w*'), ('CA', r'\bKanad\w*'), ('AU', r'\bAustralij\w*'), ('CL', r'\bČile\w*'),
    ('AR', r'\bArgentin\w*'), ('BR', r'\bBrazil\w*'), ('MX', r'\bMeksik\w*'), ('MT', r'\bMalt[aeiu]\b'), ('IE', r'\bIrsk\w*'), ('IS', r'\bIsland\w*'),
    ('LI', r'\bLihtenštajn\w*'), ('MC', r'\bMonak\w*'), ('AD', r'\bAndor\w*'), ('GE', r'\bGruzij\w*'), ('KZ', r'\bKazahstan\w*'), ('UZ', r'\bUzbekistan\w*'),
    ('TM', r'\bTurkmenistan\w*'), ('KG', r'\bKirgist\w*|\bKirgiz\w*'), ('TJ', r'\bTadžikistan\w*'), ('MN', r'\bMongolij\w*'), ('VN', r'\bVijetnam\w*'),
    ('PH', r'\bFilipin\w*'), ('MY', r'\bMalezij\w*'), ('SG', r'\bSingapur\w*'), ('AE', r'Ujedinjen\w+\s+Arapsk\w+\s+Emirat\w*'), ('SA', r'Saudijsk\w+\s+Arabij\w*'),
    ('OM', r'\bOman\w*'), ('BH', r'\bBahre\w*'), ('LB', r'\bLibanon\w*'), ('SY', r'\bSirij\w*'), ('IQ', r'\bIrak\w*'), ('PK', r'\bPakistan\w*'),
    ('AF', r'\bAfganistan\w*'), ('TN', r'\bTunis\w*'), ('DZ', r'\bAlžir\w*'), ('LY', r'\bLibij\w*'), ('ZA', r'Južnoafričk\w+'), ('CU', r'\bKub[aeiu]\b'),
    ('VE', r'\bVenezuel\w*'), ('PE', r'\bPeru\b|\bPerua\b'), ('UY', r'\bUrugvaj\w*'), ('PY', r'\bParagvaj\w*'), ('CO', r'\bKolumbij\w*'), ('EC', r'\bEkvador\w*'),
    ('NZ', r'Nov\w+\s+Zeland\w*'), ('LK', r'Šri\s+Lank\w*'), ('BD', r'\bBangladeš\w*'), ('NP', r'\bNepal\w*'), ('MU', r'\bMauricijus\w*'), ('SN', r'\bSenegal\w*'),
    ('KE', r'\bKenij\w*'), ('ET', r'\bEtiopij\w*'), ('NG', r'\bNigerij\w*'), ('GH', r'\bGan[aeiu]\b'), ('AO', r'\bAngol\w*'), ('CV', r'Zelenortsk\w*'),
    ('SC', r'\bSejšel\w*'), ('BW', r'\bBocvan\w*'), ('NA', r'\bNamibij\w*'), ('ZW', r'\bZimbabv\w*'), ('MZ', r'\bMozambik\w*'), ('ZM', r'\bZambij\w*'),
    ('SD', r'\bSudan\w*'), ('KH', r'\bKambodž\w*'), ('LA', r'\bLaos\w*'), ('MM', r'\bMjanmar\w*'), ('PS', r'\bPalestin\w*'), ('CR', r'\bKostarik\w*'),
    ('PA', r'\bPanam\w*'), ('DO', r'Dominikansk\w*'), ('BO', r'\bBolivij\w*'),
]
CTRY += [('KW', r'\bKuwait\w*'), ('KZ', r'\bKazakstan\w*'), ('MX', r'\bMeksičk\w*'), ('BE', r'\bFlandrij\w*|\bValonij\w*'), ('CA', r'\bQuebec\w*'), ('AL', r'\balbanlie\b'),
         ('FJ', r'\bFidži\w*'), ('GG', r'\bGuernsey\w*'), ('JE', r'\bJersey\w*')]
CTRY_RX = [(k, re.compile(rx, re.I)) for k, rx in CTRY]
ORG = re.compile(r'Europsk\w+\s+(?:komisij|zajednic|unij|investicijsk|banke|organizacij|agencij|svemirsk|središnj|policijsk|ured|sud|vijeć|fond)\w*|Komisij\w+\s+Europsk\w*|'
                 r'Međunarodn\w+\s+(?:bank|agencij|organizacij|fond|udrug|centr|ured|instituc|kaznen|sud|zajednic|udruženj|korporacij|unij|komisij)\w*|Svjetsk\w+\s+(?:bank|organizacij|zdravstven)\w*|'
                 r'Razvojn\w+\s+bank\w*|Vijeć\w+\s+Europe|Sjevernoatlantsk\w*|\bNATO\b|Ujedinjenih\s+naroda|\bUN\b|OESS|Organizacij\w+|Fond\w*\s+Vijeća|Europskog\s+parlamenta|'
                 r'Europske\s+banke|Bank\w+\s+za\s+|Agencij\w+|Interpol\w*|Eurojust\w*|Europol\w*|Frontex\w*|Euratom\w*|CERN|Inicijativ\w+|Zajednic\w+|\bRACVIAC\b|\bECMWF\b|Europsk\w+\s+centr\w*', re.I)


def parties(title):
    t = re.sub(r'(?i)\brepublike(?=[a-zčćžšđ])', 'Republike ', title)          # 'republikeslovenije' as printed
    t = re.sub(r'Velike\s+Britanije\s+i\s+Sjeverne\s+Irske', 'Velike Britanije', t)
    t = re.sub(r'Republik\w+\s+Hrvatsk\w+|\bHrvatsk\w+', ' ', t)
    found = []
    for k, rx in CTRY_RX:
        if rx.search(t):
            if k == 'ME' and re.search(r'Srbij\w+\s+i\s+Crn\w+\s+Gor\w*', t) and len(re.findall(r'\bCrn\w+\s+Gor\w*', t)) == 1:
                continue
            found.append(k)
    return found


c17 = defaultdict(lambda: defaultdict(int))
inst = defaultdict(Counter)
kinds17 = Counter()
unmatched = []
for a in INTL:
    y = a['y']
    t = a['title']
    inst_k = 'law' if re.match(r'^Zakon\b', t) else 'decree' if re.match(r'^(Uredb|Odluk)\w*', t) else 'other'
    inst[y // 10 * 10][inst_k] += 1
    ps = parties(t)
    if 1 <= len(ps) <= 3:
        for p in ps:
            c17[p][y] += 1
        kinds17['bilateral' if len(ps) == 1 else 'few'] += 1
    elif len(ps) >= 4:
        c17['multi'][y] += 1; kinds17['multi4'] += 1
    elif ORG.search(t):
        c17['org'][y] += 1; kinds17['org'] += 1
    else:
        c17['multi'][y] += 1; kinds17['multi'] += 1
        if 'između' in t:
            unmatched.append(t[:150])
rows17 = [{'k': k, 'n': sum(v.values()), 'by': {str(y): n for y, n in sorted(v.items())}} for k, v in c17.items()]
rows17.sort(key=lambda r: -r['n'])
D['c17'] = {'rows': rows17, 'inst': {str(k): dict(v) for k, v in sorted(inst.items())}, 'kinds': dict(kinds17), 'n': len(INTL)}
print('c17', len(INTL), 'treaty acts', dict(kinds17), [(r['k'], r['n']) for r in rows17[:14]], '| inst', D['c17']['inst'])
for u in unmatched[:15]:
    print('   c17 unmatched "between":', u)

# ------------------------------------------------------------------ c18: the minimum wage in three currencies, and indexation in the 1990s
MW = texts('t-mw.jsonl')
INF = {a['path']: a for a in acts}
AMT = re.compile(r'(?:iznos\w*\s+od|iznosi|iznosu\s+od|bruto\s+iznosu\s+od)\s+([\d.]+(?:,\d+)?)\s*(kuna|kn|eura|HRD|hrvatskih\s+dinara)')
mw = []
for path, t in sorted(MW.items()):
    a = INF.get(path)
    if not a or not re.search(r'minimaln\w+ plać', a['title'], re.I) or re.search(r'osnivanju|prestanku važenja|osiguranju sredstava|osiguravanju sredstava|ostvarivanju prava', a['title'], re.I):
        continue
    tc = clean(t)
    if path == 'uredba/1993/275':
        m = re.search(r'Akontacija minimalne plaće.*?iznosu od\s+([\d.]+)\s*(HRD)', tc)
    else:
        m = AMT.search(tc)
    if not m:
        print('   c18 no amount', path, a['title'][:80])
        continue
    v = float(m.group(1).replace('.', '').replace(',', '.'))
    cur = {'kuna': 'HRK', 'kn': 'HRK', 'eura': 'EUR', 'HRD': 'HRD'}.get(m.group(2).split()[0], 'HRD')
    eur = v / 1000 / 7.5345 if cur == 'HRD' else v / 7.5345 if cur == 'HRK' else v
    mw.append([a['inf'] or a['pub'], v, cur, round(eur, 2), a['title'][:150], path, a['pub']])
mw.sort()
# the conversion rates, as the acts state them
RT = texts('t-rates.jsonl')
k_rate = re.search(r'u omjeru\s+(\d+)\s+hrvatskih dinara za jednu kunu', clean(RT.get('odluka/1994/685', '')))
e_rate = re.search(r'Fiksni tečaj konverzije određen je na\s+([\d,]+)\s+kuna za jedan euro', clean(RT.get('odluka/2022/1302', '')))
assert k_rate and k_rate.group(1) == '1000', 'kuna rate not found'
assert e_rate and e_rate.group(1) == '7,53450', 'euro rate not found'
IDX = re.compile(r'\busklađivanj\w*|\bvalorizacij\w*|\brevalorizacij\w*', re.I)
idx = Counter()
for a in acts:
    if IDX.search(a['title']):
        idx[a['y']] += 1
D['c18'] = {'mw': mw, 'idx': sorted(idx.items()), 'rates': {'kuna': k_rate.group(1), 'euro': e_rate.group(1)}}
for r in mw:
    print('c18', r[0], r[1], r[2], r[3], r[5])
print('c18 indexation decisions', sorted(idx.items())[:12])

# ------------------------------------------------------------------ c19: the income tax rates of municipalities and cities (since 2024)
TX = texts('t-tax.jsonl')
num = r'(\d{1,2}(?:[,.]\d{1,2})?)\s*%'
c19 = []
skip19 = []
for path, t in sorted(TX.items()):
    a = INF.get(path)
    if not a:
        continue
    tc = clean(t)
    title = a['title']
    if re.match(r'^(?:Odluka o (?:izmjen|dopun)\w*|Izmjen\w*|Dopun\w*)', title, re.I):
        skip19.append(path); continue
    lo = re.search(r'niž\w*\s+(?:godišnj\w+\s+)?(?:porezn\w+\s+)?stop\w*[^0-9%]{0,80}?' + num, tc, re.I)
    hi = re.search(r'viš\w*\s+(?:godišnj\w+\s+)?(?:porezn\w+\s+)?stop\w*[^0-9%]{0,80}?' + num, tc, re.I)
    if not (lo and hi):
        two = re.findall(r'porezna stopa od\s+' + num, tc)
        if len(two) >= 2:
            lo_v, hi_v = two[0], two[1]
        else:
            skip19.append(path); continue
    else:
        lo_v, hi_v = lo.group(1), hi.group(1)
    unit = 'zagreb' if re.search(r'Grada Zagreba', title, re.I) else 'opcina' if re.search(r'\bopćin\w*', title, re.I) else 'grad' if re.search(r'\bgrad\w*', title, re.I) else '?'
    m = re.search(r'(?:Općin\w*|Grad\w*)\s+(.+)$', title, re.I)
    c19.append([a['y'], unit, float(lo_v.replace(',', '.')), float(hi_v.replace(',', '.')), (m.group(1) if m else title)[:60], a['inf'] or '', path])
D['c19'] = {'rows': c19, 'skipped': len(skip19)}
for y in sorted({r[0] for r in c19}):
    rr = [r for r in c19 if r[0] == y]
    print('c19', y, len(rr), Counter(r[1] for r in rr), '| 20/30:', sum(1 for r in rr if r[2] == 20 and r[3] == 30), '| lo range', min(r[2] for r in rr), max(r[2] for r in rr), '| hi range', min(r[3] for r in rr), max(r[3] for r in rr))
print('c19 skipped (amendments or unread)', len(skip19), skip19[:8])

# ------------------------------------------------------------------ c20: the boundary of the maritime domain, mapped from the acts' own coordinates
PD = texts('t-pd.jsonl')


def gk_to_ll(y, x, zone):
    """Gauss-Krueger (Bessel 1841, zone 5 or 6, scale 0.9999) -> lon, lat (no datum shift: tens to hundreds of metres)"""
    a, f = 6377397.155, 1 / 299.1528128
    k0, lon0, fe = 0.9999, math.radians(3 * zone), zone * 1e6 + 500000
    e2 = f * (2 - f); ep2 = e2 / (1 - e2)
    m = x / k0
    mu = m / (a * (1 - e2 / 4 - 3 * e2 ** 2 / 64 - 5 * e2 ** 3 / 256))
    e1 = (1 - math.sqrt(1 - e2)) / (1 + math.sqrt(1 - e2))
    p1 = mu + (3 * e1 / 2 - 27 * e1 ** 3 / 32) * math.sin(2 * mu) + (21 * e1 ** 2 / 16 - 55 * e1 ** 4 / 32) * math.sin(4 * mu) + (151 * e1 ** 3 / 96) * math.sin(6 * mu) + (1097 * e1 ** 4 / 512) * math.sin(8 * mu)
    n1 = a / math.sqrt(1 - e2 * math.sin(p1) ** 2)
    t1 = math.tan(p1) ** 2
    c1 = ep2 * math.cos(p1) ** 2
    r1 = a * (1 - e2) / (1 - e2 * math.sin(p1) ** 2) ** 1.5
    d = (y - fe) / (n1 * k0)
    lat = p1 - (n1 * math.tan(p1) / r1) * (d ** 2 / 2 - (5 + 3 * t1 + 10 * c1 - 4 * c1 ** 2 - 9 * ep2) * d ** 4 / 24 + (61 + 90 * t1 + 298 * c1 + 45 * t1 ** 2 - 252 * ep2 - 3 * c1 ** 2) * d ** 6 / 720)
    lon = lon0 + (d - (1 + 2 * t1 + c1) * d ** 3 / 6 + (5 - 2 * c1 + 28 * t1 - 3 * c1 ** 2 + 8 * ep2 + 24 * t1 ** 2) * d ** 5 / 120) / math.cos(p1)
    return math.degrees(lon), math.degrees(lat)


NUMS = r'(\d{1,3}(?:[ .]\d{3})+(?:[.,]\d+)?|\d{6,7}(?:[.,]\d+)?)'
PAIR = re.compile(NUMS + r'\s+' + NUMS)


def val(s):
    s = s.replace(' ', '')
    if s.count('.') > 1 or (s.count('.') == 1 and len(s.split('.')[1]) == 3 and ',' not in s):
        s = s.replace('.', '')
    return float(s.replace(',', '.'))


c20, bad20, drop20 = [], 0, []
pd_acts = [a for a in acts if re.search(r'granic\w* pomorskog dobra', a['title'], re.I)]
for a in pd_acts:
    t = PD.get(a['path'], '')
    pts = []
    for s1, s2 in PAIR.findall(t):
        try:
            yv, xv = val(s1), val(s2)
        except ValueError:
            continue
        if 5.3e6 < yv < 6.7e6 and 4.6e6 < xv < 5.2e6:
            pts.append((yv, xv))
    ll = None
    if pts:
        zone = Counter(int(p[0] // 1e6) for p in pts).most_common(1)[0][0]
        sel = [p for p in pts if int(p[0] // 1e6) == zone]
        lon, lat = gk_to_ll(sum(p[0] for p in sel) / len(sel), sum(p[1] for p in sel) / len(sel), zone)
        # the coast runs from Istria (west of 14° E, north of 44.3° N) down to Dalmatia (east of 14.8° E): a point west
        # of Dalmatia's coast in the open sea means a misprinted zone digit, and is left off the map
        if 13.2 < lon < 19.6 and 42.2 < lat < 46.6 and (lat >= 44.3 or lon > 14.8):
            ll = [round(lon, 4), round(lat, 4), len(sel)]
        else:
            bad20 += 1
            print('   c20 left off the map:', a['path'], a['title'][:80], round(lon, 3), round(lat, 3))
    ko = re.search(r'k\.\s*o\.\s*([^,]+?)(?:,|\s+-\s+|\s+na\s+|\s+za\s+|$)', a['title'])
    c20.append([a['y'], a['kind'], a['title'][:150], ll, (ko.group(1).strip() if ko else ''), a['inf'] or a['pub'] or '', 1 if pts else 0])
    if pts and not ll:
        drop20.append([a['y'], ko.group(1).strip() if ko else '', a['path']])
D['c20'] = c20
D['c20_drop'] = drop20
print('c20', len(c20), 'acts on the boundary;', sum(1 for r in c20 if r[3]), 'with coordinates;', bad20, 'outside the box', Counter(r[1] for r in c20), sorted(Counter(r[0] for r in c20).items()))
print('c20 lon/lat range', min(r[3][0] for r in c20 if r[3]), max(r[3][0] for r in c20 if r[3]), min(r[3][1] for r in c20 if r[3]), max(r[3][1] for r in c20 if r[3]))

# ------------------------------------------------------------------ profile
kinds_now = Counter(a['kind'] for a in acts if a['src'] == 'r')
PF.update({
    'built': TODAY, 'head': META['sha'], 'commits': META['commits'], 'last_in_force': META['last_in_force'],
    'by_domain': META['by_domain'], 'kinds': dict(kinds_now), 'treaties': len(INTL),
    'courts': TREE['courts'], 'local_units': TREE['local_units'], 'local_files': TREE['tops'].get('local', 0),
    'izbori': sum(1 for x in jl('acts.jsonl') if x['kind'] == 'izbori'), 'ustav_versions': len(c13),
    'corrections': len(IS), 'repeal_points': len(UK), 'files': sum(TREE['tops'].values()),
    'acts_repo': sum(1 for a in acts if a['src'] == 'r'), 'acts_unlinked': sum(1 for a in acts if a['src'] == 'r' and not a['reg']),
    'laws_linked': sum(1 for a in laws if a['reg']), 'removed_laws': len(TREE.get('removed_laws', [])),
    'local_acts': sum(1 for x in jl('nn-acts.jsonl') if x['files'].startswith('local/')),
    'court_db': TREE['courts'].get('ustavni-sud', 0), 'vrhovni': TREE['courts'].get('vrhovni-sud', 0),
})
json.dump({'charts': D, 'profile': PF}, open(os.path.join(B, 'data.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('data.json', os.path.getsize(os.path.join(B, 'data.json')))
