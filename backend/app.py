from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)


# ============================================================
# PRODUCT DATA
# ============================================================

products = [
    {
        "name": "Wireless Headphones",
        "price": 2499,
        "description": "Great for music, calls, and entertainment.",
        "keywords": [
            "headphone",
            "headphones",
            "music",
            "audio",
            "sound",
            "call",
            "calls",
            "entertainment"
        ]
    },
    {
        "name": "Smart Watch",
        "price": 3999,
        "description": "Useful for fitness tracking and everyday activities.",
        "keywords": [
            "watch",
            "smartwatch",
            "smart watch",
            "fitness",
            "exercise",
            "workout",
            "health",
            "activity"
        ]
    },
    {
        "name": "Eco Water Bottle",
        "price": 799,
        "description": "A reusable and sustainable water bottle.",
        "keywords": [
            "bottle",
            "water",
            "sustainable",
            "sustainability",
            "eco",
            "eco-friendly",
            "reusable",
            "environment"
        ]
    }
]


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def format_price(price):
    """
    Convert 2499 -> ₹2,499
    """
    return f"₹{price:,}"


def extract_budget(query):
    """
    Detect price limits from natural language.

    Examples:
    under 3000
    below ₹3000
    less than 3000
    within 3000
    budget 3000
    under ₹2,500
    """

    patterns = [
        r'(?:under|below|less than|within|max(?:imum)?|upto|up to)\s*₹?\s*([\d,]+)',
        r'(?:budget|price)\s*(?:of|is|around)?\s*₹?\s*([\d,]+)',
        r'₹\s*([\d,]+)\s*(?:or less|maximum|max)'
    ]

    for pattern in patterns:
        match = re.search(pattern, query)

        if match:
            number = match.group(1).replace(',', '')

            try:
                return int(number)
            except ValueError:
                return None

    return None


def find_matching_products(query):
    """
    Find products based on keywords in the user's query.
    """

    matches = []

    for product in products:

        for keyword in product["keywords"]:

            if keyword in query:
                matches.append(product)
                break

    return matches


def product_details(product):
    """
    Return a nicely formatted product description.
    """

    return (
        f"{product['name']} at {format_price(product['price'])}. "
        f"{product['description']}"
    )


# ============================================================
# MAIN RECOMMENDATION API
# ============================================================

@app.route('/api/recommend', methods=['POST'])
def recommend():

    # --------------------------------------------------------
    # GET USER QUERY
    # --------------------------------------------------------

    data = request.get_json(silent=True) or {}

    query = data.get('query', '')

    if not isinstance(query, str):
        query = str(query)

    query = query.lower().strip()


    # --------------------------------------------------------
    # EMPTY QUERY
    # --------------------------------------------------------

    if not query:

        return jsonify({
            'answer': (
                'Please tell me what you are looking for. '
                'For example, you can ask for headphones, '
                'a fitness product, the cheapest product, '
                'or products under ₹3000.'
            )
        })


    # --------------------------------------------------------
    # EXTRACT BUDGET
    # --------------------------------------------------------

    budget = extract_budget(query)


    # --------------------------------------------------------
    # SHOW ALL PRODUCTS
    # --------------------------------------------------------

    show_all_words = [
        'show all',
        'show me all',
        'all products',
        'all items',
        'available products',
        'available items',
        'what products',
        'what do you have',
        'catalog',
        'list products',
        'list all'
    ]

    if any(word in query for word in show_all_words):

        answer = (
            "We currently have "
            "Wireless Headphones for ₹2,499, "
            "Smart Watch for ₹3,999, and "
            "Eco Water Bottle for ₹799."
        )

        return jsonify({'answer': answer})


    # --------------------------------------------------------
    # CHEAPEST PRODUCT
    # --------------------------------------------------------

    cheapest_words = [
        'cheapest',
        'lowest price',
        'lowest',
        'most affordable',
        'affordable',
        'least expensive',
        'cheaper option',
        'cheapest option'
    ]

    if any(word in query for word in cheapest_words):

        cheapest = min(
            products,
            key=lambda product: product['price']
        )

        answer = (
            f"The most affordable option is "
            f"{product_details(cheapest)}"
        )

        return jsonify({'answer': answer})


    # --------------------------------------------------------
    # BEST PRODUCT
    # --------------------------------------------------------

    best_words = [
        'best product',
        'best option',
        'best choice',
        'best one',
        'recommend something',
        'recommend a product',
        'suggest something',
        'good product',
        'good option'
    ]

    if any(word in query for word in best_words):

        answer = (
            "Here are some options: "
            "Wireless Headphones for music and calls, "
            "Smart Watch for fitness and everyday activities, "
            "and Eco Water Bottle for sustainable everyday use."
        )

        return jsonify({'answer': answer})


    # --------------------------------------------------------
    # FIND PRODUCTS MATCHING USER'S REQUIREMENT
    # --------------------------------------------------------

    matching_products = find_matching_products(query)


    # --------------------------------------------------------
    # PRODUCT + BUDGET
    #
    # Example:
    # "music under 3000"
    # "fitness below 4000"
    # "bottle under 1000"
    # --------------------------------------------------------

    if budget is not None:

        # If user mentioned a specific product/category
        if matching_products:

            affordable_matches = [
                product
                for product in matching_products
                if product['price'] <= budget
            ]

            if affordable_matches:

                if len(affordable_matches) == 1:

                    product = affordable_matches[0]

                    answer = (
                        f"Yes! I recommend {product['name']} "
                        f"at {format_price(product['price'])}. "
                        f"It fits your budget of {format_price(budget)}. "
                        f"{product['description']}"
                    )

                else:

                    names = ", ".join(
                        f"{product['name']} ({format_price(product['price'])})"
                        for product in affordable_matches
                    )

                    answer = (
                        f"Here are the products that fit your budget "
                        f"of {format_price(budget)}: {names}."
                    )

                return jsonify({'answer': answer})


            else:

                cheapest_match = min(
                    matching_products,
                    key=lambda product: product['price']
                )

                answer = (
                    f"I couldn't find a matching product within "
                    f"{format_price(budget)}. "
                    f"The closest option is {cheapest_match['name']} "
                    f"at {format_price(cheapest_match['price'])}."
                )

                return jsonify({'answer': answer})


        # ----------------------------------------------------
        # ONLY BUDGET GIVEN
        # Example:
        # "products under 3000"
        # "show products below 3000"
        # ----------------------------------------------------

        affordable_products = [
            product
            for product in products
            if product['price'] <= budget
        ]

        if affordable_products:

            product_list = ", ".join(
                f"{product['name']} ({format_price(product['price'])})"
                for product in affordable_products
            )

            answer = (
                f"Here are the products available within "
                f"{format_price(budget)}: {product_list}."
            )

        else:

            cheapest = min(
                products,
                key=lambda product: product['price']
            )

            answer = (
                f"Unfortunately, there are no products within "
                f"{format_price(budget)}. "
                f"Our lowest-priced product is "
                f"{cheapest['name']} at "
                f"{format_price(cheapest['price'])}."
            )

        return jsonify({'answer': answer})


    # --------------------------------------------------------
    # SPECIFIC PRODUCT WITHOUT BUDGET
    # --------------------------------------------------------

    if matching_products:

        # If only one product matches
        if len(matching_products) == 1:

            product = matching_products[0]

            answer = (
                f"I recommend {product['name']} "
                f"at {format_price(product['price'])}. "
                f"{product['description']}"
            )

            return jsonify({'answer': answer})


        # Multiple products match
        names = ", ".join(
            f"{product['name']} ({format_price(product['price'])})"
            for product in matching_products
        )

        answer = (
            f"Based on your request, you can consider: {names}."
        )

        return jsonify({'answer': answer})


    # --------------------------------------------------------
    # PRICE COMPARISON
    # --------------------------------------------------------

    comparison_words = [
        'compare prices',
        'price comparison',
        'compare products',
        'compare',
        'price'
    ]

    if any(word in query for word in comparison_words):

        sorted_products = sorted(
            products,
            key=lambda product: product['price']
        )

        answer = (
            f"Price comparison: "
            f"{sorted_products[0]['name']} - "
            f"{format_price(sorted_products[0]['price'])}, "
            f"{sorted_products[1]['name']} - "
            f"{format_price(sorted_products[1]['price'])}, "
            f"and {sorted_products[2]['name']} - "
            f"{format_price(sorted_products[2]['price'])}."
        )

        return jsonify({'answer': answer})


    # --------------------------------------------------------
    # DEFAULT RESPONSE
    # --------------------------------------------------------

    answer = (
        "I can help you choose a product. "
        "You can ask things like: "
        "\"I need something for music\", "
        "\"Suggest something for fitness\", "
        "\"What is the cheapest product?\", "
        "or \"Show me products under ₹3000\"."
    )

    return jsonify({'answer': answer})


# ============================================================
# RUN FLASK SERVER
# ============================================================

if __name__ == '__main__':
    app.run(debug=True)