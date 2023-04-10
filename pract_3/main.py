import math


def main(a, n, b):
    res = 0
    for k in range(1, b + 1):
        for c in range(1, n + 1):
            for i in range(1, a + 1):
                res += 42 * math.pow(20 - 77 * i ** 2, 2) + \
                       63 * k ** 3 + c ** 2 / 98
    return res


if __name__ == "__main__":
    print(main(6, 8, 2))
