import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder:
    def test_order_creation(self):
        customer = Customer("Eve")
        coffee = Coffee("Americano")
        order = Order(customer, coffee, 3.5)
        
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 3.5
    
    def test_invalid_price_range(self):
        customer = Customer("Frank")
        coffee = Coffee("Macchiato")
        
        with pytest.raises(Exception):
            Order(customer, coffee, 0.5)
        with pytest.raises(Exception):
            Order(customer, coffee, 15.0)
    
    def test_price_immutability(self):
        customer = Customer("Grace")
        coffee = Coffee("Flat White")
        order = Order(customer, coffee, 4.0)
        
        with pytest.raises(Exception):
            order.price = 5.0
    
    def test_price_type_validation(self):
        customer = Customer("Henry")
        coffee = Coffee("Cortado")
        
        with pytest.raises(Exception):
            Order(customer, coffee, "invalid")
    
    def test_order_relationships(self):
        customer = Customer("Ivy")
        coffee = Coffee("Irish Coffee")
        order = Order(customer, coffee, 8.0)
        
        assert order in customer.orders()

        assert order in coffee.orders()