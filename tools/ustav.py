"""Prints the Croatian Constitution, or one article of it, as it stood on a given day, from this repository's history.

    python tools/ustav.py 2012-01-01 ustav 62          # čl. 62 on 1 January 2012
    python tools/ustav.py 2020-01-01 ustav             # the whole Constitution on 1 January 2020
    python tools/ustav.py 2012-01-01 ustav izvorisne-osnove

Each commit carries the day its change took effect in an `In-force:` trailer (git cannot store dates before 1970, so
the trailer, not the commit date, is the source of truth). The text in force on a day is the last commit on or before
it that changed the files. Articles are numbered as in the consolidated text of that day. Standard library only.
"""
import datetime as dt
import re
import subprocess
import sys


def git(*args: str) -> str:
    return subprocess.run(['git', *args], capture_output=True, text=True, encoding='utf-8', check=True).stdout


def order(path: str) -> tuple:
    name = path.split('/', 1)[1][:-3]
    m = re.fullmatch(r'clanak-(\d+)', name)
    return (1, int(m.group(1))) if m else (0, 0)


def file_for(key: str) -> str:
    m = re.fullmatch(r'(\d+)', key)
    return f'clanak-{int(m.group(1)):03d}.md' if m else (key if key.endswith('.md') else f'{key}.md')


def commit_on(day: str, act: str) -> str:
    out = git('log', '--format=%H%x09%(trailers:key=In-force,valueonly,separator=)', 'main', '--', act)
    for line in out.splitlines():
        h, _, d = line.partition('\t')
        if d.strip() and d.strip() <= day:
            return h
    return ''


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    day, act = sys.argv[1], sys.argv[2]
    dt.date.fromisoformat(day)
    commit = commit_on(day, act)
    if not commit:
        sys.exit(f'{act} is not in the record on {day}.')
    if len(sys.argv) > 3:
        name = file_for(sys.argv[3])
        try:
            sys.stdout.write(git('show', f'{commit}:{act}/{name}'))
        except subprocess.CalledProcessError:
            sys.exit(f'{act}/{name} was not in the text on {day}.')
        return
    files = [f for f in git('ls-tree', '-r', '--name-only', commit, f'{act}/').split('\n') if f.endswith('.md')]
    for f in sorted(files, key=order):
        sys.stdout.write(git('show', f'{commit}:{f}') + '\n')


if __name__ == '__main__':
    main()
