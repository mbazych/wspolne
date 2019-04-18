import mysql.connector


def conn():
    try:
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd=""
          )
        cur = mydb.cursor()

    except ConnectionError:
        print("BŁĄD")
