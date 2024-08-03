import MySQLdb

# Connect to MySQL
dataBase = MySQLdb.connect(
    host='localhost',
    user='caroline',
    password='Carolinetgn94!'
)

cursorObject = dataBase.cursor()

# Check if database exists
cursorObject.execute("SHOW DATABASES LIKE 'Caro'")
result = cursorObject.fetchone()

if not result:
    cursorObject.execute("CREATE DATABASE Caro")
    print("Database 'Caro' created.")
else:
    print("Database 'Caro' already exists.")

dataBase.close()
