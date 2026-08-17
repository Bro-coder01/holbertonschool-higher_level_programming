import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_data():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv_data():
    products = []
    try:
        with open('products.csv', 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row['id']),
                    "name": row['name'],
                    "category": row['category'],
                    "price": float(row['price'])
                })
        return products
    except (FileNotFoundError, KeyError, ValueError):
        return []


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json_data()
    elif source == 'csv':
        data = read_csv_data()
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id is not None:
        try:
            target_id = int(product_id)
            filtered = [p for p in data if p.get('id') == target_id]
            if not filtered:
                return render_template('product_display.html', error="Product not found")
            data = filtered
        except ValueError:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
