import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Dsposa1er'

)

# prepare cursor object
cursorObject = dataBase.cursor()

# create a database

cursorObject.execute("CREATE DATABASE techstock ")

print("All done!")