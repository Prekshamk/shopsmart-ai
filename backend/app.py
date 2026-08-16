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
            "water bottle",
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
    return f"₹{price:,}"


def extract_budget(query):
    """
    Extract budget from queries such as:

    under 3000
    below ₹3000
    less than 3000
    within 3000
    budget 3000
    upto 3000
    up to ₹2,500
    """

    patterns = [
        r"(?:under|below|less than|within|upto|up to)\s*₹?\s*([\d,]+)",
        r"(?:budget|price)\s*(?:of|is|around)?\s*₹?\s*([\d,]+)",
        r"₹\s*([\d,]+)\s*(?:or less|maximum|max)"
    ]

    for pattern in patterns:
        match = re.search(pattern, query)

        if match:
            number = match.group(1).replace(",", "")

            try:
                return int(number)
            except ValueError:
                return None

    return None


def find_matching_products(query):
    """
    Find products based on keywords.
    """

    matches = []

    for product in products:

        for keyword in product["keywords"]:

            if keyword in query:
                matches.append(product)
                break

    return matches


def find_comparison_products(query):
    """
    Find products specifically mentioned in comparison queries.
    """

    selected = []

    # Headphones
    if "headphone" in query or "headphones" in query:
        selected.append(products[0])

    # Smart Watch
    if (
        "smartwatch" in query
        or "smart watch" in query
        or (
            "watch" in query
            and "water" not in query
        )
    ):
        selected.append(products[1])

    # Water Bottle
    if (
        "bottle" in query
        or "water bottle" in query
    ):
        selected.append(products[2])

    return selected


# ============================================================
# RECOMMENDATION API
# ============================================================

@app.route("/api/recommend", methods=["POST"])
def recommend():

    # --------------------------------------------------------
    # READ REQUEST
    # --------------------------------------------------------

    data = request.get_json(silent=True) or {}

    query = data.get("query", "")

    if not isinstance(query, str):
        query = str(query)

    query = query.lower().strip()


    # --------------------------------------------------------
    # EMPTY QUERY
    # --------------------------------------------------------

    if not query:

        return jsonify({
            "answer": (
                "Please tell me what you are looking for. "
                "For example, you can ask for headphones, "
                "something for fitness, the cheapest product, "
                "or products under ₹3000."
            )
        })


    # --------------------------------------------------------
    # EXTRACT BUDGET
    # --------------------------------------------------------

    budget = extract_budget(query)


    # ========================================================
    # 1. PRODUCT COMPARISON
    # ========================================================

    comparison_words = [
        "compare",
        "comparison",
        "versus",
        "vs",
        "difference",
        "price comparison"
    ]

    if any(word in query for word in comparison_words):

        comparison_products = find_comparison_products(query)

        # ----------------------------------------------------
        # Compare specifically mentioned products
        # ----------------------------------------------------

        if len(comparison_products) >= 2:

            comparison_text = []

            for product in comparison_products:

                comparison_text.append(
                    f"{product['name']} "
                    f"({format_price(product['price'])}) - "
                    f"{product['description']}"
                )

            cheapest = min(
                comparison_products,
                key=lambda product: product["price"]
            )

            expensive = max(
                comparison_products,
                key=lambda product: product["price"]
            )

            difference = (
                expensive["price"] - cheapest["price"]
            )

            answer = (
                "Here is the comparison: "
                + " | ".join(comparison_text)
                + ". "
                + f"{cheapest['name']} is the more affordable option. "
                + f"{expensive['name']} costs "
                + f"{format_price(difference)} more."
            )

            return jsonify({
                "answer": answer
            })


        # ----------------------------------------------------
        # Only one product mentioned
        # ----------------------------------------------------

        elif len(comparison_products) == 1:

            product = comparison_products[0]

            answer = (
                f"I found {product['name']} at "
                f"{format_price(product['price'])}. "
                f"{product['description']} "
                "Please mention another product if you want "
                "a comparison."
            )

            return jsonify({
                "answer": answer
            })


        # ----------------------------------------------------
        # Compare all products
        # ----------------------------------------------------

        else:

            sorted_products = sorted(
                products,
                key=lambda product: product["price"]
            )

            answer = (
                "Here is the price comparison: "
                f"{sorted_products[0]['name']} - "
                f"{format_price(sorted_products[0]['price'])}, "
                f"{sorted_products[1]['name']} - "
                f"{format_price(sorted_products[1]['price'])}, "
                f"and {sorted_products[2]['name']} - "
                f"{format_price(sorted_products[2]['price'])}."
            )

            return jsonify({
                "answer": answer
            })


    # ========================================================
    # 2. SHOW ALL PRODUCTS
    # ========================================================

    show_all_words = [
        "show all",
        "show me all",
        "all products",
        "all items",
        "available products",
        "available items",
        "what products",
        "what do you have",
        "catalog",
        "list products",
        "list all",
        "show me products"
    ]

    if any(word in query for word in show_all_words):

        answer = (
            "We currently have "
            "Wireless Headphones for ₹2,499, "
            "Smart Watch for ₹3,999, and "
            "Eco Water Bottle for ₹799."
        )

        return jsonify({
            "answer": answer
        })


    # ========================================================
    # 3. CHEAPEST PRODUCT
    # ========================================================

    cheapest_words = [
        "cheapest",
        "lowest price",
        "lowest",
        "most affordable",
        "affordable",
        "least expensive",
        "cheapest option"
    ]

    if any(word in query for word in cheapest_words):

        cheapest = min(
            products,
            key=lambda product: product["price"]
        )

        answer = (
            f"The most affordable option is "
            f"{cheapest['name']} at "
            f"{format_price(cheapest['price'])}. "
            f"{cheapest['description']}"
        )

        return jsonify({
            "answer": answer
        })


    # ========================================================
    # 4. BEST PRODUCT
    # ========================================================

    best_words = [
        "best product",
        "best option",
        "best choice",
        "best one",
        "recommend something",
        "recommend a product",
        "suggest something",
        "good product",
        "good option"
    ]

    if any(word in query for word in best_words):

        answer = (
            "Here are some options: "
            "Wireless Headphones for music and calls, "
            "Smart Watch for fitness and everyday activities, "
            "and Eco Water Bottle for sustainable everyday use."
        )

        return jsonify({
            "answer": answer
        })


    # ========================================================
    # 5. FIND PRODUCT MATCHES
    # ========================================================

    matching_products = find_matching_products(query)


    # ========================================================
    # 6. PRODUCT + BUDGET
    # ========================================================

    if budget is not None:

        # ----------------------------------------------------
        # User mentioned a specific product/category
        # ----------------------------------------------------

        if matching_products:

            affordable_matches = [
                product
                for product in matching_products
                if product["price"] <= budget
            ]

            # -----------------------------------------------
            # Matching product is within budget
            # -----------------------------------------------

            if affordable_matches:

                if len(affordable_matches) == 1:

                    product = affordable_matches[0]

                    answer = (
                        f"Yes! I recommend {product['name']} "
                        f"at {format_price(product['price'])}. "
                        f"It fits your budget of "
                        f"{format_price(budget)}. "
                        f"{product['description']}"
                    )

                else:

                    product_list = ", ".join(
                        f"{product['name']} "
                        f"({format_price(product['price'])})"
                        for product in affordable_matches
                    )

                    answer = (
                        f"Here are the products that fit your "
                        f"budget of {format_price(budget)}: "
                        f"{product_list}."
                    )

                return jsonify({
                    "answer": answer
                })


            # -----------------------------------------------
            # Matching product is NOT within budget
            # -----------------------------------------------

            else:

                closest = min(
                    matching_products,
                    key=lambda product: product["price"]
                )

                answer = (
                    f"I couldn't find a matching product within "
                    f"{format_price(budget)}. "
                    f"The closest option is "
                    f"{closest['name']} at "
                    f"{format_price(closest['price'])}."
                )

                return jsonify({
                    "answer": answer
                })


        # ----------------------------------------------------
        # User only gave a budget
        # ----------------------------------------------------

        affordable_products = [
            product
            for product in products
            if product["price"] <= budget
        ]

        if affordable_products:

            product_list = ", ".join(
                f"{product['name']} "
                f"({format_price(product['price'])})"
                for product in affordable_products
            )

            answer = (
                f"Here are the products available within "
                f"{format_price(budget)}: "
                f"{product_list}."
            )

        else:

            cheapest = min(
                products,
                key=lambda product: product["price"]
            )

            answer = (
                f"Unfortunately, there are no products within "
                f"{format_price(budget)}. "
                f"Our lowest-priced product is "
                f"{cheapest['name']} at "
                f"{format_price(cheapest['price'])}."
            )

        return jsonify({
            "answer": answer
        })


    # ========================================================
    # 7. SPECIFIC PRODUCT WITHOUT BUDGET
    # ========================================================

    if matching_products:

        # ----------------------------------------------------
        # One product
        # ----------------------------------------------------

        if len(matching_products) == 1:

            product = matching_products[0]

            answer = (
                f"I recommend {product['name']} at "
                f"{format_price(product['price'])}. "
                f"{product['description']}"
            )

            return jsonify({
                "answer": answer
            })


        # ----------------------------------------------------
        # Multiple products
        # ----------------------------------------------------

        product_list = ", ".join(
            f"{product['name']} "
            f"({format_price(product['price'])})"
            for product in matching_products
        )

        answer = (
            f"Based on your request, you can consider: "
            f"{product_list}."
        )

        return jsonify({
            "answer": answer
        })


    # ========================================================
    # 8. DEFAULT RESPONSE
    # ========================================================

    answer = (
        "I can help you choose a product. "
        "You can ask things like: "
        "\"I need something for music\", "
        "\"Suggest something for fitness\", "
        "\"What is the cheapest product?\", "
        "\"Compare headphones and smartwatch\", "
        "or \"Show me products under ₹3000\"."
    )

    return jsonify({
        "answer": answer
    })


# ============================================================
# RUN FLASK SERVER
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)