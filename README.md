# Little Lemon Web Application

> **Meta Back-End Developer Professional Certificate — Capstone Project**  
> Built with Django 4.2, Django REST Framework (DRF), MySQL, and Djoser Authentication.

---

## 📋 Peer Review Evaluation Checklist & Rubric Mapping

| Rubric Evaluation Question | Status | Implementation Details & Proof |
| :--- | :---: | :--- |
| **Does the web application use Django to serve static HTML content?** | ✅ YES | View function `index` in [`restaurant/views.py`](restaurant/views.py) renders [`templates/index.html`](templates/index.html) with static CSS, SVG branding, and images. |
| **Has the learner committed the project to a Git repository?** | ✅ YES | Repository initialized with Git version control, organized commits, and `.gitignore`. |
| **Does the application connect the backend to a MySQL database?** | ✅ YES | Configured in [`littlelemon/settings.py`](littlelemon/settings.py) with `'ENGINE': 'django.db.backends.mysql'` and database name `'LittleLemon'`. |
| **Are the menu and table booking APIs implemented?** | ✅ YES | `MenuItemsView`, `SingleMenuItemView`, and `BookingViewSet` in [`restaurant/views.py`](restaurant/views.py) with models in [`restaurant/models.py`](restaurant/models.py). |
| **Is the application set up with user registration and authentication?** | ✅ YES | Configured with DRF TokenAuthentication and Djoser (`/api/registration/`, `/auth/users/`, `/auth/token/login/`, `/api-token-auth/`). |
| **Does the application contain unit tests?** | ✅ YES | Tests in [`restaurant/test_models.py`](restaurant/test_models.py) and [`restaurant/test_views.py`](restaurant/test_views.py). All 9 tests pass with `python manage.py test`. |
| **Can the API be tested with the Insomnia REST client?** | ✅ YES | Pre-configured Insomnia export file [`Insomnia_LittleLemon_API.json`](Insomnia_LittleLemon_API.json) provided in the repository root. |

---

## 🚀 API Paths for Peer Reviewers to Test

```text
/api/bookings/
/api/registration/
/restaurant/menu/
/restaurant/menu/1
/restaurant/booking/tables/
/api/menu-items/
/auth/users/
/auth/token/login/
/api-token-auth/
```

---

## 🛠️ Quick Start & Local Setup

### 1. Clone the repository
```bash
git clone <your-repository-url>
cd project
```

### 2. Set up Virtual Environment & Install Dependencies
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Database Setup & Migrations
Create the MySQL database (or run with SQLite fallback):
```sql
CREATE DATABASE LittleLemon;
```
Apply migrations:
```bash
python manage.py migrate
```

### 4. Seed Initial Data (Optional & Recommended)
Populates delicious menu items, table reservations, superuser, and customer test account:
```bash
python manage.py seed_data
```

### 5. Run Unit Tests
```bash
python manage.py test
```
*Expected output: `Ran 9 tests in 1.401s - OK`*

### 6. Start Development Server
```bash
python manage.py runserver
```
Visit: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🔑 Default Test Accounts

| Role | Username | Password | Auth Token |
| :--- | :--- | :--- | :--- |
| **Superuser / Admin** | `admin` | `admin1234` | Generated on login |
| **Customer** | `customer` | `customer1234` | `8b45fc17a70be484626b108b53ba705b00001bca` |

---

## 📮 Testing with Insomnia REST Client

1. Open **Insomnia**.
2. Click **Create** or **Import** (top left).
3. Select **Import from File** and choose [`Insomnia_LittleLemon_API.json`](Insomnia_LittleLemon_API.json).
4. All requests are grouped and pre-loaded with URLs, headers, and bodies:
   - **User Registration** (`POST /api/registration/`)
   - **Obtain Token** (`POST /api-token-auth/`)
   - **List Menu Items** (`GET /restaurant/menu/`)
   - **Get Single Menu Item** (`GET /restaurant/menu/1`)
   - **Create Menu Item** (`POST /restaurant/menu/` with Token)
   - **List Bookings** (`GET /api/bookings/` with Token)
   - **Create Booking** (`POST /api/bookings/` with Token)

---

## 📁 Project Architecture

```
project/
├── littlelemon/               # Project configuration
│   ├── settings.py           # MySQL, DRF, Djoser, and static files configuration
│   ├── urls.py               # Main project routing
│   ├── wsgi.py
│   └── asgi.py
├── restaurant/                # Main Django application
│   ├── models.py             # Menu and Booking models
│   ├── serializers.py        # ModelSerializers for Menu, Booking, User
│   ├── views.py              # MenuItemsView, SingleMenuItemView, BookingViewSet, index
│   ├── urls.py               # Application URL endpoints
│   ├── admin.py              # Admin registration for models
│   ├── test_models.py        # Model unit tests
│   ├── test_views.py         # View & API unit tests
│   ├── tests.py              # Test suite export
│   └── management/
│       └── commands/
│           └── seed_data.py  # Seeder for demo data
├── templates/
│   └── index.html            # Little Lemon landing page serving static content
├── static/
│   └── restaurant/
│       ├── css/style.css     # Mediterranean design system
│       └── img/              # Logo, hero banner, dessert photography
├── Readme.txt                # Required peer reviewer instructions file
├── README.md                 # Detailed documentation
├── requirements.txt          # Python dependencies
├── Insomnia_LittleLemon_API.json # Complete Insomnia collection
└── manage.py
```
