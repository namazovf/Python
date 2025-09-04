# Masin almaga pul olmayanda kreditAl() a getsin, pul olandada kreditiOde() nen odesin

class Cars:
    def __init__(self):
        self.MyCars = [
            {"name": "BMW", "price": 20000, "year": 2018, "count": 1},
            {"name": "Toyota", "price": 15000, "year": 2020, "count": 1},
            {"name": "Honda", "price": 13000, "year": 2017, "count": 1},
        ]
        self.balance=70000

    def ListCars(self):
        for car in self.MyCars:
            print(car)
    
    def ShowBalance(self):
        print(f"Your current balance is {self.balance}")

    def SelCar(self):
        a=input("Which car u want? :")
        b=int(input("How much money u have: "))
        k=0
        for car in self.MyCars:
            if(car['name'].upper() == a.upper()):
                if(car['price'] <= b):
                    print("You boought that car, Sellen")
                    car['count']-=1
                    if car['count']==0:
                        self.MyCars.remove(car)
                    k=1
                    self.balance+=b
                    break
                elif(car['price'] -500 < b):
                    print(f"You bought that car with {car['price']-b}$ discount, sellen")
                    car['count']-=1
                    if car['count']==0:
                        self.MyCars.remove(car)
                    k=1
                    self.balance+=b
                    break
                else:
                    print("Senin masin almaga pulun var e kasif, tullan")
                    k=1
                    break
        if(k==0):
            print(f"{a} adli masin yoxumuzdu")
    def BuyCar(self):
        a=input("Which car u want to sell? :")
        b=int(input("How much money u want? : "))
        y=int(input("What is the year of your car? : "))
        k=0
        for car in self.MyCars:
            if a.upper() == car['name'].upper() :
                k=1
                if b <= car['price']-2500 :
                    if b < self.balance :
                        print(f"{a} masinini aliram.")
                        car['count']+=1
                        self.balance-=b
                        break
                    else :
                        print("Bu qiymet yaxsidi amma uzurlu say o qeder pulum yoxdu hazirda")
                        break
                  
                else:
                    print(f"Bu qiymet mene uygun deil.\n Eger {car['price']-2500} e verirsense aliram.")
                    print("Bu qiymet sene uygundu?")
                    ans = input("(he,yox): ")
                    if(ans=="he"):
                        if car['price']-2500 <= self.balance:
                            print(f"{a} masinini aliram.")
                            car['count']+=1
                            self.balance-=car['price']-2500
                            break
                    else:
                        print("Hesne onda qardas ozune yaxsi bax.")
                        break
        if k==0:
            if b <=2000 :
                if b <= self.balance:
                    print(f"{a} masinini aliram.")
                    new_car = {
                        "name": a,
                        "price": b+750,
                        "year": y,
                        "count": 1
                    }
                    self.MyCars.append(new_car)
                    self.balance-=b
                else:
                    print("Bu qiymet yaxsidi amma uzurlu say o qeder pulum yoxdu hazirda")
            
            else:
                print(f"Bu qiymet mene uygun deil.\n Eger {b-1500} e verirsense aliram.")
                print("Bu qiymet sene uygundu?")
                ans = input("(he,yox): ")
                if(ans=="he"):
                    if b-1500 <= self.balance:
                        print(f"{a} masinini aliram.")
                        new_car = {
                        "name": a,
                        "price": b+1500,
                        "year": y,
                        "count": 1
                        }
                        self.MyCars.append(new_car)
                        self.balance-=b-1500
                else:
                    print("Hesne onda qardas ozune yaxsi bax.")

            
c = Cars()

# DENEME

while True:
    print("\n=== Masin Satis Sistemi ===")
    print("1. Masin al (Sən masin alirsan)")
    print("2. Masin sat (Sən musterinin dediklerini daxil edirsen)")
    print("3. Masin siyahisini göstər")
    print("4. Balansi goster")
    print("5. Sistemdən cix")
    

    secim = input("Seciminizi daxil edin (1-5): ")

    if secim == "1":
        c.BuyCar()
        # c.ShowBalance()
    elif secim == "2":
        c.SelCar()
        # c.ShowBalance()
    elif secim == "3":
        c.ListCars()
        # c.ShowBalance()
    elif secim == "4":
        c.ShowBalance()
    elif secim == "5":
        print("Sistemden cixildi.")
        break
    else:
        print("Yanlis secim! Zəhmət olmasa 1-dən 4-ə qədər secim edin.")