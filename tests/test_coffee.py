import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee:
    def test_coffee_creation(self):
        coffee = Coffee("Espresso")
        assert coffee.name == "Espresso"
    
    def test_invalid_name_length(self):
        with pytest.raises(Exception):
            Coffee("ab")
    
    def test_name_immutability(self):
        coffee = Coffee("Latte")
        with pytest.raises(Exception):
            coffee.name = "New Name"
    
    def test_orders_relationship(self):
        customer = Customer("Alice")
        coffee = Coffee("Cappuccino")
        order = Order(customer, coffee, 6.0)
        
        assert order in coffee.orders()
        assert len(coffee.orders()) == 1
    
    def test_customers_relationship(self):
        coffee = Coffee("Espresso")
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        
        Order(customer1, coffee, 5.0)
        Order(customer2, coffee, 5.5)
        Order(customer1, coffee, 4.5)
        
        customers = coffee.customers()
        assert len(customers) == 2
        assert customer1 in customers
        assert customer2 in customers
    
    def test_num_orders(self):
        coffee = Coffee("Latte")
        customer = Customer("Charlie")
        
        assert coffee.num_orders() == 0
        
        Order(customer, coffee, 5.0)
        Order(customer, coffee, 5.5)
        
        assert coffee.num_orders() == 2
    
    def test_average_price(self):
        coffee = Coffee("Mocha")
        customer = Customer("Diana")
        
        Order(customer, coffee, 4.0)
        Order(customer, coffee, 6.0)
        
        assert coffee.average_price() == 5.0
    
    def test_average_price_no_orders(self):
        coffee = Coffee("Americano")
        assert coffee.average_price() == 0