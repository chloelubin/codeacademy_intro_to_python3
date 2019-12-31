# create parent class Menu
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    # define a string representation to inspect the object
    def __repr__(self):
        return '{name} menu available from {start_time} to {end_time}'.format(name=self.name,
                                                                              start_time=self.start_time,
                                                                              end_time=self.end_time)

    # define a function to calculate the bill based on menu items purchased
    def calculate_bill(self, purchased_items):
        price_sum = 0
        for item in purchased_items:
            if item in self.items:
                value_get = self.items.get(item)
                price_sum += value_get
        return price_sum


# create sub-class Brunch that inherits from Menu
class Brunch(Menu):
    def __init__(self, name, items, start_time, end_time):
        super().__init__(name, items, start_time, end_time)


brunch = Brunch('brunch', {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50,
                           'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 11, 16)

print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))


# create sub-class Early_Bird that inherits from Menu
class Early_Bird(Menu):
    def __init__(self, name, items, start_time, end_time):
        super().__init__(name, items, start_time, end_time)


early_bird = Early_Bird('early_bird', {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
                                       'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50,
                                       'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, 15, 18)

print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))


# create sub-class Dinner that inherits from Menu
class Dinner(Menu):
    def __init__(self, name, items, start_time, end_time):
        super().__init__(name, items, start_time, end_time)


dinner = Dinner('dinner',
                {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00,
                 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 17, 23)


# create sub-class Kids that inherits from Menu
class Kids(Menu):
    def __init__(self, name, items, start_time, end_time):
        super().__init__(name, items, start_time, end_time)


kids = Kids('kids', {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 11, 21)

"""
create sub-class Arepa that inherits from Menu (this child class is a little different: 
Arepa is one of the franchises but has a menu that's unique, which is why we are giving it a class of its own)
"""


class Arepa(Menu):
    def __init__(self, name, items, start_time, end_time):
        super().__init__(name, items, start_time, end_time)


arepas_menu = Arepa('Take a’ Arepa', {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 10, 20)

menus = [brunch, early_bird, dinner, kids]


# create sub-class Franchise that inherits from Menu
class Franchise(Menu):
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    # define a string representation to inspect the object
    def __repr__(self):
        print('The address of the Franchise is {address}'.format(address=self.address))

    # define a function to return a list of menu items available at a given time, which the user specifies when
    # calling the function
    def available_menus(self, time):
        available_menu_list = []
        for menu in self.menus:
            if menu.start_time <= time <= menu.end_time:
                available_menu_list.append(menu)
            return available_menu_list


flagship_store = Franchise('1232 West End Road', menus)

new_installment = Franchise('12 East Mulberry Street', menus)

arepas_place = Franchise('189 Fitzgerald Avenue', arepas_menu)

# prints available items at 5 p.m. at our flagship_store franchise
print(flagship_store.available_menus(17))


# create sub-class Business that inherits from Franchise
class Business(Franchise):
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


# assign "Basta Fazoolin' with my Heart" as the business name for our flagship_store & new_installment franchises
business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# assign "Take a' Arepa" as the business name for our arepas_place franchise
business2 = Business("Take a' Arepa", arepas_place)
