from abc import ABC, abstractmethod


class Info(ABC):

    @abstractmethod
    def get_item(self):
        pass

    @abstractmethod
    def get_operation(self):
        pass

    @abstractmethod
    def get_result(self):
        pass

    @abstractmethod
    def get_stack(self):
        pass


class Visitor(ABC):
    @abstractmethod
    def visit(self, obj):
        pass


class Num(Info):
    def __init__(self, digit: int):
        self.digit = digit

    def get_item(self):
        return [f"PUSH {self.digit}"]

    def get_operation(self):
        return f"{self.digit}"

    def get_result(self):
        return self.digit

    def get_stack(self):
        return f"PUSH {self.digit}\n"


class Add(Info):
    def __init__(self, obj_a: Info, obj_b: Info):
        self.obj_a = obj_a
        self.obj_b = obj_b

    def get_item(self):
        return self.obj_a.get_item() + self.obj_b.get_item()

    def get_operation(self):
        return f"({self.obj_a.get_operation()} + {self.obj_b.get_operation()})"

    def get_result(self):
        return self.obj_a.get_result() + self.obj_b.get_result()

    def get_stack(self):
        return f"{self.obj_a.get_stack()}{self.obj_b.get_stack()}ADD\n"


class Sub(Info):
    def __init__(self, obj_a: Info, obj_b: Info):
        self.obj_a = obj_a
        self.obj_b = obj_b

    def get_item(self):
        return self.obj_a.get_item() + self.obj_b.get_item()

    def get_operation(self):
        return f"({self.obj_a.get_operation()} - {self.obj_b.get_operation()})"

    def get_result(self):
        return self.obj_a.get_result() - self.obj_b.get_result()

    def get_stack(self):
        return f"{self.obj_a.get_stack()}{self.obj_b.get_stack()}SUB\n"


class Mul(Info):
    def __init__(self, obj_a: Info, obj_b: Info):
        self.obj_a = obj_a
        self.obj_b = obj_b

    def get_item(self):
        return self.obj_a.get_item() + self.obj_b.get_item()

    def get_operation(self):
        return f"({self.obj_a.get_operation()} * {self.obj_b.get_operation()})"

    def get_result(self):
        return self.obj_a.get_result() * self.obj_b.get_result()

    def get_stack(self):
        return f"{self.obj_a.get_stack()}{self.obj_b.get_stack()}MUL\n"


class PrintVisitor(Visitor):
    def visit(self, obj: Info):
        return obj.get_operation()


class CalcVisitor(Visitor):
    def visit(self, obj: Info):
        return obj.get_result()


class StackVisitor(Visitor):
    def visit(self, obj: Info):
        print(obj.get_stack())


ast = Add(Num(7), Mul(Num(3), Num(2)))
pv = PrintVisitor()
cv = CalcVisitor()
sv = StackVisitor()
print(pv.visit(ast))
print(cv.visit(ast))
sv.visit(ast)
