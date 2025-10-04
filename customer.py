class Customer:
    all_customers = []
    
    def __init__(self, name):
        self._name = None
        self.name = name
        self.orders_list = []
        Customer.all_customers.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise Exception("Name must be between 1 and 15 characters")
        self._name = value
    
    def orders(self):
        return self.orders_list
    
    def coffees(self):
        return list(set(order.coffee for order in self.orders_list))
    
    def create_order(self, coffee, price):
        from order import Order
        
        if coffee.__class__.__name__ != 'Coffee':
            raise Exception("Coffee must be a Coffee instance")
        if not isinstance(price, (int, float)) or not 1.0 <= price <= 10.0:
            raise Exception("Price must be a float between 1.0 and 10.0")
        
        order = Order(self, coffee, price)
        self.orders_list.append(order)
        return order
    
    @classmethod
    def most_aficionado(cls, coffee):
        if coffee.__class__.__name__ != 'Coffee':
            raise Exception("Must provide a Coffee instance")
        
        max_spent = 0
        top_customer = None
        
        for customer in cls.all_customers:
            customer_spent = sum(
                order.price for order in customer.orders() 
                if order.coffee == coffee
            )
            if customer_spent > max_spent:
                max_spent = customer_spent
                top_customer = customer
        
        return top_customer