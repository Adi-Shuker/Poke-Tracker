import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    db="poke_tracker",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

if connection.open:
    print("the connection is opened")
