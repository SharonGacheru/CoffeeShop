import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import all classes in the test file
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    def test_customer_creation(self):
        customer = Customer("John")
        assert customer.name == "John"
    
    def test_invalid_name_length(self):
        with pytest.raises(Exception):
            Customer("")
        with pytest.raises(Exception):
            Customer("ThisNameIsWayTooLong")
    
    def test_invalid_name_type(self):
        with pytest.raises(Exception):
            Customer(123)
    
    def test_orders_relationship(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 5.0)
        
        assert order in customer.orders()
        assert len(customer.orders()) == 1
    
    def test_coffees_relationship(self):
        customer = Customer("Bob")
        coffee1 = Coffee("Espresso")
        coffee2 = Coffee("Latte")
        
        Order(customer, coffee1, 4.0)
        Order(customer, coffee2, 5.0)
        Order(customer, coffee1, 4.5)
        
        coffees = customer.coffees()
        assert len(coffees) == 2
        assert coffee1 in coffees
        assert coffee2 in coffees
    
    def test_create_order_method(self):
        customer = Customer("Charlie")
        coffee = Coffee("Mocha")
        
        order = customer.create_order(coffee, 6.0)
        
        assert order in customer.orders()
        assert order.coffee == coffee
        assert order.price == 6.0