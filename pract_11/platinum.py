from struct import *


def main(source):
    a = {}

    # В задании ошибочная информация о начальной сигнатуре
    global_address = 3

    a1 = []
    for b_iter in range(2):

        b = {}

        b1 = {}

        c1 = []
        c1_size = unpack_from('>I', source, global_address)[0]
        global_address += 4
        c1_address = unpack_from('>I', source, global_address)[0]
        global_address += 4
        for c1_iter in range(c1_size):
            c1.append(unpack_from('>b', source, c1_address)[0])
            c1_address += 1

        c2 = unpack_from('>H', source, global_address)[0]
        global_address += 2

        b1['C1'] = c1
        b1['C2'] = c2
        b['B1'] = b1

        b2 = {}

        d_address = unpack_from('>H', source, global_address)[0]
        global_address += 2
        d1 = unpack_from('>b', source, d_address)[0]
        d_address += 1
        d2 = unpack_from('>f', source, d_address)[0]
        d_address += 4
        d3 = unpack_from('>h', source, d_address)[0]
        d_address += 2
        d4 = unpack_from('>h', source, d_address)[0]
        d_address += 2

        b2['D1'] = d1
        b2['D2'] = d2
        b2['D3'] = d3
        b2['D4'] = d4
        b['B2'] = b2

        b3 = unpack_from('>i', source, global_address)[0]
        global_address += 4
        b['B3'] = b3

        a1.append(b)
    a['A1'] = a1

    a2 = unpack_from('>f', source, global_address)[0]
    global_address += 4
    a['A2'] = a2
    a3 = unpack_from('>q', source, global_address)[0]
    global_address += 8
    a['A3'] = a3

    a4_size = unpack_from('>H', source, global_address)[0]
    global_address += 2
    a4_address = unpack_from('>I', source, global_address)[0]
    global_address += 4
    a4 = ''
    for a4_iter in range(a4_size):
        a4 += str(unpack_from('>c', source, a4_address)[0])[2]
        a4_address += 1
    a['A4'] = a4
    a5 = unpack_from('>i', source, global_address)[0]
    global_address += 4
    a['A5'] = a5
    a6 = unpack_from('>H', source, global_address)[0]
    global_address += 2
    a['A6'] = a6
    a7 = unpack_from('>d', source, global_address)[0]
    global_address += 8
    a['A7'] = a7

    a8 = []
    a8_size = 4
    for a8_iter in range(a8_size):
        a8.append(unpack_from('>q', source, global_address)[0])
        global_address += 8
    a['A8'] = a8

    return a
