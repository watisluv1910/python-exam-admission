import struct


def main(s):
    d = {}
    a2 = {}
    b1 = []
    b7 = {}
    a5 = {}
    a8 = {}

    base_address = 4

    d['A1'] = struct.unpack_from('>I', s, base_address)[0]
    base_address += 4

    b_address = struct.unpack_from('>H', s, base_address)[0]
    base_address += 2

    for i in range(3):
        c123 = {}

        c_address = struct.unpack_from('>I', s, b_address)[0]
        b_address += 4

        c123['C1'] = struct.unpack_from('>I', s, c_address)[0]
        c_address += 4
        c123['C2'] = struct.unpack_from('>b', s, c_address)[0]
        c_address += 1
        c123['C3'] = struct.unpack_from('>h', s, c_address)[0]
        c_address += 2

        b1.append(c123)

    a2['B1'] = b1

    a2['B2'] = struct.unpack_from('>d', s, b_address)[0]
    b_address += 8
    a2['B3'] = struct.unpack_from('>h', s, b_address)[0]
    b_address += 2
    a2['B4'] = struct.unpack_from('>h', s, b_address)[0]
    b_address += 2
    a2['B5'] = struct.unpack_from('>q', s, b_address)[0]
    b_address += 8
    a2['B6'] = struct.unpack_from('>f', s, b_address)[0]
    b_address += 4

    d_address = struct.unpack_from('>H', s, b_address)[0]
    b_address += 2

    d1_size = struct.unpack_from('>H', s, d_address)[0]
    d_address += 2
    d1_address = struct.unpack_from('>I', s, d_address)[0]
    d_address += 4

    d1 = []
    for i in range(d1_size):
        d1.append(struct.unpack_from('>B', s, d1_address)[0])
        d1_address += 1

    d2 = []
    for i in range(3):
        d2.append(struct.unpack_from('>b', s, d_address)[0])
        d_address += 1

    b7['D1'], b7['D2'] = d1, d2

    a2['B7'] = b7

    d['A2'] = a2
    d['A3'] = struct.unpack_from('>d', s, base_address)[0]
    base_address += 8
    d['A4'] = struct.unpack_from('>I', s, base_address)[0]
    base_address += 4

    a5['E1'] = struct.unpack_from('>Q', s, base_address)[0]
    base_address += 8
    a5['E2'] = struct.unpack_from('>I', s, base_address)[0]
    base_address += 4
    a5['E3'] = struct.unpack_from('>f', s, base_address)[0]
    base_address += 4

    d['A5'] = a5
    d['A6'] = struct.unpack_from('>h', s, base_address)[0]
    base_address += 2
    d['A7'] = struct.unpack_from('>I', s, base_address)[0]
    base_address += 4

    f1 = []
    for i in range(6):
        f1.append(struct.unpack_from('>B', s, base_address)[0])
        base_address += 1

    a8['F1'], a8['F2'] = f1, struct.unpack_from('>q', s, base_address)[0]
    base_address += 8

    d['A8'] = a8

    return d


print(main(b'\xe0QHKs\x8bW\xca\x00^\xbf\xbf=\x12\xb2W:@\x16\xcb\x85\x9e\x17d&\x92D6'
           b',\x87\xd2\x88lv\xbf\nR\xe6\xdbW%\x0c\xf9\xc6\x8d\xa4\xcc~\xf3\xdc\t\xcc'
           b'B\xbc/\xca\x84Q\r\xbb~\xee$\x1e\xd8\xa2\xe8\xe98gU\xa0\x8c\x1ca\x06'
           b'\xfe\x0cQN`\x11yx\xef\x00\x06\x00\x00\x00O\xe1K\x86\x00\x00\x00:\x00\x00'
           b'\x00A\x00\x00\x00H?\xe6\xf1\t\x86\xbae^\x97[z\xd9!\x93\x12\xef9r\xa3/\xbe#'
           b'=\x89\x00U'))
