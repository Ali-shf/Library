# Library Management

**Author:** Ali Shahrabi  
**App:** book (includes account URLs)  
**Framework:** Django  
**Views:** Function-Based Views (FBV)  
**Templates:** Django Templates

---

## Project Overview

A simple **Library Management System** implemented in Django. Users can manage books with basic CRUD operations and filtering capabilities.

---

## Workflow

1. **User Authentication (Optional)**
   - Register and login (handled inside `book` app).

2. **Book Management**
   - **Add Book:** Create new book entries.
   - **View Books:** Display all books.
   - **Search & Filter:** Search by title, author, or filter by price/publication date.
   - **Edit Book:** Update book details.
   - **Delete Book:** Remove individual or filtered books.

3. **Templates**
   - All pages use Django templates for rendering forms and book lists in a user-friendly layout.

---

## Project Structure

```
library_management/
│
├── book/
│   ├── templates/
│   ├── views.py          # Function-Based Views
│   ├── urls.py           # Book and account routes
│   └── models.py
├── library_management/
│   └── settings.py
└── manage.py
```

---

## Installation

```bash
git clone <repository_url>
cd library_management
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) to access the app.

---

## License

MIT License
