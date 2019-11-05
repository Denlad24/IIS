import math


class Equation:
    def __init__(self, func=None):
        if func:
            self.execute = func

    def execute(a, b, c):
        discr = b ** 2 - 4 * a * c

        if discr > 0:
            assert discr > 0, "should be > 0"
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            return x1, x2
        elif discr == 0:
            assert discr == 0, "should be = 0"
            x = -b / (2 * a)
            return x
        else:
            return "Корней нет"


def vietta(a, b, c):
    x1 = -b
    x2 = 0
    discr = b ** 2 - 4 * a * c
    if discr < 0:
        print("Корней нет")
    else:
        while (x1 + x2 != -b or x1 * x2 != c):
            x2 = x2 + 1
            x1 = x1 - 1
        return x1, x2


if __name__ == "__main__":
    print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    print("Выберите как вы хотите решить уравнение. Методом Виета (нажмите 1) или дискриминантом (нажмите 2)")
    ch = int(input())
    assert type(ch) == int, "Should be float"
    if ch == 1:
        assert ch == 1, "should be 1"
        strat1 = Equation(vietta)
        print(strat1.execute(a, b, c))
    if ch == 2:
        assert ch == 2, "should be 1"
        strat2 = Equation()
        print(strat2.execute(a, b, c))


