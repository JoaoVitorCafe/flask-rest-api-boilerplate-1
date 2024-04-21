import os
from dotenv import load_dotenv
from sqlalchemy import URL

# Set base directory of the app
basedir = os.path.abspath(os.path.dirname(__file__))

# Load the .env and .flaskenv variables
load_dotenv(os.path.join(basedir, ".env"))

class Config(object):
    """
    Set the config variables for the Flask app
    """
        
    SECRET_KEY = os.environ.get("SECRET_KEY")

    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    DB_DRIVER = os.getenv('DB_DRIVER')

    connection_string = f"DRIVER={DB_DRIVER};SERVER={DB_HOST};DATABASE={DB_NAME};UID={DB_USERNAME};PWD={DB_PASSWORD};TrustServerCertificate=yes;"
    connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})

    SQLALCHEMY_DATABASE_URI = connection_url

    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get(
        "SQLALCHEMY_TRACK_MODIFICATIONS"
    )