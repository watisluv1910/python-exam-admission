class MealyError(Exception):
    pass


class Mealy:
    def __init__(self):
        self.cond = 'A'

    def leer(self):
        if self.cond == 'A':
            self.cond = 'B'
            return 0
        if self.cond == 'B':
            self.cond = 'C'
            return 1
        if self.cond == 'C':
            self.cond = 'A'
            return 4
        if self.cond == 'D':
            self.cond = 'E'
            return 5
        if self.cond == 'E':
            self.cond = 'F'
            return 7
        raise MealyError('leer')

    def chain(self):
        if self.cond == 'B':
            self.cond = 'D'
            return 2
        if self.cond == 'C':
            self.cond = 'D'
            return 3
        if self.cond == 'D':
            self.cond = 'D'
            return 6
        if self.cond == 'F':
            self.cond = 'B'
            return 8
        raise MealyError('chain')


def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as e:
        assert type(e) == error
        assert output is None


def main():
    return Mealy()


def test():
    m = Mealy()
    raises(lambda: m.chain(), MealyError)
    m.leer()
    m.leer()
    m.leer()
    m.leer()
    m.chain()
    m.chain()
    m.leer()
    raises(lambda: m.chain(), MealyError)
    m.leer()
    raises(lambda: m.leer(), MealyError)
    m.chain()
    m.leer()
    m.chain()
    m.chain()
    return main()


if __name__ == "__main__":
    print(test())
