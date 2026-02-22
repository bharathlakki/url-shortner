🔗 Shortify – Flask URL Shortener

![Shortify UI Screenshot](logo.png) <!-- Add a screenshot if you'd like -->

**Shortify** is a modern, minimal, and fully-functional URL shortener built using **Flask** and **MongoDB**. It allows you to shorten URLs, customize short codes, track click counts, and optionally set expiration times.

---

## 🚀 Features

- 🔗 Shorten long URLs into compact links
- ✏️ Optional **custom short codes**
- ⏳ Optional **expiration** (in hours)
- 📈 Real-time **click tracking**
- 📋 Copy-to-clipboard button
- 🎨 Clean, responsive Bootstrap frontend
- ❌ 404 page for broken links

---

## 🧱 Tech Stack

- Backend: [Flask](https://flask.palletsprojects.com/)
- Database: [MongoDB](https://www.mongodb.com/)
- Frontend: HTML, Bootstrap 5, JavaScript
- Others: `pymongo`, `python-dotenv`

---

## 📂 Project Structure

```
shortify/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── routes.py
│   └── utils.py
├── templates/
│   ├── index.html
│   └── 404.html
├── static/              # Optional for CSS/JS
├── run.py
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/Nuraj250/shortify
cd shortify
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
MONGO_URI=Include your MongoDB String
DB_NAME=shortify
BASE_URL=http://localhost:5000
```

### 5. Run the App

```bash
python run.py
```

Visit `http://localhost:5000` in your browser 🎉

---

## 📡 API Endpoints

### `POST /shorten`

Shortens a URL.

#### Request Body (JSON):
```json
{
  "url": "https://example.com/long-url",
  "custom_code": "mycustomcode",    // optional
  "expires_in": 24                  // optional (in hours)
}
```

#### Response:
```json
{
  "short_url": "http://localhost:5000/mycustomcode",
  "custom_code": "mycustomcode",
  "expires_in": 24
}
```

---

### `GET /<short_code>`

Redirects to the original URL, or returns a 404 page if invalid or expired.

---

### `GET /<short_code>/stats`

Returns click stats for a short URL.

#### Response:
```json
{
  "short_code": "abc123",
  "clicks": 5
}
```

---

## 🛠 Future Ideas

- 🔐 Admin dashboard for URL management
- 📦 Docker support for deployment
- 📊 Analytics with charts
- 💬 QR code generation



Pull requests and feature ideas are welcome! Drop a ⭐ if you like the project.
