# Inventory-Pro
# InventoryPro

InventoryPro is a web-based platform designed to make inventory management simple, efficient, and scalable for businesses. Whether it’s tracking stock, managing suppliers, or empowering wholesalers, InventoryPro provides the tools to streamline it all.

## Features

### For Admins:

- Add, update, and track products with details such as SKU, stock levels, wholesale/retail prices, and reorder thresholds.
- Manage accounts and permissions for wholesalers and suppliers.

### For Wholesalers:

- Browse a product catalog with wholesale pricing.
- Add multiple products to the cart and place bulk orders seamlessly.
- Register and log in securely using email-based authentication.

### For Suppliers:

- Track and manage supplier details, including contact information and associated products.

## Tech Stack

### Frontend

- Built using an Envato template.
- JavaScript for consuming REST APIs.

### Backend

- **Django**: Powered by Django's robust framework.
- **Django REST Framework (DRF)**: Used for creating efficient REST APIs using DRF Serializers and Filters.
- Multi-language support enabled via Django's internationalization (i18n) framework.

### Authentication

- Admin and wholesaler authentication implemented using custom decorators.
- Secured views using Django’s built-in `LoginRequiredMixin`.
- Email-based registration and login for secure user access.

## Development Approach

- Leveraged Django’s class-based views (e.g., `ListView`, `DetailView`, `CreateView`) to ensure reusability, maintainability, and clean code.

## Installation

Follow these steps to set up the project on your local machine:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/inventorypro.git
   cd inventorypro
   ```

2. Set up a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Apply database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

5. Access the application in your browser at `http://127.0.0.1:8000/`.

## Dependencies

The following packages and libraries are used in this project:

- `asgiref==3.8.1`
- `Django==5.1.4`
- `django-filter==24.3`
- `djangorestframework==3.15.2`
- `pillow==11.0.0`
- `six==1.17.0`
- `sqlparse==0.5.3`

## Usage

1. **Admins** can log in to manage products, suppliers, and wholesalers.
2. **Wholesalers** can register, log in, and place bulk orders.
3. **Suppliers** can view and manage their product information.

## Future Development

### Analytics and Reporting

- Generate reports for:
  - Monthly stock trends.
  - Top-selling products.
  - Inventory valuation (current stock value).
- Visualize data using charts (e.g., bar charts, line graphs).

### Barcode Integration

- Use barcode scanners to:
  - Add new stock.
  - Update stock levels during sales or stock intake.

### Multi-Warehouse Support

- Track inventory across multiple locations.
- Allow users to transfer stock between warehouses.

## Contribution

We welcome contributions to enhance InventoryPro. If you'd like to contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add a meaningful commit message"
   ```
4. Push to your fork and create a pull request.

## Contact

For questions or support, please contact:

- **Ali Muhammad**
- Email: [alimuhammad3003@gmail.com](mailto\:alimuhammad3003@gmail.com)
- GitHub: [aliPythonDeveloper](https://github.com/aliPythonDeveloper)

