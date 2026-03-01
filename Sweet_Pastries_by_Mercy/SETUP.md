# Quick Setup Guide

This guide will get you up and running with Sweet Pastries by Mercy API in just a few minutes.

## Prerequisites Check

Before you begin, ensure you have:
- [ ] Python 3.8 or higher installed
- [ ] PostgreSQL 12 or higher installed and running
- [ ] Git installed
- [ ] A terminal/command prompt

## Quick Start (5 Steps)

### Step 1: Clone and Navigate
```bash
git clone https://github.com/Michael-Mbuthia/Sweet-Pastries-by-Mercy.git
cd Sweet-Pastries-by-Mercy/Sweet_Pastries_by_Mercy
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

You should see `(.venv)` in your terminal prompt.

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- Django 6.0
- Django REST Framework
- JWT Authentication
- PostgreSQL adapter
- Image processing library
- And other dependencies

### Step 4: Setup Database

#### Option A: Using PostgreSQL Command Line
```bash
# Connect to PostgreSQL
psql -U postgres

# In PostgreSQL shell, run:
CREATE DATABASE bakery_db;
\q
```

#### Option B: Using pgAdmin
1. Open pgAdmin
2. Right-click on "Databases"
3. Select "Create" → "Database"
4. Name it `bakery_db`
5. Click "Save"

Then configure the database in `Sweet_Pastries_by_Mercy/settings.py`:
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "bakery_db",
        "USER": "postgres",
        "PASSWORD": "YOUR_POSTGRES_PASSWORD",  # Change this!
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

### Step 5: Initialize and Run
```bash
# Apply database migrations
python manage.py migrate

# Create admin user (follow prompts)
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

## Verify Installation

### 1. Check API is Running
Open your browser and visit: http://localhost:8000/api/products/

You should see a Django REST Framework browsable API page.

### 2. Access Admin Panel
Visit: http://localhost:8000/admin/

Login with the superuser credentials you created.

### 3. Test API with curl
```bash
# Register a new user
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass123","password2":"testpass123","email":"test@example.com"}'

# Login
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass123"}'
```

## Common Issues and Solutions

### Issue 1: "psycopg2" installation fails
**Solution:**
```bash
pip install psycopg2-binary
```

### Issue 2: "database does not exist"
**Solution:** Make sure you created the database in PostgreSQL:
```bash
psql -U postgres -c "CREATE DATABASE bakery_db;"
```

### Issue 3: "Port 8000 already in use"
**Solution:** Run on a different port:
```bash
python manage.py runserver 8080
```

### Issue 4: "permission denied" for PostgreSQL
**Solution:** Check your PostgreSQL user and password in settings.py match your PostgreSQL installation.

### Issue 5: "No module named 'PIL'"
**Solution:**
```bash
pip install Pillow
```

## Next Steps

### 1. Create Sample Data
Use the Django admin panel to create:
1. Categories (e.g., "Cakes", "Pastries", "Cookies")
2. Products with images, prices, and stock quantities

### 2. Test the API
Use tools like:
- **Postman** - Download from https://www.postman.com/
- **Thunder Client** - VS Code extension
- **curl** - Command line tool (already installed on most systems)

### 3. Read Full Documentation
See [README.md](README.md) for:
- Complete API endpoint documentation
- Authentication examples
- Advanced filtering and search
- Production deployment guide

## Development Workflow

### Daily Development
```bash
# Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Run server
python manage.py runserver

# In another terminal, run tests (optional)
python manage.py test
```

### Making Changes to Models
```bash
# After modifying models.py files
python manage.py makemigrations
python manage.py migrate
```

### Adding Sample Products (Django Shell)
```bash
python manage.py shell
```

```python
from products.models import Category, Product

# Create a category
pastries = Category.objects.create(name="Pastries")

# Create a product
Product.objects.create(
    name="Chocolate Croissant",
    description="Buttery, flaky croissant with dark chocolate",
    price=4.50,
    stock_quantity=30,
    category=pastries
)

print("Sample data created!")
exit()
```

## Quick Reference Commands

| Task | Command |
|------|---------|
| Start server | `python manage.py runserver` |
| Create migrations | `python manage.py makemigrations` |
| Apply migrations | `python manage.py migrate` |
| Create superuser | `python manage.py createsuperuser` |
| Run tests | `python manage.py test` |
| Open shell | `python manage.py shell` |
| Check for issues | `python manage.py check` |

## Environment Variables (Optional)

For better security, copy `.env.example` to `.env`:
```bash
copy .env.example .env  # Windows
cp .env.example .env    # macOS/Linux
```

Then edit `.env` with your actual values.

## Getting Help

- **Documentation**: See [README.md](README.md)
- **Django Docs**: https://docs.djangoproject.com/
- **DRF Docs**: https://www.django-rest-framework.org/
- **Issues**: Open an issue on GitHub

## Success Checklist

By now, you should be able to:
- [ ] Access http://localhost:8000/api/products/
- [ ] Login to http://localhost:8000/admin/
- [ ] Register a user via API
- [ ] Get a JWT token
- [ ] Make authenticated requests

If you can do all of the above, congratulations! 🎉 Your setup is complete!

---

**Need help?** Check the [full README](README.md) or open an issue on GitHub.
