import re


def main(s):
    res = []
    for block in re.finditer(r"\[([A-Za-z0-9_\+\-\\:=\s]+)\]", s):
        components = re.sub(r'\\|::=', ' ', block.group(1).strip()).split()
        res.append((components[1], components[2]))
    return res


if __name__ == "__main__":
    print(main("<block> [ new tiaala ::= inat][new arbior ::= raso_763 ][ new iseror ::= soares_610 ] </block>"))
