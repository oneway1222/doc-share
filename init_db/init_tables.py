"""
This file file contains all the queries for creating tables
To initialize database, please run 'run.py'
"""
def init(mycursor):
    mycursor.execute(
        """CREATE TABLE Users(
            username  VARCHAR(20) PRIMARY KEY,
            password  VARCHAR(20) NOT NULL,
            email     VARCHAR(20),
            firstName VARCHAR(20),
            lastName  VARCHAR(20)
        );"""
    )

    mycursor.execute("INSERT INTO Users(username, password) VALUES ('xin', 'xin');")
