# ShopSmart AI

AI-powered full-stack e-commerce recommendation platform built using **React, Flask, and Python**.

## Features

* Responsive shopping landing page
* Featured product cards with images and prices
* AI shopping assistant
* Flask REST API backend
* React frontend with reusable components
* Frontend-backend integration using `fetch()` and JSON

## Tech Stack

* **Frontend:** React, Vite, JavaScript, CSS
* **Backend:** Flask, Flask-CORS, Python
* **Version Control:** Git & GitHub

## Project Structure

```text
shopsmart-ai/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── App.jsx
│   │   └── main.jsx
│   └── package.json
├── backend/
│   └── app.py
└── README.md
```

## Run Locally

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Backend

```bash
cd backend
pip install flask flask-cors
python app.py
```

Frontend runs at `http://localhost:5173`

Backend runs at `http://127.0.0.1:5000`

## API Endpoint

### POST `/api/recommend`

Request:

```json
{
  "query": "best headphones"
}
```

Response:

```json
{
  "answer": "I recommend Wireless Headphones for music and calls."
}
```

## Screenshots

Add screenshots of:

1. Home page
2. Featured products section
3. AI assistant interaction

## Future Enhancements

* Integrate Gemini API for real AI responses
* Add user authentication
* Add shopping cart and checkout
* Store products in MySQL
* Deploy frontend and backend online

## Author

**Preksha M K**
CSE (Data Science) Student | Full-Stack & AI Enthusiast
