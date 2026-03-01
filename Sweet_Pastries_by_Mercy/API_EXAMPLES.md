# API Examples & Testing Guide

This document provides practical examples for testing all API endpoints using various tools.

## Table of Contents
- [Using Postman](#using-postman)
- [Using curl](#using-curl)
- [Using Python Requests](#using-python-requests)
- [Common Workflows](#common-workflows)

## Base URL
```
http://localhost:8000
```

---

## Authentication Endpoints

### 1. Register a New User
**Endpoint:** `POST /api/auth/register/`

**Request Body:**
```json
{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "SecurePass123!",
    "password2": "SecurePass123!"
}
```

**curl:**
```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "SecurePass123!",
    "password2": "SecurePass123!"
  }'
```

**Expected Response (201):**
```json
{
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "message": "User registered successfully"
}
```

### 2. Login (Get JWT Tokens)
**Endpoint:** `POST /api/auth/login/`

**Request Body:**
```json
{
    "username": "john_doe",
    "password": "SecurePass123!"
}
```

**curl:**
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "SecurePass123!"
  }'
```

**Expected Response (200):**
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

💡 **Save the `access` token** - you'll need it for authenticated requests!

### 3. Refresh Access Token
**Endpoint:** `POST /api/auth/token/refresh/`

**Request Body:**
```json
{
    "refresh": "YOUR_REFRESH_TOKEN"
}
```

**curl:**
```bash
curl -X POST http://localhost:8000/api/auth/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }'
```

---

## Product Endpoints

### 1. List All Products
**Endpoint:** `GET /api/products/`  
**Authentication:** Not required

**curl:**
```bash
curl http://localhost:8000/api/products/
```

**With Filters:**
```bash
# Search for "chocolate" products
curl "http://localhost:8000/api/products/?search=chocolate"

# Filter by category ID 1
curl "http://localhost:8000/api/products/?category=1"

# Sort by price (ascending)
curl "http://localhost:8000/api/products/?ordering=price"

# Sort by price (descending)
curl "http://localhost:8000/api/products/?ordering=-price"

# Combine filters
curl "http://localhost:8000/api/products/?category=1&ordering=-price&search=cake"
```

**Expected Response (200):**
```json
{
    "count": 25,
    "next": "http://localhost:8000/api/products/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Chocolate Croissant",
            "description": "Buttery pastry filled with dark chocolate",
            "price": "4.50",
            "stock_quantity": 50,
            "category": {
                "id": 1,
                "name": "Pastries"
            },
            "image": "http://localhost:8000/media/products/croissant.jpg",
            "created_at": "2026-03-01T10:30:00Z"
        }
    ]
}
```

### 2. Get Product Details
**Endpoint:** `GET /api/products/{id}/`  
**Authentication:** Not required

**curl:**
```bash
curl http://localhost:8000/api/products/1/
```

### 3. Create Product (Admin Only)
**Endpoint:** `POST /api/products/create/`  
**Authentication:** Required (Admin)

**curl:**
```bash
curl -X POST http://localhost:8000/api/products/create/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Vanilla Cupcake",
    "description": "Light and fluffy vanilla cupcake with buttercream frosting",
    "price": "3.25",
    "stock_quantity": 100,
    "category": 2
  }'
```

### 4. Update Product (Admin Only)
**Endpoint:** `PUT/PATCH /api/products/{id}/update/`  
**Authentication:** Required (Admin)

**curl (PATCH - partial update):**
```bash
curl -X PATCH http://localhost:8000/api/products/1/update/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "price": "4.99",
    "stock_quantity": 75
  }'
```

### 5. Delete Product (Admin Only)
**Endpoint:** `DELETE /api/products/{id}/delete/`  
**Authentication:** Required (Admin)

**curl:**
```bash
curl -X DELETE http://localhost:8000/api/products/5/delete/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## Cart Endpoints

### 1. View Cart
**Endpoint:** `GET /api/cart/`  
**Authentication:** Required

**curl:**
```bash
curl http://localhost:8000/api/cart/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Expected Response (200):**
```json
{
    "id": 1,
    "user": "john_doe",
    "items": [
        {
            "id": 1,
            "product": {
                "id": 1,
                "name": "Chocolate Croissant",
                "price": "4.50"
            },
            "quantity": 2,
            "subtotal": "9.00"
        }
    ],
    "total": "9.00"
}
```

### 2. Add Item to Cart
**Endpoint:** `POST /api/cart/add/`  
**Authentication:** Required

**Request Body:**
```json
{
    "product_id": 1,
    "quantity": 2
}
```

**curl:**
```bash
curl -X POST http://localhost:8000/api/cart/add/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "product_id": 1,
    "quantity": 2
  }'
```

### 3. Update Cart Item
**Endpoint:** `POST /api/cart/update/`  
**Authentication:** Required

**Request Body:**
```json
{
    "cart_item_id": 1,
    "quantity": 5
}
```

**curl:**
```bash
curl -X POST http://localhost:8000/api/cart/update/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "cart_item_id": 1,
    "quantity": 5
  }'
```

### 4. Remove Item from Cart
**Endpoint:** `POST /api/cart/remove/`  
**Authentication:** Required

**Request Body:**
```json
{
    "cart_item_id": 1
}
```

**curl:**
```bash
curl -X POST http://localhost:8000/api/cart/remove/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "cart_item_id": 1
  }'
```

---

## Order Endpoints

### 1. Checkout (Create Order)
**Endpoint:** `POST /api/orders/checkout/`  
**Authentication:** Required

**Request Body:**
```json
{
    "payment_method": "mpesa",
    "transaction_id": "MPX123456789"
}
```

**curl:**
```bash
curl -X POST http://localhost:8000/api/orders/checkout/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "payment_method": "mpesa",
    "transaction_id": "MPX123456789"
  }'
```

**Expected Response (201):**
```json
{
    "id": 1,
    "order_number": "ORD-20260301-001",
    "total_price": "9.00",
    "status": "pending",
    "items": [
        {
            "product_name": "Chocolate Croissant",
            "quantity": 2,
            "price": "4.50",
            "subtotal": "9.00"
        }
    ],
    "payment": {
        "method": "mpesa",
        "transaction_id": "MPX123456789",
        "status": "pending"
    },
    "created_at": "2026-03-01T14:30:00Z"
}
```

### 2. View Order History
**Endpoint:** `GET /api/orders/`  
**Authentication:** Required

**curl:**
```bash
curl http://localhost:8000/api/orders/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Expected Response (200):**
```json
{
    "count": 5,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "order_number": "ORD-20260301-001",
            "total_price": "9.00",
            "status": "completed",
            "created_at": "2026-03-01T14:30:00Z"
        }
    ]
}
```

### 3. List All Orders (Admin Only)
**Endpoint:** `GET /api/orders/admin/`  
**Authentication:** Required (Admin)

**curl:**
```bash
curl http://localhost:8000/api/orders/admin/ \
  -H "Authorization: Bearer YOUR_ADMIN_ACCESS_TOKEN"
```

### 4. Update Order Status (Admin Only)
**Endpoint:** `PUT/PATCH /api/orders/admin/{id}/`  
**Authentication:** Required (Admin)

**Request Body:**
```json
{
    "status": "confirmed"
}
```

**curl:**
```bash
curl -X PATCH http://localhost:8000/api/orders/admin/1/ \
  -H "Authorization: Bearer YOUR_ADMIN_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "status": "confirmed"
  }'
```

---

## Common Workflows

### Workflow 1: Complete Shopping Experience

```bash
# Step 1: Register
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"customer1","password":"pass123","password2":"pass123","email":"customer@example.com"}'

# Step 2: Login
TOKEN=$(curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"customer1","password":"pass123"}' | jq -r '.access')

# Step 3: Browse Products
curl http://localhost:8000/api/products/

# Step 4: Add items to cart
curl -X POST http://localhost:8000/api/cart/add/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"product_id":1,"quantity":2}'

# Step 5: View cart
curl http://localhost:8000/api/cart/ \
  -H "Authorization: Bearer $TOKEN"

# Step 6: Checkout
curl -X POST http://localhost:8000/api/orders/checkout/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"payment_method":"mpesa","transaction_id":"MPX123"}'

# Step 7: View orders
curl http://localhost:8000/api/orders/ \
  -H "Authorization: Bearer $TOKEN"
```

---

## Using Postman

### Import Collection

Create a new collection in Postman and add these variables:
- `base_url`: `http://localhost:8000`
- `access_token`: (will be set after login)

### Setup Authorization

1. Go to Collection Settings → Authorization
2. Type: Bearer Token
3. Token: `{{access_token}}`

### Create Requests

Create folders for each endpoint category and add the requests above.

---

## Using Python Requests Library

```python
import requests

BASE_URL = "http://localhost:8000"

# Register
response = requests.post(f"{BASE_URL}/api/auth/register/", json={
    "username": "pythonuser",
    "password": "secure123",
    "password2": "secure123",
    "email": "python@example.com"
})
print(response.json())

# Login
response = requests.post(f"{BASE_URL}/api/auth/login/", json={
    "username": "pythonuser",
    "password": "secure123"
})
token = response.json()["access"]

# Headers for authenticated requests
headers = {
    "Authorization": f"Bearer {token}"
}

# Get products
response = requests.get(f"{BASE_URL}/api/products/")
products = response.json()
print(products)

# Add to cart
response = requests.post(
    f"{BASE_URL}/api/cart/add/",
    headers=headers,
    json={"product_id": 1, "quantity": 2}
)
print(response.json())

# View cart
response = requests.get(f"{BASE_URL}/api/cart/", headers=headers)
print(response.json())

# Checkout
response = requests.post(
    f"{BASE_URL}/api/orders/checkout/",
    headers=headers,
    json={
        "payment_method": "mpesa",
        "transaction_id": "PY123456"
    }
)
print(response.json())
```

---

## Testing Checklist

- [ ] User can register
- [ ] User can login and receive token
- [ ] Token can be refreshed
- [ ] Products can be listed without auth
- [ ] Products can be filtered and searched
- [ ] User can add items to cart
- [ ] User can update cart quantities
- [ ] User can remove cart items
- [ ] User can checkout and create order
- [ ] User can view order history
- [ ] Admin can create/update/delete products
- [ ] Admin can view all orders
- [ ] Admin can update order status

---

## Error Responses

### 400 Bad Request
```json
{
    "error": "Invalid data",
    "details": {
        "password": ["This field is required"]
    }
}
```

### 401 Unauthorized
```json
{
    "detail": "Authentication credentials were not provided."
}
```

### 403 Forbidden
```json
{
    "detail": "You do not have permission to perform this action."
}
```

### 404 Not Found
```json
{
    "detail": "Not found."
}
```

---

**Happy Testing! 🚀**
