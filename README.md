# Flask API

Simple REST API built with **Flask** and deployed on **Vercel** using Serverless Functions.

## 🚀 Live Demo

[https://flask-api-nu-seven.vercel.app/](https://flask-api-nu-seven.vercel.app/)

## 📦 Repository

[https://github.com/Kenkyoo/flask-api](https://github.com/Kenkyoo/flask-api)

## ✨ Features

* Flask-based REST API
* JSON responses
* Serverless deployment on Vercel
* Simple project structure
* Ideal for frontend consumption (React / Vue)

## 📁 Project Structure

```
.
├── app.py
├── requirements.txt
├── vercel.json
└── data.json
```

## 🔌 API Endpoints

### Get sample data

```
GET /api/data
```

**Response (example):**

```json
{
  "notes": [
    {
      "id": 1,
      "title": "Aprender Flask",
      "body": "Repasar rutas y jsonify",
      "completed": false
    }
  ]
}
```

## 🛠️ Tech Stack

* Python
* Flask
* Vercel Serverless Functions

## 📄 Requirements

```
Flask==3.1.2
gunicorn==23.0.0
```

> ⚠️ **Note:** `gunicorn` is not required for Vercel, but is included for compatibility with other platforms.

## ▶️ Run Locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

API available at:

```
http://localhost:5000/api/data
```

## ☁️ Deploy on Vercel

1. Fork or clone the repository
2. Go to [https://vercel.com](https://vercel.com)
3. Import the repository
4. Deploy

The API will be available at:

```
https://your-project.vercel.app/api/data
```

## 🧪 Use Case

This project is intended for:

* Learning Flask
* Mock APIs
* Portfolio projects
* Frontend testing

---

Made with Flask 🐍
