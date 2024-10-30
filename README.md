# aban Task API

This is a Django-based API for purchasing cryptocurrency from an exchange. It supports creating and aggregating user purchase orders and includes Docker configuration for easy setup.

## Features

- Allows users to purchase cryptocurrency based on a specified amount and cryptocurrency name.
- Deducts funds from user accounts based on cryptocurrency prices.
- Aggregates small orders (less than $10) into a single larger order to reduce exchange transaction costs.
- Built with Django and Django REST framework (DRF).
- Uses MySQL for database storage.
- Contains tests for service and API functionalities using pytest.

## Requirements

- Python 3.9 or higher
- Docker and Docker Compose
- MySQL

## Project Structure

```plaintext
abanTask/
├── abanTask/         # Django project settings
├── orders/                  # Main app for managing cryptocurrency orders
│   ├── migrations/          # Database migrations for orders app
│   ├── models.py            # Database models (User, Order, Cryptocurrency)
│   ├── services.py          # Order handling logic, including aggregation
│   ├── views.py             # API view for handling purchase requests
│   └── tests.py             # Test cases for models, services, and API
├── manage.py                # Django management script
├── Dockerfile               # Docker configuration for Django app
├── docker-compose.yml       # Docker Compose configuration for app and database
└── requirements.txt         # Python dependencies
