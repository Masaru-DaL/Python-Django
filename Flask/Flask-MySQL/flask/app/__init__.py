import os
import sqlalchemy
import pymysql
from flask import Flask
from yaml import load, Loader

def init_connect_engine():
    if os.environ.get('GAE_ENV') != 'standard':
        variables = load(open("app.yaml"), Loader=Loader)
        env_variables = variables['env_variables']
        for var in env_variables:
            os.environ[var] = env_variables[var]

    pool = sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL(
                drivername="mysql+pymysql",
                username=os.environ.get('MYSQL_USER'), #username
                password=os.environ.get('MYSQL_PASSWORD'), #user password
                database=os.environ.get('MYSQL_DB'), #database name
                host=os.environ.get('MYSQL_HOST') #ip
            )
        )
    return pool

app = Flask(__name__)
db = init_connect_engine()



from app import routes
