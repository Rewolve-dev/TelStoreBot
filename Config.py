import os
config = {'user': f"{os.environ.get('DATABASEUNAME')}", 'password': f"{os.environ.get('DATABASEPASS')}", 'host': f"{os.environ.get('DATABASEHOST')}", 'database': f"{os.environ.get('DATABASE')}"}
DATABASE = os.environ.get("DATABASE")

