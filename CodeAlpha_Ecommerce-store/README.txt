# CodeAlpha Ecommerce Store

A simple e-commerce web application built with Django, Bootstrap, and SQLite. This project demonstrates fundamental e-commerce features including product listings, detail pages, shopping cart, checkout, and user authentication.

---

## Features

* **Product Catalog**: Browse a grid of products with images, names, descriptions, and prices.
* **Product Details**: View individual product information and add items to your cart.
* **Shopping Cart**: Add, view, and manage items in a session-based cart.
* **Checkout**: Simple order completion page (orders are cleared after checkout).
* **User Authentication**: Sign up, log in, and log out via Django’s built-in auth system.
* **Admin Dashboard**: Manage products, orders, and order items through Django’s admin interface.
* **Sample Data**: Preloaded fixtures with 5 example products.

---

## Project Structure

```
CodeAlpha_Ecommerce-store/
├── config/                # Django project settings and URLs
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── store/                 # Main application
│   ├── admin.py
│   ├── apps.py
│   ├── models.py          # Product, Order, OrderItem models
│   ├── views.py           # Product list, detail, cart, checkout, signup
│   ├── urls.py
│   ├── fixtures/          # Sample product data
│   ├── migrations/        # Auto‑generated migrations
│   ├── static/css/site.css# Basic custom styling
│   └── templates/
│       ├── registration/  # login/logout templates
│       └── store/         # base, product_list, detail, cart, checkout, signup
├── db.sqlite3             # SQLite database file
├── manage.py              # Django management script
└── README.md
```

---

## Prerequisites

* Python 3.8 or newer
* Git (for version control)

---

## Setup and Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/CodeAlpha_Ecommerce-store.git
   cd CodeAlpha_Ecommerce-store
   ```

2. **Create and activate a virtual environment**

   On Windows (Command Prompt):

   ```cmd
   python -m venv env
   env\Scripts\activate
   ```

   On macOS/Linux:

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install django Pillow
   ```

4. **Create database migrations**

   ```bash
   python manage.py makemigrations store
   python manage.py migrate
   ```

5. **Load sample data**

   ```bash
   python manage.py loaddata store/fixtures/products.json
   ```

6. **Create a superuser (optional, for admin access)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

8. **Access the application**

   * Frontend: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   * Admin Dashboard: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Usage

* Browse products on the homepage.
* Click **Sign Up** or **Login** (top nav) to register or authenticate.
* Add products to your cart and proceed to checkout.
* In the admin dashboard, log in with your superuser credentials to manage products and orders.

---

## Customization

* Add or modify products via Django Admin or by editing `store/fixtures/products.json` and reloading.
* Extend styling in `store/static/css/site.css` or integrate additional frontend frameworks.
* Implement payment integration by connecting a payment gateway in the `checkout` view.

---

## License

This project is open-source and available under the MIT License. Feel free to fork and adapt it for your own use.
