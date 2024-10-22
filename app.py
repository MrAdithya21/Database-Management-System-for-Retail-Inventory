from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///retail_inventory.db'
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sku = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Define the Supplier model
class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=False)

# Home route
@app.route('/')
def home():
    # Query all products in the inventory
    products = Product.query.all()
    
    # Render the home.html template, passing the products to it
    return render_template('home.html', products=products)

# Route to manage products
@app.route('/products', methods=['GET', 'POST'])
def manage_products():
    if request.method == 'POST':
        name = request.form['name']
        sku = request.form['sku']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])
        new_product = Product(name=name, sku=sku, price=price, quantity=quantity)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('manage_products'))
    
    products = Product.query.all()
    return render_template('products.html', products=products)

# Route to manage orders
@app.route('/orders', methods=['GET', 'POST'])
def manage_orders():
    if request.method == 'POST':
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        supplier_id = request.form['supplier_id']
        
        # Create new order
        new_order = Order(product_id=product_id, quantity=quantity, supplier_id=supplier_id, date=datetime.now())
        db.session.add(new_order)
        db.session.commit()
    
    # Query orders with joined product and supplier data
    orders = db.session.query(Order, Product, Supplier).join(Product, Order.product_id == Product.id).join(Supplier, Order.supplier_id == Supplier.id).all()
    products = Product.query.all()
    suppliers = Supplier.query.all()
    
    return render_template('orders.html', orders=orders, products=products, suppliers=suppliers)
# Route to manage suppliers
@app.route('/suppliers', methods=['GET', 'POST'])
def manage_suppliers():
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        email = request.form['email']
        new_supplier = Supplier(name=name, contact=contact, email=email)
        db.session.add(new_supplier)
        db.session.commit()
        return redirect(url_for('manage_suppliers'))

    suppliers = Supplier.query.all()
    return render_template('suppliers.html', suppliers=suppliers)

# Route to get sales data (for visualizations)
@app.route('/sales_data')
def sales_data():
    orders = Order.query.all()
    sales_by_date = {}
    
    # Aggregate sales by date
    for order in orders:
        date_str = order.date.strftime('%Y-%m-%d')
        sales_by_date[date_str] = sales_by_date.get(date_str, 0) + order.quantity
    
    return jsonify(sales_by_date)

# Route to get top product data (for visualizations)
@app.route('/top_products_data')
def top_products_data():
    products = Product.query.all()
    product_sales = {}

    for product in products:
        product_sales[product.name] = sum(order.quantity for order in Order.query.filter_by(product_id=product.id))

    return jsonify(product_sales)

# Route to show visualizations
@app.route('/sales_visualization')
def sales_visualization():
    return render_template('sales_visualization.html')

if __name__ == '__main__':
    app.run(debug=True)
