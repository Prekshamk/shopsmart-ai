from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Product data
products = [
    {
        "name": "Wireless Headphones",
        "price": 2499,
        "description": "Great for music, calls, and entertainment."
    },
    {
        "name": "Smart Watch",
        "price": 3999,
        "description": "Useful for fitness tracking and everyday activities."
    },
    {
        "name": "Eco Water Bottle",
        "price": 799,
        "description": "A reusable and sustainable water bottle."
    }
]


@app.route('/api/recommend', methods=['POST'])
def recommend():

    data = request.get_json()
    query = data.get('query', '').lower().strip()

    # Empty query
    if not query:
        return jsonify({
            'answer': 'Please tell me what product you are looking for.'
        })

    # ------------------------------------------------
    # 1. CHEAPEST / LOWEST PRICE
    # ------------------------------------------------
    if any(word in query for word in ['cheapest', 'lowest', 'budget', 'affordable']):

        cheapest = min(products, key=lambda product: product['price'])

        answer = (
            f"The most affordable option is {cheapest['name']} "
            f"at ₹{cheapest['price']}. {cheapest['description']}"
        )

        return jsonify({'answer': answer})

    # ------------------------------------------------
    # 2. HEADPHONES
    # ------------------------------------------------
    if any(word in query for word in ['headphone', 'headphones', 'music', 'audio']):

        product = products[0]

        answer = (
            f"I recommend {product['name']} at ₹{product['price']}. "
            f"{product['description']}"
        )

        return jsonify({'answer': answer})

    # ------------------------------------------------
    # 3. SMART WATCH
    # ------------------------------------------------
    if any(word in query for word in ['watch', 'smartwatch', 'fitness']):

        product = products[1]

        answer = (
            f"I recommend {product['name']} at ₹{product['price']}. "
            f"{product['description']}"
        )

        return jsonify({'answer': answer})

    # ------------------------------------------------
    # 4. WATER BOTTLE
    # ------------------------------------------------
    if any(word in query for word in ['bottle', 'water', 'sustainable', 'eco']):

        product = products[2]

        answer = (
            f"I recommend {product['name']} at ₹{product['price']}. "
            f"{product['description']}"
        )

        return jsonify({'answer': answer})

    # ------------------------------------------------
    # 5. BEST PRODUCT
    # ------------------------------------------------
    if any(word in query for word in ['best', 'recommend', 'suggestion']):

        answer = (
            "Here are some options: "
            "Wireless Headphones for music, "
            "Smart Watch for fitness, and "
            "Eco Water Bottle for sustainable everyday use."
        )

        return jsonify({'answer': answer})

    # ------------------------------------------------
    # 6. SHOW ALL PRODUCTS
    # ------------------------------------------------
    if any(word in query for word in ['products', 'items', 'available', 'catalog']):

        answer = (
            "We currently have Wireless Headphones for ₹2,499, "
            "Smart Watch for ₹3,999, and "
            "Eco Water Bottle for ₹799."
        )

        return jsonify({'answer': answer})

    # ------------------------------------------------
    # 7. DEFAULT RESPONSE
    # ------------------------------------------------
    answer = (
        "I can help you find products such as Wireless Headphones, "
        "Smart Watch, or Eco Water Bottle. "
        "You can also ask for the cheapest or best option."
    )

    return jsonify({'answer': answer})


if __name__ == '__main__':
    app.run(debug=True)