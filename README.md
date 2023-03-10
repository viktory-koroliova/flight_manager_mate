# iTravel - Flight manager you need.

Django project for managing flights and crew in Flight Management system.

## Check it out!

[Flight manager project deployed to render.com](https://flight-manager.onrender.com)

## Installation

Python3 must be already installed

```shell
git clone https://github.com/viktory-koroliova/flight_manager_mate
cd flight_manager_mate
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver # starts Django Server
```

## Features

- Authentication for CrewMember/User
- Managing flights, routes, crew and aircraft directly from the website interface
- Powerful admin panel for advanced managing 

## Demo

Use the following command to load prepared data from fixture to get demo access to the system:
  `python manage.py loaddata flight_manager_db_data.json`.

After loading data from fixture you can use following superuser (or create another one by yourself):
  - Login: `admin.user`
  - Password: `admin12345`

![Website interface](demo.png)