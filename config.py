import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

# Give access to the project in ANY as we find ourselves in
# Allow outside files/folders to be added to the project from the base directory

load_dotenv(os.path.join(basedir, '.env'))

class Config():
    """
        Set config variables for the flask app
        using environment variables where available other
        create the config variables if not already not
    
    """
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess this, yoink'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #Turn off database updates from sqlalchemy