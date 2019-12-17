class Car():
    def __init__(self):
        self.engine = None
        self.tyres = None
        self.speedometer = None

    def __str__(self):
        return '{} | {} | {}'.format(self.engine, self.tyres, self.speedometer)


class AbstractBuilder():
    def __init__(self):
        self.car = None

    def createNewCar(self):
        self.car = Car()


class ConcreteBuilder(AbstractBuilder):

    def addEngine(self):
        self.car.engine = "4 цилиндра"

    def addTyres(self):
        self.car.tyres = "Летние"

    def addSpeedometer(self):
        self.car.speedometer = "0-160"


class ConcreteBuilder2(AbstractBuilder):

    def addEngine(self):
        self.car.engine = "5 цилиндров"

    def addTyres(self):
        self.car.tyres = "Зимние"

    def addSpeedometer(self):
        self.car.speedometer = "0-200"


class Director():
    def __init__(self, builder):
        self._builder = builder

    def constructCar(self):
        self._builder.createNewCar()
        self._builder.addEngine()
        self._builder.addTyres()
        self._builder.addSpeedometer()

    def getCar(self):
        return self._builder.car


concreteBuilder = ConcreteBuilder()
director = Director(concreteBuilder)
director.constructCar()
carOne = director.getCar()
print("Детали машины 1:", carOne)

concreteBuilder = ConcreteBuilder2()
director = Director(concreteBuilder)
director.constructCar()
carTwo = director.getCar()
print("Детали машины 2:", carTwo)
