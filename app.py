from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'cambia-esta-clave'

# Datos de ejemplo para la tienda
ITEMS = [
    {'id': 1, 'name': 'Camisa', 'price': 20.0, 'image': 'https://via.placeholder.com/150'},
    {'id': 2, 'name': 'Pantal\u00f3n', 'price': 35.0, 'image': 'https://via.placeholder.com/150'},
    {'id': 3, 'name': 'Chaqueta', 'price': 50.0, 'image': 'https://via.placeholder.com/150'}
]

@app.route('/')
def index():
    cart = session.get('cart', {})
    return render_template('index.html', items=ITEMS, cart=cart)

@app.route('/add/<int:item_id>', methods=['POST'])
def add_to_cart(item_id):
    cart = session.get('cart', {})
    cart[item_id] = cart.get(item_id, 0) + 1
    session['cart'] = cart
    return redirect(url_for('index'))

@app.route('/cart')
def view_cart():
    cart = session.get('cart', {})
    cart_items = []
    total = 0
    for item in ITEMS:
        quantity = cart.get(item['id'], 0)
        if quantity:
            subtotal = item['price'] * quantity
            total += subtotal
            cart_items.append({'item': item, 'qty': quantity, 'total': subtotal})
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/clear_cart', methods=['POST'])
def clear_cart():
    session['cart'] = {}
    return redirect(url_for('view_cart'))

if __name__ == '__main__':
    app.run(debug=True)
