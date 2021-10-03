from car import Car
from account import Account
from conductor import Conductor
from usuario import usuario

if __name__ == "__main__":
    print("Hola mundo");
    car = Car("AMS134", Account("Andres Gutierrez","NPI111"));
    print(vars(car));
    print(vars(car.conductor));

    car2 = Car("TPU799", Account("Manuel Estrada", "STG123"))
    print(vars(car2));
    print(vars(car2.conductor));

    car3 = Car("BVI124", Account("Emilia Restrepo", "KKK888"));
    print(vars(car));
    print(vars(car.conductor));
