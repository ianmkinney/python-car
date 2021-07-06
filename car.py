class car:
    def __init__(self,company,car,mpg,gasTank):
        self.company = company
        self.car = car
        self.mpg = mpg
        self.gasTank = gasTank
        self.milesDriven = 0
        self.fill = 0
        
    def takeTrip(self,miles):
        if(miles > (self.fill * self.mpg)):
            print("Too far to drive with current gas, please fill up!")
        else:
            self.milesDriven = self.milesDriven + miles
            self.fill = self.fill - (int(miles/mpg))
            print(f"Successfully drove {miles} miles. You have {self.milesDriven} on your car.")
        
    def fillUp(self, amount):
        if(amount > (self.gasTank - self.fill)):
            print("That is too much gas! You overflowed!!")
        else: 
            self.fill = self.fill + amount
            print(f"You now have {self.fill} gallons in your tank! You can travel up to {self.mpg * self.fill} miles!")
        
    def display(self):
        print(f"Your {self.company} {self.car} gets {self.mpg} mpg. It can hold up to {self.gasTank} gallons! You have currently driven {self.milesDriven} miles.")
        if(self.fill == 0):
            print("You are on empty! Time to fill up!")
        else:
            print(f"You have {self.fill} gallons in the tank. You can travel a maximum of {self.fill * self.mpg} miles")


company = input("What is the company that made your car?")
carModel = input("What is your car model?")
mpg = int(input("How many miles per gallon does your car get?"))
gasTank = int(input("How many gallons can your tank hold?"))

carObj = car(company,carModel,mpg,gasTank)

carObj.display()

cont = 0 
while(cont == 0):
    print("What would you like to do?")
    print("1: Check car")
    print("2: Take Trip")
    print("3: Fill up")
    print("4: Stop program")
    userInput = int(input("Please enter the number of your option:"))
    if(userInput == 1): 
        carObj.display()
    if(userInput == 2):
        print(f"You can travel up to {carObj.mpg * carObj.fill} miles.")
        distance = int(input("How far would you like to go? (in miles): "))
        carObj.takeTrip(distance)
    if(userInput == 3):
        amount = int(input("How many gallons would you like to add to the tank?: "))
        carObj.fillUp(amount)
    if(userInput == 4):
        print("Ok, have a nice day!")
        cont = 1