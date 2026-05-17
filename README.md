# Car Dealership 🚗

> A full-featured car dealership web platform built with **Django 5.2**, featuring advanced search & filtering, multi-image galleries, inquiry messaging, and a Bootstrap 4 frontend.

---

## 📸 Preview

| Home | Cars Listing | Car Detail |
|------|-------------|------------|
| Featured cars, search bar, team | Paginated grid with filters | Gallery, specs, inquiry form |

---

## 📦 Tech Stack

<p>
  <img src="https://skillicons.dev/icons?i=python,django,bootstrap,sqlite,js" height="40"/>
</p>

| Layer | Technology |
|-------|-----------|
| Backend | Django 5.2 |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Frontend | Bootstrap 4 + jQuery |
| Rich Text | CKEditor 6 |
| Images | Pillow |

---

## ✨ Features

- ✅ Browse car listings with pagination (6 per page)
- ✅ Advanced search & filter by model, city, year, body style, transmission, price range
- ✅ Multi-image gallery per listing
- ✅ Inquiry messaging system (one per car per user)
- ✅ User registration, login & personal dashboard
- ✅ Featured cars on homepage
- ✅ Team members showcase
- ✅ Contact form
- ✅ Rich text descriptions with CKEditor
- ✅ Full admin panel with inline image management & bulk actions

---

## 🚀 Getting Started

```bash
# 1. Clone
git clone https://github.com/alisamadzadeh46/car.git
cd car

# 2. Create virtual environment
py -m venv .venv

# 3. Activate
# Windows:
.\.venv\Scripts\Activate
# Mac/Linux:
source .venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Migrate
python manage.py migrate

# 6. Load sample data
python manage.py loaddata seed.json

# 7. Copy media files (sample images)
# Copy the media/ folder from the repo to your project root

# 8. Create superuser
python manage.py createsuperuser

# 9. Run
python manage.py runserver
```

Visit → **http://localhost:8000**

---

## 🔗 Pages

| Page | URL |
|------|-----|
| Home | http://localhost:8000/ |
| Cars | http://localhost:8000/cars/ |
| Search | http://localhost:8000/search/ |
| Register | http://localhost:8000/accounts/register/ |
| Login | http://localhost:8000/accounts/login/ |
| Dashboard | http://localhost:8000/accounts/dashboard/ |
| Admin | http://localhost:8000/admin/ |

---

## 📁 Project Structure

```
car/
├── car/              # Settings & main URLs
├── cars/             # Listings, search, inquiries
├── home/             # Homepage, about, contact, team
├── accounts/         # Auth & dashboard
├── templates/        # HTML templates (Bootstrap 4)
├── static/           # CSS, JS, images
├── media/            # Uploaded files
├── fixtures/
│   └── seed.json     # Sample data (10 cars + 3 team members)
└── requirements.txt
```

---

## ⚙️ PostgreSQL (Production)

In `car/settings.py`, uncomment:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'car',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 📄 License

MIT License

---

<p align="center">Made with ❤️ by <a href="https://github.com/alisamadzadeh46">Ali Samadzadeh</a></p>
