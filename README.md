# iTravel - Flight manager you need.


Imagine that you are a flight manager for an airline. Your company has its own fleet and crew, as well as a list of routes to frequent and popular destinations. 

This application will help you to keep track of future flights, change them and remove them from the schedule, as well as add and update information about your aircraft, routes and crew. 

Unregistered users of the site have access to general information about the airline, as well as a page with contact details. 

Registered users get access to manage their flights.

Use the following command to load prepared data from fixture to get demo access to the system:
  `python manage.py loaddata flight_manager_db_data.json`.
- After loading data from fixture you can use following superuser (or create another one by yourself):
  - Login: `admin`
  - Password: `admin12345`