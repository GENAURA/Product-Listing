#  Product Browser Backend

A high-performance product browsing application built with **FastAPI**, **SQLAlchemy**, and **Supabase PostgreSQL**. The project supports browsing a large product catalog with category filtering and cursor-based pagination, and includes a simple web UI served by FastAPI.

## ✨ Features

* FastAPI REST API
* Supabase PostgreSQL database
* SQLAlchemy ORM
* Cursor-based pagination for efficient large dataset browsing
* Category-based product filtering
* Bulk seeding of 200,000 products
* Swagger/OpenAPI documentation
* Simple frontend UI connected to backend APIs
* Ready for deployment on Render

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **Database:** PostgreSQL (Supabase)
* **ORM:** SQLAlchemy
* **Frontend:** HTML, CSS, JavaScript, Bootstrap
* **Server:** Uvicorn

---

## 📁 Project Structure

```text
codevector-backend/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── crud.py
│   ├── schemas.py
│   └── config.py
│
├── scripts/
│   └── seed_products.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── app.js
│   └── style.css
│
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd codevector-backend
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**macOS/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
DATABASE_URL=your_supabase_postgresql_connection_string
```

### 5. Run the application

```bash
uvicorn app.main:app --reload
```

---

## 🌐 Local URLs

| Endpoint      | Description               |
| ------------- | ------------------------- |
| `/`           | Health/Home endpoint      |
| `/docs`       | Swagger API documentation |
| `/products`   | Browse products           |
| `/categories` | List available categories |
| `/health`     | Health check              |
| `/ui`         | Web interface             |

Example:

```
http://127.0.0.1:8000/docs
```

---

## 🌱 Seed 200,000 Products

Run:

```bash
python -m scripts.seed_products
```

The script performs bulk inserts to efficiently populate the database.

---

## 📄 Example API Requests

Retrieve products:

```
GET /products?limit=20
```

Filter by category:

```
GET /products?category=Electronics&limit=20
```

Retrieve categories:

```
GET /categories
```

---

## 🚀 Deployment

The application can be deployed on Render.

**Build Command**

```bash
pip install -r requirements.txt
```

**Start Command**

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

Configure the `DATABASE_URL` environment variable with your Supabase PostgreSQL connection string.

---

## 🧠 Design Decisions

* **FastAPI** was chosen for its performance and automatic API documentation.
* **Supabase PostgreSQL** provides a managed cloud database with PostgreSQL compatibility.
* **Cursor-based pagination** was implemented instead of offset pagination to improve scalability and reduce the likelihood of duplicate or skipped records when data changes.
* **Bulk inserts** are used to efficiently generate and load 200,000 products.

---

## 🔮 Future Improvements

* Full-text product search
* Opaque cursor tokens
* Authentication and authorization
* Automated testing
* Caching and monitoring
* CI/CD pipeline
* Advanced frontend filtering and sorting


## 👨‍💻 Author

**Shubham Kumar**

Built as part of the CodeVector Backend Assignment using FastAPI, Supabase PostgreSQL, and SQLAlchemy.
