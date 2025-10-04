from customer import Customer
from coffee import Coffee
from order import Order

def debug_demo():
    print("=== COFFEE SHOP DEBUG DEMO ===")
    
    print("\n1. Creating customers...")
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    print(f"Created: {customer1.name}, {customer2.name}")
    
    print("\n2. Creating coffees...")
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")
    cappuccino = Coffee("Cappuccino")
    print(f"Created: {espresso.name}, {latte.name}, {cappuccino.name}")
    
    print("\n3. Creating orders...")
    order1 = Order(customer1, espresso, 5.0)
    order2 = Order(customer1, latte, 6.5)
    order3 = Order(customer2, espresso, 5.0)
    order4 = Order(customer2, cappuccino, 7.0)
    print("Orders created successfully!")
    
    print("\n4. Testing relationships...")
    print(f"{customer1.name}'s orders: {len(customer1.orders())}")
    print(f"{customer1.name}'s coffees: {[coffee.name for coffee in customer1.coffees()]}")
    print(f"Espresso customers: {[customer.name for customer in espresso.customers()]}")
    print(f"Espresso number of orders: {espresso.num_orders()}")
    print(f"Espresso average price: ${espresso.average_price():.2f}")
    
    print("\n5. Testing bonus method...")
    top_espresso_customer = Customer.most_aficionado(espresso)
    print(f"Top espresso customer: {top_espresso_customer.name if top_espresso_customer else 'None'}")
    
    # error handling
    print("\n6. Testing error handling...")
    try:
        invalid_customer = Customer("ThisNameIsWayTooLongForValidation")
    except Exception as e:
        print(f"✓ Customer validation error caught: {e}")
    
    try:
        invalid_coffee = Coffee("ab")
    except Exception as e:
        print(f"✓ Coffee validation error caught: {e}")
    
    try:
        invalid_order = Order(customer1, espresso, 15.0)
    except Exception as e:
        print(f"✓ Order validation error caught: {e}")
    
    print("\n=== DEBUG COMPLETE ===")

if __name__ == "__main__":
    debug_demo()