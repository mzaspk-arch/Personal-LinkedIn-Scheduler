"""Turn a caption file into LinkedIn-ready text.

LinkedIn has no bold button for posts, so **text** is converted to Unicode bold
letters (works on desktop and mobile). Everything else is kept as written.

Usage: python3 tools/linkedin_format.py captions/NAME.txt  -> prints the post text
"""
import re, sys

def _bold_char(c):
    o = ord(c)
    if 'A' <= c <= 'Z': return chr(0x1D5D4 + o - 65)
    if 'a' <= c <= 'z': return chr(0x1D5EE + o - 97)
    if '0' <= c <= '9': return chr(0x1D7EC + o - 48)
    return c

def bold(text):
    return ''.join(_bold_char(c) for c in text)

def to_linkedin(caption):
    out = re.sub(r'\*\*(.+?)\*\*', lambda m: bold(m.group(1)), caption)
    return out.strip() + '\n'

if __name__ == '__main__':
    sys.stdout.write(to_linkedin(open(sys.argv[1], encoding='utf-8').read()))
