# Sweet Pastries by Mercy 🥐

A Django REST Framework e-commerce API for a pastry shop with product management, shopping cart, order processing, and multi-payment gateway support.

## ✨ Features

- **Products**: Browse, search, and filter pastries with images and categories
- **Cart**: Add, update, and remove items from personalized shopping cart
- **Orders**: Complete checkout with order history and status tracking
- **Payments**: Support for PayPal and M-Pesa payment methods
- **Authentication**: JWT-based secure API access with token refresh
- **Admin**: Django admin panel and REST API for order management

## 🛠 Tech Stack

Django 6.0 • Django REST Framework • JWT Auth • PostgreSQL • django-filter • Pillow

## 📁 Project Structure

```
Sweet_Pastries_by_Mercy/
├── accounts/          # User registration and JWT auth
├── products/          # Product catalog with categories
├── cart/              # Shopping cart management
├── orders/            # Order processing and payment
└── Sweet_Pastries_by_Mercy/  # Django settings
```

## 🗄 Models

**Products**: Category, Product (with images, pricing, stock)  
**Cart**: Cart, CartItem  
**Orders**: Order, OrderItem, Payment (PayPal/M-Pesa)  
**Auth**: Django User model

## 🚀 Quick Start

**See [SETUP.md](SETUP.md) for detailed installation instructions.**

```bash
# 1. Clone and setup
git clone https://github.com/Michael-Mbuthia/Sweet-Pastries-by-Mercy.git
cd Sweet-Pastries-by-Mercy/Sweet_Pastries_by_Mercy
python -m venv .venv
.venv\Scripts\activate  # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure database in settings.py, then:
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit: http://localhost:8000/api/products/

## 📡 API Endpoints

**See [API_EXAMPLES.md](API_EXAMPLES.md) for detailed examples and testing guide.**

| Endpoint | Method | Description | Auth |
|----------|--------|-------------|------|
| `/api/auth/register/` | POST | Register user | No |
| `/api/auth/login/` | POST | Get JWT tokens | No |
| `/api/auth/token/refresh/` | POST | Refresh token | No |
| `/api/products/` | GET | List products (filter, search, sort) | No |
| `/api/products/<id>/` | GET | Product details | No |
| `/api/products/create/` | POST | Create product | Admin |
| `/api/products/<id>/update/` | PUT/PATCH | Update product | Admin |
| `/api/products/<id>/delete/` | DELETE | Delete product | Admin |
| `/api/cart/` | GET | View cart | Yes |
| `/api/cart/add/` | POST | Add to cart | Yes |
| `/api/cart/update/` | POST | Update quantity | Yes |
| `/api/cart/remove/` | POST | Remove item | Yes |
| `/api/orders/checkout/` | POST | Create order | Yes |
| `/api/orders/` | GET | Order history | Yes |
| `/api/orders/admin/` | GET | All orders | Admin |
| `/api/orders/admin/<id>/` | PUT/PATCH | Update order | Admin |

**Product Filtering**: `?category=1&search=chocolate&ordering=-price`

## 🔐 Authentication

JWT tokens required for protected endpoints.

```bash
# Login
POST /api/auth/login/
{"username": "user", "password": "pass"}
# Returns: {"access": "token...", "refresh": "token..."}

# Use token
Authorization: Bearer <access_token>
```

Token lifetime: Access (60 min), Refresh (1 day)

## 🔧 Development

```bash
python manage.py test                    # Run tests
python manage.py createsuperuser         # Create admin
python manage.py shell                   # Django shell
python manage.py makemigrations          # Create migrations
```

## 🚀 Production Deployment

**Critical Security Steps:**

1. **Environment Variables** - Use `.env` file (see `.env.example`)
2. **Settings** - Set `DEBUG=False` and update `SECRET_KEY`
3. **Hosts** - Configure `ALLOWED_HOSTS`
4. **Static Files** - Run `python manage.py collectstatic`
5. **HTTPS** - Enable SSL and set security cookies
6. **Database** - Use production PostgreSQL instance

## 📝 Documentation

- **[SETUP.md](SETUP.md)** - Detailed setup guide with troubleshooting
- **[API_EXAMPLES.md](API_EXAMPLES.md)** - Complete API testing examples

## 🎯 Future Enhancements

- Email notifications • Real-time order tracking • Product reviews • Loyalty program • Advanced analytics • Wishlist • Multi-language support

## 📄 License

Private and proprietary to Sweet Pastries by Mercy.

---

**Made with ❤️ by Sweet Pastries by Mercy Team**
