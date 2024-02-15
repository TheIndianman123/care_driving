import time
import re
res = ""

class Parts:
    def __init__(self, brand, wheels, seats, lights, gears,Idnumber):
        self.brand = brand
        self.wheels = wheels
        self.seats = seats
        self.lights = lights
        self.gears = gears
        self.Idnumber=Idnumber

    def __str__(self):
        return f"[Name]=[{self.brand:>12}]\n[Number Of Wheel]=[{self.wheels}]\n[Number Of Gears]=[{self.gears}]\n[Number of lights]=[{self.lights}]\n[Number of Seats]=[{self.seats}]"


class Car(Parts):
    def __init__(self, brand, wheels, seats, lights, gears, m_a,Idnumber):
        self.m_a = m_a
        self.Sp = 0 
        self.sig="" 
        super().__init__(brand, wheels, seats, lights, gears,Idnumber)

    def go(self):
        
        print(f"Car {self.brand} is moving. It is {self.m_a}. Speed {self.Sp}")

          
        for i in range(0,4):
            time.sleep(1)
            print(">",end='')
        
        print("\n")

    def stop(self):
        self.Sp = 0  
        print(f"Car {self.brand} stopped")
    
    def reverse(self):
          print(f"Car {self.brand} reverseing")

          for i in range(0,4):
              time.sleep(1)
              print("<",end='')


    def clutch(self, option):
        if option == 1:
            print("Shifting to Gear One")

        elif option == 2:
            print("Shifting to Gear Two")
        elif option == 3:
            print("Shifting to Gear Three")
        elif option == 4:
            print("Shifting to Gear Four")
        elif option == 5:
            print("Shifting to Gear Five")
        elif option == 6:
            print("Shifting to Reverse")
            self.reverse()
        elif option == 7:
            print("Car in Neutral")
            return "Neutral"
        else:
            print("Invalid Gear Error")
            self.stop()

        return "Running"

    def speed(self):
        print("Increasing speed")
        if self.check_speed_limit():
            for i in range(0,2):

                self.Sp += 5
                time.sleep(1)
                print(f"{self.Sp} km/h")
            
            res3=self.change_gear()
            
            self.clutch(res3)


        else:
            print("Warning")
            print("Car slowing down")
            self.slow_down()

    def check_speed_limit(self):
        if self.Sp >= 50:
            return False
        else:
            return True

    def slow_down(self):
        if self.Sp == 0:
            print("The car has stopped")
        else:
            len1=self.Sp//2
            len1=len1//2
            for i in range(0,len1):

                self.Sp -= 2
                time.sleep(1)
                print(f"Speed reduced to {self.Sp} km/h")

    def change_gear(self):
      
        if self.Sp ==0:
            print("Shift to Gear One")
            return 1

        elif self.Sp ==10:
            print("Shift to Gear Two")
            return 2
        elif self.Sp == 20:
            print("Shift to Gear Three")
            return 3
        elif self.Sp ==30:
            print("Shifting to Gear Four")
            return 4
        elif self.Sp==40:
            print("Shifting to Gear Five")
            return 5
       
        else:
            print("Invalid Gear Error")
            self.stop()

        return "Running"

    def signals(self):
        self.sig=input("Enter L for left or R for Right")
        while True:
            if self.sig == "L":
                print("➔", end="")
                return "LEFT"
            elif self.sig == "R":
                print("←", end="")
                return "RIGHT"
        

           
         



    def check_id(self):
        x=re.search("^CER",self.Idnumber)
        if x:
            print("You id is valid")
        else:
            print("Your Id is wrong")


    def turn_left(self):
          
        if self.sig== "LEFT":
            print("Turning left")
        elif self.sig == "RIGHT":
            print("WRONG SIGNAL")
        else:
            print("NO signal")
            self.stop()


            
      


m2 = Car("ford", 4, 4, 4, 6, "Automatic","CER-444")

print(m2)
import time

def animate_car():
    car_position = 0
    line = ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    while True:
        print("\r" + line[:car_position] + "[ CAR ]" + line[car_position+len("[ CAR ]"):], end="")
        time.sleep(0.1)
        car_position += 1
        if car_position >= len(line) - len("[ CAR ]"):
            car_position = 0

animate_car()

            

    



while True:
    user = int(input("Enter the option\n[1][Clutch]\n[2][Start the Engine]\n[3][Speed Up]\n[4][Slow Down]\n[5][Stop]\n[6][Signal lights]\n[7][Turn Left]\n[8][Check ID]"))

    if user == 1:
        print()
        clutch1 = int(input("Enter Your clutch gear 1.Gear one\n2.Gear two\n3.Gear three\n4.Gear four\n5.Gear five\n6.Gear Reverse\n7.Neutral"))
        res = m2.clutch(clutch1)
    elif user == 2:
        if res != "Running":
            print("We cannot start the car put the clutch down first and set the gears")
        else:
            print("The car is ready to go !")
            m2.go()
    elif user == 3:
        print("Speed car Up")
        if res != "Running":
            print("We cannot make the car go faster the clutch down first ")
        else:
            print("The car is ready to go !")
            m2.speed()
    elif user == 4:
        print("Slowing the car")
        m2.slow_down()
    elif user == 5:
        m2.stop()
    elif user==6:
     
        m2.signals()

    elif user==7:
        m2.turn_left()
    elif user==8:
        m2.check_id()

    else:
        print("Invalid")
