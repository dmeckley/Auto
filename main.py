# Dustin Meckley
# main.py
# Base Class --> Auto
# Derived Classes --> Car, Truck, SUV

import Automobile


def main():

    # Creation of Auto object instance using constructor w/params:
    print()
    auto = Automobile.Auto(2005, 'Dodge', 'Dakota', 'V6', 'AT', '4WD')
    autoRepr = repr(auto)
    autoStr = str(auto)
    print('auto -->', auto)
    print('repr(auto) -->', autoRepr)
    print('str(auto) -->', autoStr)

    # Creation of Auto object instance using default constructor w/o params:
    print()
    newAuto = Automobile.Auto()
    newAutoRepr = repr(newAuto)
    newAutoStr = str(newAuto)
    print('newAuto -->', newAuto)
    print('repr(newAuto) -->', newAutoRepr)
    print('str(newAuto) -->', newAutoStr)

    # Building an Auto object instance from previous use of default constructor:
    print()
    newAuto.setYear(2019)
    newAuto.setMake("Toyota")
    newAuto.setModel("Camry")
    newAuto.setEngine("Inline 4")
    newAuto.setTransmission("AT")
    newAuto.setDriveTrain("2WD")
    newAutoRepr = repr(newAuto)
    newAutoStr = str(newAuto)
    print('newAuto -->', newAuto)
    print('repr(newAuto) -->', newAutoRepr)
    print('str(newAuto) -->', newAutoStr)

    # Creation of a derived Car object instance inheriting from the Auto base class: 
    print()
    car = Automobile.Car()
    car.setYear(1969)
    car.setMake("Chevy")
    car.setModel("Chevelle")
    car.setEngine("V8")
    car.setTransmission("AT")
    car.setDriveTrain("2WD")
    car.setDoor(2)
    carRepr = repr(car)
    carStr = str(car)
    print('car -->', car)
    print('repr(car) -->', carRepr)
    print('str(car) -->', carStr)

    print()
    truck = Automobile.Truck()
    truck.setYear(1957)
    truck.setMake("Chevy")
    truck.setModel("Cameo")
    truck.setEngine("5.7")
    truck.setTransmission("AT")
    truck.setDriveTrain("2WD")
    truck.setBed("Long")
    truck.setCab("Standard")
    truckRepr = repr(truck)
    truckStr = str(truck)
    print('truck -->', truck)
    print('repr(truck) -->', truckRepr)
    print('str(truck) -->', truckStr)

    print()
    suv = Automobile.SUV(2001, "Cadillac", "Escalade", "V8", "AT", "2WD", 8)
    suvRepr = repr(suv)
    suvStr = str(suv)
    print('suv -->', suv)
    print('repr(suv) -->', suvRepr)
    print('str(suv) -->', suvStr)


if __name__ == "__main__":
    main()