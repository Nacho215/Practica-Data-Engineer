# Imports
from decouple import config

# Get .env variables
host = config('MYSQL_HOST')
user = config('MYSQL_USER')
password = config('MYSQL_PASSWORD')
db = config('MYSQL_DB')

# Print them all
print(f'Host: {host}')
print(f'User: {user}')
print(f'Password: {password}')
print(f'Database: {db}')
