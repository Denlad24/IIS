class Pizza():
    def __init__(self):
        self.type = None
        self.grad = None
        self.time = None

    def __str__(self):
        return '{} | температура = {} | время = {}'.format(self.type, self.grad, self.time)

    def create(self):
        pass


class Creator_Pizza():
    def __init__(self, type):
        self.type = type

    def create(self):
        if self.type == "Сырная":
            return CheesePizza()
        if self.type == "Мясная":
            return MeatPizza()


class AbstractBuilder():
    def __init__(self):
        self.pizza = None

    def createNewPizza(self):
        self.pizza = Pizza()


class CheesePizza(AbstractBuilder):

    def addType(self):
        self.pizza.type = "Сырная"

    def addGrad(self):
        self.pizza.grad = "400"

    def addTime(self):
        self.pizza.time = "12"


class MeatPizza(AbstractBuilder):

    def addType(self):
        self.pizza.type = "Мясная"

    def addGrad(self):
        self.pizza.grad = "380"

    def addTime(self):
        self.pizza.time = "15"


class Director():
    def __init__(self, builder):
        self._builder = builder

    def createpizza(self):
        self._builder.createNewPizza()
        self._builder.addType()
        self._builder.addGrad()
        self._builder.addTime()

    def getpizza(self):
        return self._builder.pizza


pizza_fabric = Creator_Pizza("Сырная")
pizza = pizza_fabric.create()
director = Director(pizza)
director.createpizza()
pizzaOne = director.getpizza()
print("Детали пиццы:", pizzaOne)

pizza_fabric = Creator_Pizza("Мясная")
pizza = pizza_fabric.create()
director = Director(pizza)
director.createpizza()
pizzaOne = director.getpizza()
print("Детали пиццы:", pizzaOne)
