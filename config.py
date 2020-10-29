import os

def get_postgres_uri():
    host = os.environ.get('DB_HOST', 'localhost')
    port = 54321 if host == 'localhost' else 5432
    password = os.environ.get('DB_PASSWORD', 'admin')
    user, db_name = 'virajment', 'virajment'
    return f"postgres://{user}:{password}@{host}:{port}/{db_name}"
