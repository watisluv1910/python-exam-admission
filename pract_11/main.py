import struct


def main(s):
    d = {}
    a4 = {}
    b2 = {}
    b4 = []

    base_address = 3

    d.setdefault('A1', struct.unpack_from('>h', s, base_address)[0])
    base_address += 2
    d.setdefault('A2', struct.unpack_from('>I', s, base_address)[0])
    base_address += 4
    d.setdefault('A3', struct.unpack_from('>f', s, base_address)[0])
    base_address += 4

    new_address_b = struct.unpack_from('>I', s, base_address)[0]
    base_address += 4
    a4.setdefault('B1', struct.unpack_from('>d', s, new_address_b)[0])
    new_address_b += 8

    new_address_c = struct.unpack_from('>H', s, new_address_b)[0]
    new_address_b += 2
    b2.setdefault('C1', struct.unpack_from('>d', s, new_address_c)[0])
    new_address_c += 8

    c2 = ''
    for i in range(5):
        c2 += str(struct.unpack_from('>c', s, new_address_c)[0])[2]
        new_address_c += 1
    b2.setdefault('C2', c2)

    b2.setdefault('C3', struct.unpack_from('>B', s, new_address_c)[0])
    new_address_c += 1

    a4.setdefault('B2', b2)

    a4.setdefault('B3', struct.unpack_from('>H', s, new_address_b)[0])
    new_address_b += 2

    for i in range(3):
        d123 = {}

        new_address_d = struct.unpack_from('>H', s, new_address_b)[0]
        new_address_b += 2

        d1 = [struct.unpack_from('>q', s, new_address_d)[0]]
        new_address_d += 8
        d1.append(struct.unpack_from('>q', s, new_address_d)[0])
        new_address_d += 8
        d123.setdefault('D1', d1)

        new_size = struct.unpack_from('>I', s, new_address_d)[0]
        new_address_d += 4
        new_address_d_2 = struct.unpack_from('>H', s, new_address_d)[0]
        new_address_d += 2

        d2 = []
        for j in range(new_size):
            d2.append(struct.unpack_from('>H', s, new_address_d_2)[0])
            new_address_d_2 += 2
        d123.setdefault('D2', d2)
        d123.setdefault('D3', struct.unpack_from('>q', s, new_address_d)[0])
        new_address_d += 8
        b4.append(d123)

    a4.setdefault('B4', b4)
    a4.setdefault('B5', struct.unpack_from('>B', s, new_address_b)[0])
    new_address_b += 1

    d.setdefault('A4', a4)

    d.setdefault('A5', struct.unpack_from('>Q', s, base_address)[0])
    base_address += 8
    d.setdefault('A6', struct.unpack_from('>I', s, base_address)[0])
    base_address += 4

    return d


print(main(b'DTA\xa5\xcf\x99\xa3\x1f\xde>Y\xa9{\x00\x00\x00\x9b\xd1zQ{\xdb\x0f\xdf'
           b'|\xe5\x99\xe5\xa5\xbf\xda]\xf4?gtddhehb\x85\x88/\xb1yG\x8b\xf1\xd4\xb5'
           b'9F&\x9a\xf4\n\xf9`\x88L\xfc\x8d\x92\x00\x00\x00\x03\x00+O\x8f\x9f\x1b^'
           b'\x1e\xbc\xc6\xdd\x182\x80\x86\xafP\xe3\x19\x89G\xa1<\xca\x03\xd8\xc5'
           b'\xdb\xad\xa3Lc\xb4\xa0\x00\x00\x00\x04\x00O\xff\xed%`s\xf71\xa3\x1f?\xe4'
           b'\x9d\xff\xd3\xa9\xfc\xc4\x12\xcbKV\xcc\xc1\xe6\x97\x01Wr\x8a\xbb\xba'
           b'\x98\x00\x00\x00\x04\x00u\xc2\xe7\x95Le\xfd\xd0<\xbf\xe82gj\xde\xad6\x00'
           b'\x1d\x19\xb0\x001\x00W\x00}\xec'))
