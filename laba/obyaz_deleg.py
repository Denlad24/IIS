import abc
from enum import IntEnum
from flask import Flask, render_template, request


class Car:
    def __init__(self):
        self.name = None
        self.km = None
        self.fuel = None
        self.oil = None


class TO2Mech():
    def handle_request(self):
        return (str(self) + " Второй механик выполнил его задачу.")


class MechEnum(IntEnum):
    Oil = 1
    Fuel = 2
    TO = 3


class Rabot(metaclass=abc.ABCMeta):
    def __init__(self):
        self.next_handler = None

    @abc.abstractmethod
    def handle_request(self, km, fuel, oil, rez):
        pass

    def set_next_handler(self, handler):
        self.next_handler = handler


class OilMech(Rabot):
    def handle_request(self, km, fuel, oil, rez):
        if oil < 2:
            rez.append("Масло залито механиком механиком по заливу масла")
        if self.next_handler is not None:
            rez.append(self.next_handler.handle_request(km, fuel, oil, rez))
        return rez


class FuelMech(Rabot):
    def handle_request(self, km, fuel, oil, rez):
        if fuel < 10:
            rez.append("Топливо залито механиком по заливу топлива")
        if self.next_handler is not None:
            return rez.append(self.next_handler.handle_request(km, fuel, oil, rez))


class TOMech(Rabot):
    def handle_request(self, km, fuel, oil, rez):
        if km > 10000:
            rez.append(TO2Mech.handle_request("Первый механик делегировал свои обязанности второму."))
        if self.next_handler is not None:
            self.next_handler.handle_request(km, fuel, oil, rez)
        else:
            return rez


def set_up_chain():
    Mech_oil_handler = OilMech()
    Mech_fuel_handler = FuelMech()
    Star_mech_handler = TOMech()

    Mech_oil_handler.set_next_handler(Mech_fuel_handler)
    Mech_fuel_handler.set_next_handler(Star_mech_handler)

    return Mech_oil_handler


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        km = int(request.form['km'])
        fuel = int(request.form['fuel'])
        oil = int(request.form['oil'])
        chain = set_up_chain()
        r = chain.handle_request(km, fuel, oil, rez=[])
        r_len = len(r) - 2
        flag = 0
        print(r_len)
        if r_len != 0:
            flag = 1
    return render_template('result.html', prediction=r[:r_len], work=flag)


if __name__ == '__main__':
    app.run(debug=True)
