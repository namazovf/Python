import json
import os


class Cars:
    def __init__(self):
        self.balance_file = "balance.txt"
        self.cars_file = "cars.json"
        self.credit_file = "credit.txt"
        self.MyCars = self.LoadCars()
        self.balance = self.LoadBalance()
        self.MyCredit = self.LoadCredit()

    def SaveBalance(self):
        with open(self.balance_file, "w") as f:
            f.write(str(self.balance))

    def LoadBalance(self):
        if os.path.exists(self.balance_file):
            with open(self.balance_file, "r") as f:
                return int(f.read())
        return 70000  # Əgər fayl yoxdursa, ilkin balans

    def LoadCredit(self):
        if os.path.exists(self.credit_file):
            with open(self.credit_file, "r") as f:
                return int(f.read())
        return 0

    def SaveCredit(self):
        with open(self.credit_file, "w") as f:
            f.write(str(self.MyCredit))

    def SaveCars(self):
        with open(self.cars_file, "w") as f:
            json.dump(self.MyCars, f)

    def LoadCars(self):
        if os.path.exists(self.cars_file):
            with open(self.cars_file, "r") as f:
                return json.load(f)
        return [
            {"name": "BMW", "price": 20000, "year": 2018, "count": 1},
            {"name": "Toyota", "price": 15000, "year": 2020, "count": 1},
            {"name": "Honda", "price": 13000, "year": 2017, "count": 1},
        ]

    def ListCars(self):
        for car in self.MyCars:
            print(car)

    def ShowBalance(self):
        print(f"Your current balance is {self.balance}$")

    def ShowCredit(self):
        print(f"Senin Javid Credite olan borcun {self.MyCredit}$ teskil edir")

    
    def GetCredit(self):
        print("\nJavid Credits e xos gelmisiz, size nece komek ede bilerem: ?")
        a = input("\n1.Credit almaq isteyirem\n2.Creditimi odemek isteyirem\n")

        if a == "1":
            amount = int(input("Ne qeder credit almaq isteyirsiz? : "))
            self.balance += amount
            self.SaveBalance()
            self.MyCredit += amount
            self.SaveCredit()
            print("\nCreditiniz balansiniza yatdi, bizi secdiyiniz ucun tesekkurler :)")
            print(f"\nIndi sizin balansiniz {self.balance}$ dir.")
        elif a=="2":
            if self.MyCredit ==0:
                print("\nSizin bize borcunuz yoxdur.")
            else:
                print(f"\nSizin borcunuz {self.MyCredit}$ teskil edir.")
                ode = int(input("Siz ne qeder odemek isteyirsiz? : "))
                if ode > self.balance:
                    print("\nSizin bu qeder pulunuz yoxdu, pulunuz olanda  odeyersiz.")
                elif ode > self.MyCredit:
                    self.balance -=self.MyCredit
                    self.SaveBalance()
                    self.MyCredit = 0
                    self.SaveCredit()
                    print(f"\nBu mebleg borcunuzdan daha coxdu, {self.MyCredit}$ borcunuz silindi bu ise sizin elave verdiyiniz {ode-self.MyCredit}$")
                elif ode > 0 :
                    self.balance-=ode
                    self.SaveBalance()
                    self.MyCredit-=ode
                    self.SaveCredit()
                    print(f"\n{ode}$ kredit borcunuz odendi, sizin qaliq kredit borcunuz {self.MyCredit}$ dir.")     
                else:
                    print("\nSiz o boyda Javid Credits ile mezelenirsiz deyesen, normal pul verin borcunuzu silin yoxsa birde size credit verilmeyecek!!!")        
                        
                    
                    
                    
    def SelCar(self):
        a = input("Which car u want? :")
        b = int(input("How much money u have: "))
        k = 0
        for car in self.MyCars:
            if car["name"].upper() == a.upper():
                if car["price"] <= b:
                    print("You bought that car, Sellen")
                    car["count"] -= 1
                    if car["count"] == 0:
                        self.MyCars.remove(car)
                    k = 1
                    self.balance += b
                    break
                elif car["price"] - 500 <= b:
                    print(
                        f"You bought that car with {car['price'] - b}$ discount, sellen"
                    )
                    car["count"] -= 1
                    if car["count"] == 0:
                        self.MyCars.remove(car)
                    k = 1
                    self.balance += b
                    break
                else:
                    print("Senin masin almaga pulun var e kasif, tullan")
                    k = 1
                    break
        if k == 0:
            print(f"{a} adli masin yoxumuzdu")

        self.SaveBalance()
        self.SaveCars()

    def BuyCar(self):
        a = input("Which car u want to sell? :")
        b = int(input("How much money u want? : "))
        y = int(input("What is the year of your car? : "))
        k = 0
        for car in self.MyCars:
            if a.upper() == car["name"].upper():
                k = 1
                if b <= car["price"] - 2500:
                    if b < self.balance:
                        print(f"{a} masinini aliram.")
                        car["count"] += 1
                        self.balance -= b
                        break
                    else:
                        ans = input(
                            "I dont have enough money , do I want to get credit? (yes/no)"
                        )
                        if ans == "yes":
                            self.GetCredit()
                            if b <= self.balance:
                                print(f"{a} masinini aliram.")
                                car["count"] += 1
                                self.balance -= b
                                break
                            else:
                                print("Uzurlu  say pulum catmir.")
                        else:
                            print("Sorry qaqa alasi olmadim")
                        break
                else:
                    print(
                        f"Bu qiymet mene uygun deil.\nEger {car['price'] - 2500} e verirsense aliram."
                    )
                    ans = input("Bu qiymet sene uygundu? (he,yox): ")
                    if ans == "he":
                        if car["price"] - 2500 <= self.balance:
                            print(f"{a} masinini aliram.")
                            car["count"] += 1
                            self.balance -= car["price"] - 2500
                            break
                        else:
                            ans = input(
                            "I dont have enough money , do I want to get credit? (yes/no)"
                            )
                            if ans == "yes":
                                self.GetCredit()
                                if car["price"] - 2500 <= self.balance:
                                    print(f"{a} masinini aliram.")
                                    car["count"] += 1
                                    self.balance -= b
                                    break
                                else:
                                    print("Uzurlu  say pulum catmir.")
                            else:
                                print("Sorry qaqa alasi olmadim")
                            break
                    else:
                        print("Hesne onda qardas ozune yaxsi bax.")
                        break
        if k == 0:
            if b <= 2000:
                if b <= self.balance:
                    print(f"{a} masinini aliram.")
                    new_car = {"name": a, "price": b + 750, "year": y, "count": 1}
                    self.MyCars.append(new_car)
                    self.balance -= b
                else:
                    ans = input(
                            "I dont have enough money , do I want to get credit? (yes/no)"
                            )
                    if ans == "yes":
                        self.GetCredit()
                        if b <= self.balance:
                            print(f"{a} masinini aliram.")
                            new_car = {"name": a, "price": b + 750, "year": y, "count": 1}
                            self.MyCars.append(new_car)
                            self.balance -= b
                        else:
                            print("Uzurlu  say pulum catmir.")
                    else:
                        print("Sorry qaqa , alasi olmadim")
            else:
                print(
                    f"Bu qiymet mene uygun deil.\nEger {b - 1500} e verirsense aliram."
                )
                ans = input("Bu qiymet sene uygundu? (he,yox): ")
                if ans == "he":
                    if b - 1500 <= self.balance:
                        print(f"{a} masinini aliram.")
                        new_car = {"name": a, "price": b + 1500, "year": y, "count": 1}
                        self.MyCars.append(new_car)
                        self.balance -= b - 1500
                    else:    
                        ans = input(
                            "I dont have enough money , do I want to get credit? (yes/no)"
                            )
                        if ans == "yes":
                            self.GetCredit()
                            if b - 1500 <= self.balance:
                                print(f"{a} masinini aliram.")
                                new_car = {"name": a, "price": b + 1500, "year": y, "count": 1}
                                self.MyCars.append(new_car)
                                self.balance -= b - 1500
                            else:
                                print("Uzurlu  say pulum catmir.")
                        else:
                            print("Sorry qaqa , alasi olmadim")        
                else:
                    print("Hesne onda qardas ozune yaxsi bax.")

        self.SaveBalance()
        self.SaveCars()


# DENEME
c = Cars()

while True:
    print("\n=== Masin Satis Sistemi ===")
    print("1. Masin al (Sən masin alirsan)")
    print("2. Masin sat (Sən musterinin dediklerini daxil edirsen)")
    print("3. Masin siyahisini göstər")
    print("4. Balansi goster")
    print("5. Javid credite muraciet et")
    print("6. Javid credite olan borcumuza bax")
    print("7. Sistemdən cix")

    secim = input("Seciminizi daxil edin (1-6): ")

    if secim == "1":
        c.BuyCar()
    elif secim == "2":
        c.SelCar()
    elif secim == "3":
        c.ListCars()
    elif secim == "4":
        c.ShowBalance()
    elif secim == "5":
        c.GetCredit()
    elif secim == "6":
        c.ShowCredit()
    elif secim == "7":
        print("Sistemden cixildi.")
        break
    else:
        print("Yanlis secim! Zəhmət olmasa 1-dən 5-ə qədər secim edin.")
