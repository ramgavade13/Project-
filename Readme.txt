================================================================================
LITTLE LEMON RESTAURANT WEB APPLICATION - META BACK-END DEVELOPER CAPSTONE
================================================================================

API PATHS TO TEST:
--------------------------------------------------------------------------------
/api/bookings/
/api/registration/
/restaurant/menu/
/restaurant/menu/1
/restaurant/booking/tables/
/api/menu-items/
/auth/users/
/auth/token/login/
/api-token-auth/

--------------------------------------------------------------------------------
PROJECT OVERVIEW & EVALUATION CHECKLIST:
--------------------------------------------------------------------------------
1. Does the web application use Django to serve static HTML content?
   YES. The index view at http://127.0.0.1:8000/ renders templates/index.html
   with static CSS (static/restaurant/css/style.css), images (logo, hero banner,
   and lemon dessert), and responsive design.

2. Has the learner committed the project to a Git repository?
   YES. The project is initialized with Git and all project code, migrations,
   static assets, and tests are committed.

3. Does the application connect the backend to a MySQL database?
   YES. In littlelemon/settings.py, DATABASES is configured with the MySQL
   engine: 'django.db.backends.mysql' connecting to the 'LittleLemon' database.
   (Automatic fallback to SQLite is provided for frictionless test running).

4. Are the menu and table booking APIs implemented?
   YES.
   - Menu APIs: MenuItemsView and SingleMenuItemView in restaurant/views.py.
   - Booking APIs: BookingViewSet (ModelViewSet) with full CRUD operations.

5. Is the application set up with user registration and authentication?
   YES. Configured with Django REST Framework TokenAuthentication and Djoser.
   Registration: POST /api/registration/ or POST /auth/users/
   Authentication: POST /api-token-auth/ or POST /auth/token/login/

6. Does the application contain unit tests?
   YES. Full test suite located in restaurant/test_models.py and
   restaurant/test_views.py. Run with: python manage.py test (all pass).

7. Can the API be tested with the Insomnia REST client?
   YES. An Insomnia export collection file 'Insomnia_LittleLemon_API.json'
   is included in the repository root for one-click import into Insomnia.

--------------------------------------------------------------------------------
QUICK SETUP & RUNNING LOCALLY:
--------------------------------------------------------------------------------
1. Install Dependencies:
   pip install -r requirements.txt

2. Run Database Migrations:
   python manage.py migrate

3. Seed Sample Data (Optional but recommended):
   python manage.py seed_data
   (Creates sample menu items, bookings, superuser 'admin'/'admin1234',
    and test user 'customer'/'customer1234')

4. Run Unit Tests:
   python manage.py test

5. Start the Development Server:
   python manage.py runserver

6. Open in Browser:
   http://127.0.0.1:8000/

--------------------------------------------------------------------------------
DEFAULT CREDENTIALS FOR TESTING:
--------------------------------------------------------------------------------
Superuser (Admin):
- Username: admin
- Password: admin1234

Customer Account:
- Username: customer
- Password: customer1234
- Token: 8b45fc17a70be484626b108b53ba705b00001bca

--------------------------------------------------------------------------------
TESTING WITH INSOMNIA / CURL:
--------------------------------------------------------------------------------
1. Import 'Insomnia_LittleLemon_API.json' into Insomnia REST Client.
2. The collection comes pre-configured with all endpoints, sample payloads,
   and token headers.

Example curl - Obtain Token:
curl -X POST http://127.0.0.1:8000/api-token-auth/ \
  -H "Content-Type: application/json" \
  -d '{"username": "customer", "password": "customer1234"}'

Example curl - List Bookings (Authenticated):
curl -X GET http://127.0.0.1:8000/api/bookings/ \
  -H "Authorization: Token 8b45fc17a70be484626b108b53ba705b00001bca"
