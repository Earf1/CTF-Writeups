import sys
from pathlib import Path
ROW_ORDER = [12, 11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ROWSET_TO_CHAR = {
    frozenset(): ' ',
    frozenset({12,1}): 'A',
    frozenset({12,2}): 'B',
    frozenset({12,3}): 'C',
    frozenset({12,4}): 'D',
    frozenset({12,5}): 'E',
    frozenset({12,6}): 'F',
    frozenset({12,7}): 'G',
    frozenset({12,8}): 'H',
    frozenset({12,9}): 'I',
    frozenset({11,1}): 'J',
    frozenset({11,2}): 'K',
    frozenset({11,3}): 'L',
    frozenset({11,4}): 'M',
    frozenset({11,5}): 'N',
    frozenset({11,6}): 'O',
    frozenset({11,7}): 'P',
    frozenset({11,8}): 'Q',
    frozenset({11,9}): 'R',
    frozenset({0,2}): 'S',
    frozenset({0,3}): 'T',
    frozenset({0,4}): 'U',
    frozenset({0,5}): 'V',
    frozenset({0,6}): 'W',
    frozenset({0,7}): 'X',
    frozenset({0,8}): 'Y',
    frozenset({0,9}): 'Z',
    frozenset({12,5,8}): '[',
    frozenset({11,5,8}): ']',
    frozenset({12,7,8}): '#',
    frozenset({11,7,8}): 'Δ',
    frozenset({11,3,8}): '$',
    frozenset({2,8}): '&',
    frozenset({5,8}): ':',
    frozenset({1}): '1',
    frozenset({0}): '0',
    frozenset({3}): '3',
    frozenset({7,11}): 'P',
    frozenset({11,3}): 'L',
    frozenset({11,5}): 'N',
    frozenset({11,9}): 'R',
    frozenset({11,7}): 'P',
    frozenset({12,2}): 'B',
    frozenset({0,4}): 'U',
    frozenset({12,8}): 'H',
    frozenset({11,1}): 'J',
    frozenset({5,8,11}): ']',
    frozenset({5,8,12}): '[',
    frozenset({3,11}): 'L',
}

def chunk_bits(bitstring, n=12):
    for i in range(0, len(bitstring), n):
        yield bitstring[i:i+n]

def rows_from_chunk(chunk):
    rows = set()
    for bit, row in zip(chunk, ROW_ORDER):
        if bit == '1':
            rows.add(row)
    return frozenset(rows)

def decode_bitstream(bitstring):
    out = []
    for c in chunk_bits(bitstring, 12):
        rows = rows_from_chunk(c)
        glyph = ROWSET_TO_CHAR.get(rows)
        if glyph is None:
            glyph = '?'
        out.append(glyph)
    return ''.join(out)

def read_bits_from_file(path):
    s = Path(path).read_text().strip()
    s = ''.join(s.split())
    if len(s) % 12 != 0:
        s = s[:len(s) - (len(s) % 12)]
    return s

def main():
    default_path = "/mnt/data/transmission.txt"
    infile = sys.argv[1] if len(sys.argv) > 1 else default_path
    bits = read_bits_from_file(infile)
    decoded = decode_bitstream(bits)
    print(decoded)

if __name__ == "__main__":
    main()
