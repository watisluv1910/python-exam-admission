import struct


def main(s):
    # unpack A1
    d = {'A1': struct.unpack_from('>I', s, 4)[0]}

    # unpack B1
    b1 = []
    b_address = struct.unpack_from('>H', s, 8)[0]
    for i in range(3):
        c123 = {}
        c_address = struct.unpack_from('>I', s, b_address)[0]
        c123['C1'], c123['C2'], c123['C3'] = struct.unpack_from('>Ibh', s, c_address)
        b1.append(c123)
        b_address += 4
    a2 = {'B1': b1}

    # unpack B2 - B6
    b_address = struct.unpack_from('>H', s, b_address)[0] + 2

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

    # unpack B7
    d1_size, d1_address = struct.unpack_from('>HH', s, b_address)
    b_address += 6
    d1 = struct.unpack_from(f'>{d1_size}B', s, d1_address)
    d2 = struct.unpack_from('>bbb', s, b_address)
    b7 = {'D1': d1, 'D2': d2}
    a2['B7'] = b7

    # unpack A2 - A8
    d['A2'] = a2
    d['A3'], d['A4'] = struct.unpack_from('>di', s, b_address + 4)
    a5 = {
        'E1': struct.unpack_from('>Q', s, b_address + 12)[0],
        'E2': struct.unpack_from('>I', s, b_address + 20)[0],
        'E3': struct.unpack_from('>f', s, b_address + 24)[0],
    }
    d['A5'] = a5
    d['A6'], d['A7'] = struct.unpack_from('>hi', s, b_address + 28)
    f1 = struct.unpack_from('>6B', s, b_address + 32)
    a8 = {'F1': f1, 'F2': struct.unpack_from('>q', s, b_address + 38)[0]}
    d['A8'] = a8

    return d


if __name__ == "__main__":
    print(main(b'\xe0QHKs\x8bW\xca\x00^\xbf\xbf=\x12\xb2W:@\x16\xcb\x85\x9e\x17d&\x92D6'
               b',\x87\xd2\x88lv\xbf\nR\xe6\xdbW%\x0c\xf9\xc6\x8d\xa4\xcc~\xf3\xdc\t\xcc'
               b'B\xbc/\xca\x84Q\r\xbb~\xee$\x1e\xd8\xa2\xe8\xe98gU\xa0\x8c\x1ca\x06'
               b'\xfe\x0cQN`\x11yx\xef\x00\x06\x00\x00\x00O\xe1K\x86\x00\x00\x00:\x00\x00'
               b'\x00A\x00\x00\x00H?\xe6\xf1\t\x86\xbae^\x97[z\xd9!\x93\x12\xef9r\xa3/\xbe#'
               b'=\x89\x00U'))
