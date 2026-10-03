from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Notebook",
        "price": 199
    },
    {
        "id": 2,
        "name": "Coffee Mug",
        "price": 299
    },
    {
        "id": 3,
        "name": "Wall Art",
        "price": 499
    }
]

@app.route("/api/products")
def get_products():
    return jsonify(products)

@app.route("/api/health")
def health():
    return jsonify({"status": "Backend is running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
