class HotBeverage:
    price = 0.30
    name = "hot beverage"
    def description(self):
        return "Just some hot water in a cup."
    def __str__(self):
        return f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description()}"

class Coffee(HotBeverage):
    price = 0.40
    name = "coffee" 
    def description(self):
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    name = "tea"

class Chocolate(HotBeverage):
    name = "chocolate"
    price = 0.50
    def description(self):
        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    name = "cappuccino"
    price = 0.45
    def description(self):
        return "“Un po’ di Italia nella sua tazza!"

class1 = HotBeverage()

inst1 = Coffee()
inst2 = Tea()
inst3 = Chocolate()
inst4 = Cappuccino()


print("---- HotBeverage ----")
print(class1)
print("\n---- Coffee ----")
print(inst1)
print("\n---- Tea ----")
print(inst2)
print("\n---- Chocolate ----")
print(inst3)
print("\n---- Cappuccino ----")
print(inst4)
