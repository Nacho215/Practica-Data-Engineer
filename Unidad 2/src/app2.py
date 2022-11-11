# Imports
from dotenv import load_dotenv, find_dotenv
import os

# Find and load dotenv file
load_dotenv(find_dotenv())

# Get .env variables
host = os.getenv('MYSQL_HOST')
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
db = os.getenv('MYSQL_DB')

# Print them all
print(f'Host: {host}')
print(f'User: {user}')
print(f'Password: {password}')
print(f'Database: {db}')
