Web Application for EasyStarter Crowdfunding Platform Project

1. Install and configure VirtualEnv:
    sudo apt-get install virtualenv 
    mkdir ~/virtualenvironment
    virtualenv --no-site-packages ~/virtualenvironment/my_new_app
    cd ~/virtualenvironment/my_new_app/bin
    source activate

2. Clone git repository:
    mkdir EasyStarterProject && cd EasyStarterProject
    git clone https://github.com/easystarter/easystarter_web_application.git
    cd easystarter_web_application/ 
    pip install -r /path/to/requirements.txt

3. PostgreSQL
Installation:
    sudo apt-get update
    sudo apt-get install postgresql postgresql-contrib

Create a Database and Database User:
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
