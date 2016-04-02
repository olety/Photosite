## Installation

1. Install the following apps:
    * `python` (2.7)
    * `python-pip`
    * `python-virtualenv`
    * `postgresql-server-dev-X.Y` (9.3)
2. `git clone` this project
3. `cd Photosite`
4. `virtualenv venv`
5. _(if you plan to contribute)_ Edit your global `.gitignore` and add `venv/` in it.
6. `source venv/bin/activate`
7. `pip install -r requirements.txt`
    * you may need to issue `pip install --upgrade setuptools`
8. Set up your PostgreSQL database (you can use `pgadmin3`)
    * database details are in `Photosite/settings.py`
9. `./manage.py migrate`
10. `./manage.py runserver`