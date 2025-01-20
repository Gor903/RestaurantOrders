# Restaurant Orders
A simple Django application for managing restaurant orders. This project allows workers to view the coffee menu, place orders, and manage their profiles. The owner can also manage orders, including updating the order status and viewing customer details.

## Features
 - Menu Management: Admins can add, update, or delete items from the menu.
 - Order Management: Workers can place orders, view orders, and track their status.
 - Owner Order Management: The owner (admin) can view all orders, update the status of each order (Pending, Ready, Paid), and manage customer orders in the admin panel.

## Prerequisites
 - Linux
 - Python
 - PostgreSQL

## Installation
### 1.Clone the repository
```bash
    git clone https://github.com/Gor903/RestaurantOrders.git
    cd RestaurantOrders
```

### 2. Create a virtual environment 
```bash
    python -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
```

### 3. Configuration
Set up the database and create .env file following the .env.example

### 4. Run migrations
```bash
    python manage.py migrate
```

### 5. Create super user
Create super user to have an access to admin panel.
Run:
```bash
    python manage.py createsuperuser
```
and follow the prompts.

### 6. Run the development server
```bash
    python manage.py runserver
```

### 7. Access the admin panel
Go to http://localhost:8000/admin to access the Django admin panel. Log in with the superuser account you created earlier. From here, the owner can most part of data.


## Useful links
 - **Swagger**: http://localhost:8000/swagger/
 - **Orders**: http://localhost:8000/orders/
 - **Create order**: http://localhost:8000/orders/
 - **Manage order**: http://localhost:8000/orders/{uuid}/
 - **Report**: http://localhost:8000/report/

## You can find in swagger page:
 - Order create
 - Order update (patch)
 - Order delete
 - Order List
 - Order detail

### Run Unittests
```bash
    python manage.py test
```
