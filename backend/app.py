from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.json
    query = data.get('query', '').lower()

    if 'headphone' in query:
        answer = 'I recommend Wireless Headphones for music and calls.'
    elif 'watch' in query:
        answer = 'The Smart Watch is a great choice for fitness tracking.'
    elif 'bottle' in query:
        answer = 'The Eco Water Bottle is a sustainable option.'
    else:
        answer = 'Please search for headphones, watch, or bottle.'

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)