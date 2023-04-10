def main(n):
    return (lambda: main(n - 1) - main(n - 1) ** 3 / 95 - 1,
            lambda: -99e-02)[n == 0]()


if __name__ == "__main__":
    print(main(8))
