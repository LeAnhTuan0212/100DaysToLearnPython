class MONEYMACHINE:
    
    CURRENCY = "$"
    
    COIN_VALUE = {
        "quarters": 0.25,
        "dimes": 0.1,
        "nickles": 0.05,
        "pennies": 0.01
    }
    
    def __init__(self):
        self.profit = 0
        self.money_recieved = 0
        
    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")
        
    def process_coin(self):
        """Return the total calculated froms coin inserted"""    
        print("Please insert coins.")
        for coin in self.COIN_VALUE:
            self.money_recieved += int(input(f"How many {coin}? ")) * self.COIN_VALUE[coin]
        return self.money_recieved
    
    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coin()
        if self.money_recieved >= cost:
            change = round(self.money_recieved - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_recieved = 0
            return True
        else:
            print("Sorry! Thar's not enough money. Money refunded.")
            self.money_recieved = 0
            return False
    
    