import mysql.connector

class DatabaseController():
    def __init__(self, config):
        self.mydb = mysql.connector.connect(**config)
        self.mycursor = self.mydb.cursor()

    def sign_up(self, username, password):
        qry = "INSERT INTO Users (username, password) VALUES (%s, %s)"
        self.mycursor.execute(qry, (username, password))
        self.mydb.commit()
        return