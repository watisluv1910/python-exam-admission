def main(d):
    d1 = bin(int(d['Q1']))[2:].zfill(10)
    d2 = bin(int(d['Q2']))[2:].zfill(4)
    d3 = bin(0)[2:].zfill(9)
    d4 = bin(int(d['Q4']))[2:].zfill(3)
    d5 = bin(int(d['Q5']))[2:].zfill(6)
    return hex(int(d5 + d4 + d3 + d2 + d1, 2))


if __name__ == "__main__":
    print(main({'Q1': '66', 'Q2': '15', 'Q4': '4', 'Q5': '37'}),
          main({'Q1': '252', 'Q2': '1', 'Q4': '3', 'Q5': '34'}),
          main({'Q1': '607', 'Q2': '11', 'Q4': '4', 'Q5': '17'}),
          main({'Q1': '25', 'Q2': '2', 'Q4': '4', 'Q5': '14'}))
