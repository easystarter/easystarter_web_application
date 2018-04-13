# Web Application for EasyStarter Crowdfunding Platform Project

#### Install and configure VirtualEnv:

```
sudo apt-get install virtualenv
mkdir ~/virtualenvironment
virtualenv --no-site-packages ~/virtualenvironment/my_new_app
cd ~/virtualenvironment/my_new_app/bin
source activate
```
#### Clone git repository:
```
mkdir EasyStarterProject && cd EasyStarterProject
git clone https://github.com/easystarter/easystarter_web_application.git
cd easystarter_web_application/
pip install -r /path/to/requirements.txt
```

## PostgreSQL:

#### Installation:
```
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
```

#### Create a Database and Database User:

```
sudo su - postgres
psql
CREATE DATABASE myproject;
CREATE USER myprojectuser WITH PASSWORD 'password';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
\q
exit
```
#### Install psycopg2
```
(myvenv)$ pip install psycopg2
```
#### Configure the Django Database Settings

Now that we have a project, we need to configure it to use the database we created.
Open the main Django project settings file located within the child project directory.

Towards the bottom of the file, you will see a DATABASES section that looks like this:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

This is currently configured to use SQLite as a database. We need to change this so that our PostgreSQL database is used instead.

First, change the engine so that it uses the postgresql_psycopg2 adaptor instead of the sqlite3 adaptor. For the NAME, use the name of your database (myproject in our example). We also need to add login credentials. We need the username, password, and host to connect to. We'll add and leave blank the port option so that the default is selected:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
#### Migrate the Database and Test your Project
Now that the Django settings are configured, we can migrate our data structures to our database and test out the server.
We can begin by creating and applying migrations to our database. Since we don't have any actual data yet, this will simply set up the initial database structure:
```
cd ~/myproject
python manage.py makemigrations
python manage.py migrate
```
After creating the database structure, we can create an administrative account by typing:
```
python manage.py createsuperuser
```
You will be asked to select a username, provide an email address, and choose and confirm a password for the account.
You can test that your database is performing correctly by starting up the Django development server:
```
python manage.py runserver
```
In your web browser, visit your server's domain name or IP address followed by :8000 to reach default Django root page:
```
http://server_domain_or_IP:8000
```