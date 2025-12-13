import beverages
import random as r

class CoffeeMachine:
    trials = 10
    def __init__(self):
        pass
    class EmptyCup(beverages.HotBeverage):
        name = "empty cup"
        price = 0.90
        def description(self):
            return "An empty cup?! Gimme my money back!"
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")
    def repair(self):
        self.trials = 10
    def serve(self, beverage_class):
        print(self.trials)
        i = r.randint(0,1)
        if not self.trials:
            raise self.BrokenMachineException()
        else:
            if i:
                self.trials -= 1
                return beverage_class()
            self.trials -= 1
            return self.EmptyCup()
        
try:
    i = CoffeeMachine()
    b = CoffeeMachine()
    i.trials -= 1
    print(b.trials)
except CoffeeMachine.BrokenMachineException as e:
    print(e)