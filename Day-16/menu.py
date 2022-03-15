class MENUITEM:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost 
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }   

class MENU:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = {
            MENUITEM(name="espresso", water=58, coffee=18, milk=0, cost=1.5),
            MENUITEM(name="latte", water=200, coffee=24, milk=150, cost=2.5),
            MENUITEM(name="cappuccino", water=250, coffee=24, milk=100, cost=3.0)
        }

    def get_item(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options+= f"{item.name}/"
        return options
    
    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry! That item is not available.")