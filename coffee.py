class Coffee:
    all_coffees = []
    
    def __init__(self, name):
        self._name = None
        self.name = name
        self.orders_list = []
        Coffee.all_coffees.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if len(value) < 3:
            raise Exception("Name must be at least 3 characters long")
        if self._name is not None:
            raise Exception("Coffee name cannot be changed after creation")
        self._name = value
    
    def orders(self):
        return self.orders_list
    
    def customers(self):
        return list(set(order.customer for order in self.orders_list))
    
    def num_orders(self):
        return len(self.orders_list)
    
    def average_price(self):
        if not self.orders_list:
            return 0
        return sum(order.price for order in self.orders_list) / len(self.orders_list)