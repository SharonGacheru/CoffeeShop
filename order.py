class Order:
    all_orders = []
    
    def __init__(self, customer, coffee, price):
        self._price = None
        self.price = price
        self._customer = customer
        self._coffee = coffee
        
        self.customer.orders_list.append(self)
        self.coffee.orders_list.append(self)
        
        Order.all_orders.append(self)
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise Exception("Price must be a number")
        if not 1.0 <= value <= 10.0:
            raise Exception("Price must be between 1.0 and 10.0")
        if self._price is not None:
            raise Exception("Order price cannot be changed after creation")
        self._price = float(value)
    
    @property
    def customer(self):
        return self._customer
    
    @property
    def coffee(self):
        return self._coffee