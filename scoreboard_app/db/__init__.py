
import os
from dotenv import load_dotenv
'''
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))  # Load environment variables from .env file
url = os.getenv('API_URL')
port = os.getenv('API_PORT')
protocol = os.getenv('API_PROTOCOL')'''
API_URL = 'http://192.168.0.43:5000'

#API_URL = f'{protocol}://{url}:{port}'  # API URL