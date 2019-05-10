# Dustin Meckley
# automobile.py
# Base Class --> Auto
# Derived Classes --> Car, Truck, SUV

# BASE CLASS:
class Automobile:

    # Constructor Method:
    def __init__(self, year=None, make=None, model=None, engine=None, transmission=None, drivetrain=None):
        # Default and Overloaded Constructor Method:

        # Set Automobile Class Data Attributes:
        self.__year = year
        self.__make = make
        self.__model = model
        self.__engine = engine
        self.__transmission = transmission
        self.__drivetrain = drivetrain

    # Mutator Methods:
    def setYear(self, year):
        self.__year = year

    def setMake(self, make):
        self.__make = make

    def setModel(self, model):
        self.__model = model

    def setEngine(self, engine):
        self.__engine = engine

    def setTransmission(self, transmission):
        self.__transmission = transmission

    def setDriveTrain(self, drivetrain):
        self.__drivetrain = drivetrain

    # Accessor Methods:
    def getYear(self):
        return(self.__year)
    
    def getMake(self):
        return(self.__make)

    def getModel(self):
        return(self.__model)

    def getEngine(self):
        return(self.__engine)

    def getTransmission(self):
        return(self.__transmission)

    def getDriveTrain(self):
        return(self.__drivetrain)

    # Object Representation Method:
    def __repr__(self):
        return("{!r} {!r} {!r} {!r} {!r} {!r}".format(self.getYear(), self.getMake(), self.getModel(), self.getEngine(), self.getTransmission(), self.getDriveTrain()))

    # Object String Method:
    def __str__(self):
        return("{0} {1} {2} {3} {4} {5}".format(str(self.getYear()), self.getMake(), self.getModel(), self.getEngine(), self.getTransmission(), self.getDriveTrain()))


# DERIVED CLASS:
class Car(Automobile):

    # Constructor Method:
    def __init__(self, year=None, make=None, model=None, engine=None, transmission=None, drivetrain=None, door=None):
        # Default and Overloaded Constructor Method:

        # Call Base Class Method (Inheritance):
        super().__init__(year, make, model, engine, transmission, drivetrain)

        # Set Car Class Data Attributes:
        self.__door = door

    # Mutator Methods:
    def setDoor(self, door):
        self.__door = door

    # Accessor Methods:
    def getDoor(self):
        return(self.__door)

    # Object Representation Method:
    def __repr__(self):
        return(super().__repr__() + " {!r}dr".format(self.getDoor()))

    # Object String Method:
    def __str__(self):
        return(super().__str__() + " {0}dr".format(str(self.getDoor())))


# DERIVED CLASS:
class Truck(Automobile):

    # Constructor Method:
    def __init__(self, year=None, make=None, model=None, engine=None, transmission=None, drivetrain=None, bed=None):
        # Default and Overloaded Constructor Method:

        # Call Base Class Method (Inheritance):
        super().__init__(year, make, model, engine, transmission, drivetrain)

        # Set Truck Class Data Attributes:
        self.__bed = bed

    # Mutator Methods:
    def setBed(self, bed):
        self.__bed = bed

    # Accessor Methods:
    def getBed(self):
        return(self.__bed)

    # Object Representation Method:
    def __repr__(self):
        return(super().__repr__() + " {!r}bed".format(self.getBed()))

    # Object String Method:
    def __str__(self):
        return(super().__str__ () + " {0}bed".format(self.getBed()))


# DERIVED CLASS:
class SUV(Automobile):

    # Constructor Method:
    def __init__(self, year=None, make=None, model=None, engine=None, transmission=None, drivetrain=None, passenger=None):
        # Default and Overloaded Constructor Method:

        # Call Base Class Method (Inheritance):
        super().__init__(year, make, model, engine, transmission, drivetrain)

        # Set SUV Class Data Attributes:
        self.__passenger = passenger

    # Mutator Methods:
    def setPassenger(self, passenger):
        self.__passenger = passenger

    # Accessor Methods:
    def getPassenger(self):
        return(self.__passenger)

    # Object Representation Method:
    def __repr__(self):
        return(super().__repr__() + " {!r}pass".format(self.getPassenger()))

    # Object String Method:
    def __str__(self):
        return(super().__str__() + " {0}pass".format(str(self.getPassenger())))