import os


# Database credentials
DB_TYPE = 'sqlite'
DB_TYPE = os.environ.get('DB_TYPE', DB_TYPE)
DB_HOST = 'localhost'
DB_HOST = os.environ.get('DB_HOST', DB_HOST)
DB_PORT = 5432
DB_PORT = os.environ.get('DB_PORT', DB_PORT)
DB_USER = 'pik'
DB_USER = os.environ.get('DB_USER', DB_USER)
DB_PASSWORD = '123'
DB_PASSWORD = os.environ.get('DB_PASSWORD', DB_PASSWORD)
DB_NAME = 'volunteers.db'
DB_NAME = os.environ.get('DB_NAME', DB_NAME)

# Server credentials
SERVER_HOST = 'localhost'
SERVER_HOST = os.environ.get('SERVER_HOST', SERVER_HOST)
SERVER_PORT = 5000
SERVER_PORT = os.environ.get('SERVER_PORT', SERVER_PORT)
