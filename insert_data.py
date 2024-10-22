from app import app, db, Product, Supplier, Order
import datetime

with app.app_context():
    # Insert Products
    products = [
        Product(name='Laptop', sku='SKU001', price=799.99, quantity=50),
        Product(name='Smartphone', sku='SKU002', price=499.99, quantity=100),
        Product(name='Headphones', sku='SKU003', price=199.99, quantity=200),
        Product(name='Tablet', sku='SKU004', price=299.99, quantity=75),
        Product(name='Monitor', sku='SKU005', price=249.99, quantity=30),
        Product(name='Keyboard', sku='SKU006', price=49.99, quantity=150),
        Product(name='Mouse', sku='SKU007', price=29.99, quantity=180),
        Product(name='Charger', sku='SKU008', price=19.99, quantity=300),
        Product(name='Power Bank', sku='SKU009', price=39.99, quantity=100),
        Product(name='Webcam', sku='SKU010', price=99.99, quantity=85),
        Product(name='Smartwatch', sku='SKU011', price=199.99, quantity=50),
        Product(name='Gaming Console', sku='SKU012', price=299.99, quantity=40),
        Product(name='TV', sku='SKU013', price=999.99, quantity=20),
        Product(name='Bluetooth Speaker', sku='SKU014', price=149.99, quantity=90),
        Product(name='Smart Home Hub', sku='SKU015', price=129.99, quantity=70),
        Product(name='Drone', sku='SKU016', price=499.99, quantity=10),
        Product(name='Fitness Tracker', sku='SKU017', price=99.99, quantity=120),
        Product(name='Digital Camera', sku='SKU018', price=499.99, quantity=25),
        Product(name='Projector', sku='SKU019', price=349.99, quantity=35),
        Product(name='VR Headset', sku='SKU020', price=299.99, quantity=60),
        Product(name='Smart Light Bulb', sku='SKU021', price=29.99, quantity=200),
        Product(name='Electric Scooter', sku='SKU022', price=499.99, quantity=15),
        Product(name='E-book Reader', sku='SKU023', price=129.99, quantity=50),
        Product(name='Wireless Charger', sku='SKU024', price=49.99, quantity=100),
        Product(name='Air Purifier', sku='SKU025', price=199.99, quantity=30),
        Product(name='Security Camera', sku='SKU026', price=149.99, quantity=40),
        Product(name='Action Camera', sku='SKU027', price=199.99, quantity=35),
        Product(name='Noise Cancelling Earbuds', sku='SKU028', price=199.99, quantity=150),
        Product(name='Streaming Stick', sku='SKU029', price=49.99, quantity=80),
        Product(name='Portable SSD', sku='SKU030', price=99.99, quantity=200)
    ]
    
    db.session.add_all(products)
    
    # Insert Suppliers
    suppliers = [
        Supplier(name='Tech Supplier Co.', contact='John Doe', email='john@techsupplier.com'),
        Supplier(name='Gadgets Supplier Inc.', contact='Jane Doe', email='jane@gadgetssupplier.com'),
        Supplier(name='Electronic World', contact='Mark Smith', email='mark@electronicworld.com'),
        Supplier(name='Gadget Hub', contact='Alice Johnson', email='alice@gadgethub.com'),
        Supplier(name='Digital Distributors', contact='Tom Brown', email='tom@digitaldistributors.com'),
        Supplier(name='Device Supply Ltd.', contact='Nancy White', email='nancy@devicesupply.com'),
        Supplier(name='Tech Parts & More', contact='Steve Green', email='steve@techparts.com'),
        Supplier(name='PC Essentials', contact='Karen Blue', email='karen@pcessentials.com'),
        Supplier(name='Peripheral Supplies', contact='Emily Black', email='emily@peripheralsupplies.com'),
        Supplier(name='Component Warehouse', contact='James Gray', email='james@componentwarehouse.com'),
        Supplier(name='Electronics Direct', contact='Michael Lee', email='michael@electronicsdirect.com'),
        Supplier(name='Global Tech Supplies', contact='Laura Davis', email='laura@globaltech.com'),
        Supplier(name='Smart Devices Co.', contact='David Wilson', email='david@smartdevices.com'),
        Supplier(name='Gizmo Depot', contact='Sarah Brown', email='sarah@gizmodepot.com'),
        Supplier(name='FutureTech Ltd.', contact='Chris Adams', email='chris@futuretech.com'),
        Supplier(name='Innovative Solutions', contact='Karen Scott', email='karen@innovativesolutions.com'),
        Supplier(name='Smart Gear Supply', contact='Andrew Hall', email='andrew@smartgear.com'),
        Supplier(name='Hardware Hub', contact='Lisa White', email='lisa@hardwarehub.com'),
        Supplier(name='Electronics Outlet', contact='Charles King', email='charles@electronicsoutlet.com'),
        Supplier(name='SmartTech Supplies', contact='Jessica Taylor', email='jessica@smarttech.com'),
        Supplier(name='Gadget Mart', contact='Robert Harris', email='robert@gadgetmart.com'),
        Supplier(name='Tech Products Ltd.', contact='Kevin Lewis', email='kevin@techproducts.com'),
        Supplier(name='Component Supply Co.', contact='Natalie Baker', email='natalie@componentsupply.com'),
        Supplier(name='Modern Gadgets', contact='Brandon Thomas', email='brandon@moderngadgets.com'),
        Supplier(name='SmartTech Distribution', contact='Susan Evans', email='susan@smarttechdistribution.com'),
        Supplier(name='Electronics Universe', contact='Jeffrey Martin', email='jeffrey@electronicsuniverse.com'),
        Supplier(name='Tech Accessories Co.', contact='Henry Clark', email='henry@techaccessories.com'),
        Supplier(name='Advanced Devices', contact='Patricia Lewis', email='patricia@advanceddevices.com'),
        Supplier(name='Smart Solutions Ltd.', contact='Daniel Walker', email='daniel@smartsolutions.com'),
        Supplier(name='Tech Distribution Inc.', contact='Rebecca Robinson', email='rebecca@techdistribution.com')
    ]
    
    db.session.add_all(suppliers)

    # Insert Orders
    orders = [
        Order(product_id=1, quantity=5, supplier_id=1, date=datetime.datetime(2024, 10, 1)),
        Order(product_id=2, quantity=8, supplier_id=2, date=datetime.datetime(2024, 10, 2)),
        Order(product_id=3, quantity=10, supplier_id=3, date=datetime.datetime(2024, 10, 3)),
        Order(product_id=4, quantity=4, supplier_id=4, date=datetime.datetime(2024, 10, 4)),
        Order(product_id=5, quantity=3, supplier_id=5, date=datetime.datetime(2024, 10, 5)),
        Order(product_id=6, quantity=7, supplier_id=6, date=datetime.datetime(2024, 10, 6)),
        Order(product_id=7, quantity=12, supplier_id=7, date=datetime.datetime(2024, 10, 7)),
        Order(product_id=8, quantity=20, supplier_id=8, date=datetime.datetime(2024, 10, 8)),
        Order(product_id=9, quantity=15, supplier_id=9, date=datetime.datetime(2024, 10, 9)),
        Order(product_id=10, quantity=6, supplier_id=10, date=datetime.datetime(2024, 10, 10)),
        Order(product_id=11, quantity=10, supplier_id=1, date=datetime.datetime(2024, 10, 11)),
        Order(product_id=12, quantity=5, supplier_id=2, date=datetime.datetime(2024, 10, 12)),
        Order(product_id=13, quantity=8, supplier_id=3, date=datetime.datetime(2024, 10, 13)),
        Order(product_id=14, quantity=9, supplier_id=4, date=datetime.datetime(2024, 10, 14)),
        Order(product_id=15, quantity=6, supplier_id=5, date=datetime.datetime(2024, 10, 15)),
        Order(product_id=16, quantity=4, supplier_id=6, date=datetime.datetime(2024, 10, 16)),
        Order(product_id=17, quantity=7, supplier_id=7, date=datetime.datetime(2024, 10, 17)),
        Order(product_id=18, quantity=10, supplier_id=8, date=datetime.datetime(2024, 10, 18)),
        Order(product_id=19, quantity=12, supplier_id=9, date=datetime.datetime(2024, 10, 19)),
        Order(product_id=20, quantity=6, supplier_id=10, date=datetime.datetime(2024, 10, 20)),
        Order(product_id=21, quantity=10, supplier_id=1, date=datetime.datetime(2024, 10, 21)),
        Order(product_id=22, quantity=5, supplier_id=2, date=datetime.datetime(2024, 10, 22)),
        Order(product_id=23, quantity=8, supplier_id=3, date=datetime.datetime(2024, 10, 23)),
        Order(product_id=24, quantity=9, supplier_id=4, date=datetime.datetime(2024, 10, 24)),
        Order(product_id=25, quantity=6, supplier_id=5, date=datetime.datetime(2024, 10, 25)),
        Order(product_id=26, quantity=4, supplier_id=6, date=datetime.datetime(2024, 10, 26)),
        Order(product_id=27, quantity=7, supplier_id=7, date=datetime.datetime(2024, 10, 27)),
        Order(product_id=28, quantity=10, supplier_id=8, date=datetime.datetime(2024, 10, 28)),
        Order(product_id=29, quantity=12, supplier_id=9, date=datetime.datetime(2024, 10, 29)),
        Order(product_id=30, quantity=6, supplier_id=10, date=datetime.datetime(2024, 10, 30))
    ]
    
    db.session.add_all(orders)

    # Commit all changes to the database
    db.session.commit()

print("Data successfully inserted!")
