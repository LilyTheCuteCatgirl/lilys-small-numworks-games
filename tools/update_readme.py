from pathlib import Path
import argparse
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- GAME_TABLE_START -->'
END = '<!-- GAME_TABLE_END -->'
NAMES = {
    '2048': '2048',
    'chrome_dino': 'Chrome Dino',
    'flappy_bird': 'Flappy Bird',
    'pacman': 'Pac-Man',
    'space_invaders': 'Space Invaders',
}
ORDER = [
    'chess', 'chrome_dino', 'snake', 'flappy_bird', '2048',
    'pacman', 'tetris', 'minesweeper', 'pong', 'space_invaders',
    'breakout', 'frogger',
]

def make_table(folder):
    scripts = sorted(folder.glob('*.py'), key=lambda p: (
        ORDER.index(p.stem) if p.stem in ORDER else len(ORDER), p.name.lower()))
    if not scripts:
        raise RuntimeError('No .py games in ' + str(folder))
    lines = ['| Games | File Size |', '|---|---:|']
    total = 0
    for path in scripts:
        size = len(path.read_bytes())
        total += size
        name = NAMES.get(path.stem, path.stem.replace('_', ' ').title())
        lines.append(f'| [{name}](games/{path.name}) | {size:,} bytes |')
    lines.append(f'| **Total** | **{total:,} bytes** |')
    return '\n'.join(lines)

def update(text, table):
    block = START + '\n' + table + '\n' + END
    if START in text or END in text:
        if text.count(START) != 1 or text.count(END) != 1:
            raise ValueError('README has mismatched or duplicate table markers')
        return re.sub(re.escape(START) + r'.*?' + re.escape(END),
                      lambda _: block, text, count=1, flags=re.S)
    heading = re.search(r'(?m)^## Available Games\s*\n', text)
    if not heading:
        return text.rstrip() + '\n\n## Available Games\n\n' + block + '\n'
    after = heading.end()
    next_heading = re.search(r'(?m)^#{1,6}[ \t]+\S', text[after:])
    stop = after + next_heading.start() if next_heading else len(text)
    return text[:after] + '\n' + block + '\n\n' + text[stop:].lstrip('\n')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Exit 1 if README table is outdated')
    args = parser.parse_args()
    readme = ROOT / 'README.md'
    old = readme.read_text(encoding='utf-8')
    new = update(old, make_table(ROOT / 'games'))
    if args.check:
        if new != old:
            print('README game table is out of date. Run python tools/update_readme.py')
            return 1
        print('README game table is up to date.')
    elif new != old:
        readme.write_text(new, encoding='utf-8', newline='\n')
        print('Updated README game table.')
    else:
        print('Already up to date.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
