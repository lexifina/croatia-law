"""Functional smoke test of the built Croatian law repository: the things a reader does with it work. Standard library only.

    python -X utf8 scripts/croatia-law/test_repo.py [--repo ../croatia-law] [--record]
    python -X utf8 tools/test_repo.py                   # from inside the repository

It asserts that:
1. `git blame` on a changed article names an amending act as author of its lines;
2. tools/ustav.py gives the text before and after known amendments, and each equals the file at that act's tag;
3. `git log --follow` on a file lists its amending acts in the order they took effect;
4. every tag resolves to a commit, and every commit but the documentation commit has an `In-force:` trailer;
5. no commit is authored by Lexifina except the documentation commit (the last one);
6. every git or tool command in the README's table runs and prints something.
With --record the result is written to verification.json next to this script (for REPRODUCE.md).
"""
import argparse
import json
import re
import shlex
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LAW = re.compile(r'^NN \d+/\d{4}( \([^)]+\))?$')


def default_repo() -> Path:
    if (HERE.parent / '.git').exists():
        return HERE.parent
    return HERE.parents[2] / 'croatia-law'


class Smoke:
    def __init__(self, repo: Path):
        self.repo = repo
        self.results: list[tuple[str, bool, str]] = []

    def git(self, *args: str) -> str:
        out = subprocess.run(['git', *args], cwd=self.repo, capture_output=True, text=True, encoding='utf-8')
        if out.returncode:
            raise AssertionError(f'git {" ".join(args)}: {out.stderr.strip()}')
        return out.stdout

    def tool(self, *args: str) -> str:
        out = subprocess.run([sys.executable, '-X', 'utf8', 'tools/ustav.py', *args], cwd=self.repo, capture_output=True,
                             text=True, encoding='utf-8')
        if out.returncode:
            raise AssertionError(f'ustav {" ".join(args)}: {out.stderr.strip()}')
        return out.stdout

    def check(self, name: str, fn):
        try:
            detail = fn() or ''
            self.results.append((name, True, detail))
            print(f'PASS {name}: {detail}')
        except AssertionError as exc:
            self.results.append((name, False, str(exc)))
            print(f'FAIL {name}: {exc}')

    # 1
    def blame(self):
        out = self.git('blame', '--line-porcelain', 'main', '--', 'ustav/clanak-062.md')
        authors = {l[7:] for l in out.splitlines() if l.startswith('author ')}
        assert authors and all(LAW.match(a) for a in authors), f'unexpected authors {authors}'
        assert 'NN 5/2014 (referendum 2013)' in authors, f'the 2013 change is not among the authors {authors}'
        assert len(authors) >= 2, f'only {authors}'
        return f'ustav/clanak-062.md lines by {", ".join(sorted(authors))}'

    # 2
    def on_date(self):
        done = []
        for path, tag, before, after, prev_tag in [
                ('ustav/clanak-062.md', 'nn/2014-5', '2013-11-30', '2013-12-01', 'nn/2010-76'),
                ('ustav/clanak-007.md', 'nn/2001-55', '2001-03-27', '2001-03-28', 'nn/2001-28')]:
            a, b = self.tool(before, 'ustav', path.split('-')[1][:3].lstrip('0')), self.tool(after, 'ustav', path.split('-')[1][:3].lstrip('0'))
            assert a and b and a != b, f'{path}: no change between {before} and {after}'
            assert b == self.git('show', f'{tag}:{path}'), f'{path} on {after} is not the file at {tag}'
            if prev_tag == 'nn/2010-76':
                assert a == self.git('show', f'{prev_tag}:{path}'), f'{path} on {before} is not the file at {prev_tag}'
            done.append(f'{path} {before} != {after}')
        whole = self.tool('1991-01-01', 'ustav')
        assert 'Članak 1.' in whole and 'Članak 142.' in whole, 'whole Constitution on 1991-01-01 is incomplete'
        return '; '.join(done)

    # 3
    def follow(self):
        path = 'ustav/clanak-062.md'
        out = self.git('log', '--follow', '--format=%an%x09%(trailers:key=In-force,valueonly,separator=)', 'main', '--', path)
        rows = [l.split('\t') for l in out.splitlines() if l]
        assert len(rows) >= 4, f'{path}: {len(rows)} commits'
        days = [d.strip() for _, d in rows]
        assert days == sorted(days, reverse=True), f'{path}: not in date order {days}'
        assert all(LAW.match(a) for a, _ in rows), f'{path}: authors {[a for a, _ in rows]}'
        return f'{path} {len(rows)} commits, newest first: {days}'

    # 4
    def tags_and_trailers(self):
        tags = self.git('tag').split()
        assert tags, 'no tags'
        for t in tags:
            self.git('rev-parse', '--verify', '-q', f'{t}^{{commit}}')
        rows = self.git('log', '--format=%H%x09%an%x09%(trailers:key=In-force,valueonly,separator=)', 'main').splitlines()
        missing = [r for r in rows[1:] if not r.split('\t')[2].strip()]
        assert not missing, f'{len(missing)} commits without In-force, e.g. {missing[:2]}'
        bad = [r for r in rows if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', r.split('\t')[2].strip())]
        assert not bad, f'malformed In-force {bad[:2]}'
        return f'{len(tags)} tags resolve; {len(rows) - 1} law commits carry In-force'

    # 5
    def lexifina(self):
        rows = self.git('log', '--format=%H%x09%an%x09%ae%x09%cn', 'main').splitlines()
        by_lex = [r for r in rows if r.split('\t')[1] == 'Lexifina']
        assert len(by_lex) == 1 and by_lex[0] == rows[0], f'{len(by_lex)} commits by Lexifina'
        assert all(r.split('\t')[3] == 'Lexifina' for r in rows), 'a committer other than Lexifina'
        assert all(r.split('\t')[2].endswith('.invalid') for r in rows[1:]), 'a law author without an .invalid address'
        authors = {r.split('\t')[1] for r in rows[1:]}
        assert all(LAW.match(a) for a in authors), f'unexpected authors {authors}'
        return f'only the documentation commit {rows[0][:10]} is by Lexifina; {len(authors)} distinct authors'

    # 6
    def readme(self):
        text = (self.repo / 'README.md').read_text(encoding='utf-8')
        table = text[text.index('## The questions'):text.index('## The dates')]
        cmds = [c for c in re.findall(r'`([^`]+)`', table) if c.startswith(('git ', 'python '))]
        assert len(cmds) >= 7, f'only {len(cmds)} commands found'
        for c in cmds:
            args = shlex.split(c)
            if args[0] == 'python':
                args = [sys.executable, '-X', 'utf8', *args[1:]]
            out = subprocess.run(args, cwd=self.repo, capture_output=True, text=True, encoding='utf-8')
            assert out.returncode == 0, f'{c}: exit {out.returncode} {out.stderr.strip()[:200]}'
            assert out.stdout.strip(), f'{c}: printed nothing'
        return f'{len(cmds)} README commands ran and printed output'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default=None)
    ap.add_argument('--record', action='store_true')
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    s = Smoke(Path(args.repo) if args.repo else default_repo())
    s.check('blame names an act', s.blame)
    s.check('text before and after an amendment', s.on_date)
    s.check('log --follow in date order', s.follow)
    s.check('tags resolve, In-force on every law commit', s.tags_and_trailers)
    s.check('only the documentation commit is by Lexifina', s.lexifina)
    s.check('README commands run', s.readme)
    ok = all(r[1] for r in s.results)
    print(f'{sum(r[1] for r in s.results)}/{len(s.results)} passed')
    if args.record:
        p = HERE / 'verification.json'
        rec = json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}
        rec['smoke'] = {'passed': sum(r[1] for r in s.results), 'total': len(s.results),
                        'results': [{'test': n, 'ok': o, 'detail': d} for n, o, d in s.results]}
        p.write_text(json.dumps(rec, indent=1, sort_keys=True, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    raise SystemExit(0 if ok else 1)


if __name__ == '__main__':
    main()
