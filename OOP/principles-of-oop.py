class MyStore:
    def sign_in(self, user):
        self.user = user
    
    def current_user(self):
        return self.user
    
    def item(self, item):
        self.item  = item

    def item_price(self, price):
        self.price  = price

    def shopping_cart(self):
        self.shopping_cart = list()

    def add_to_cart(self, item):
        self.shopping_cart.append(item)

    def remove_from_cart(self, item):
        self.shopping_cart.remove(item)

# ABSTRACTION
def checkout(self, discount = 0):
    total = sum([item.price for item in self.shopping_cart()])

    if discount == 10:
        total -= total * 10 / 100.00
    elif discount == 20:
        total -= total * 20 / 100.00
    elif discount == 50:
        total -= total * 50 / 100.00

    return total
# REfactor the above code.
# we will create an ATTRIBUTE TO ACCESS DATA about a coupon amount.
# Then our checkout() method can use the coupon attribute to calculate user's total.

class ShoppingCart:
    def __init__(self, coupon = 0):
        self.coupon = coupon

    def checkout(self):
        total = sum([item.price for item in self.shopping_cart()])
        total -= total* self.coupon / 100
        return total