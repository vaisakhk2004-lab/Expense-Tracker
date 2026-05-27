# Expense Tracker

A full-stack Expense Tracker application built using **FastAPI**, **Streamlit**, and **MySQL**.  
This project helps users manage and analyze their expenses efficiently with filtering options based on date, month, and category.

---

## Features

- Add daily expenses
- Update existing expenses
- Delete expenses
- Track expenses by date
- Monthly expense analytics
- Category-wise expense tracking
- Interactive Streamlit UI
- FastAPI backend for API handling
- MySQL database integration

---

## Tech Stack

### Frontend
- Streamlit

### Backend
- FastAPI
- Uvicorn

### Database
- MySQL

---

## Project Structure

```bash
expense_tracker/
│
├── backend/
│   ├── server.py
│   ├── db_helper.py
│   ├── models.py
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
├── sql/
│   └── expense_db.sql
│
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone <your-github-repo-link>
cd expense_tracker
```

---

## Backend Setup (FastAPI)

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run FastAPI Server

```bash
uvicorn server:app --reload
```

FastAPI server will run on:

```bash
http://127.0.0.1:8000
```

---

## Frontend Setup (Streamlit)

### Run Streamlit App

```bash
streamlit run app.py
```

Streamlit app will run on:

```bash
http://localhost:8501
```

---

## Database Setup

1. Create a MySQL database
2. Import the SQL file:

```sql
expense_db.sql
```

3. Update database credentials in:

```python
db_helper.py
```

Example:

```python
host="localhost"
user="root"
password="your_password"
database="expense_manager"
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/expenses/{date}` | Get expenses by date |
| POST | `/expenses/{date}` | Add or update expenses |
| POST | `/analytics_by_month` | Get monthly analytics |

---

## Analytics Included

- Total monthly spending
- Category-wise spending
- Expense trends
- Monthly summaries

---

## Future Improvements

- User authentication
- Export reports to Excel/PDF
- Budget tracking
- Charts and visualizations
- Cloud deployment

---

## Author

Developed by Vaisakh K
