import numpy as np
import pandas as pd
import mysql.connector as msql
from mysql.connector import Error

titanicdata = pd.read_csv("D:/Coding/datasets/Titanic survival/train.csv", index_col=False, delimiter=',')

# Handle missing values appropriately (replace '-' with np.nan)
titanicdata['Cabin'] = titanicdata['Cabin'].replace(np.nan, '')
titanicdata['Age'] = titanicdata['Age'].replace(np.nan, np.nan)
titanicdata['Embarked'] = titanicdata['Embarked'].replace(np.nan, '')

# Create a connection to MySQL
try:
    conn = msql.connect(host='localhost', database='titanic', user='root', password='12345')
    cur = conn.cursor()

    # Create the table with appropriate data types
    cur.execute("""
        CREATE TABLE IF NOT EXISTS passenger_data (
            PassengerId INT,
            Survived INT,
            Pclass INT,
            Name VARCHAR(255),
            Sex VARCHAR(10),
            Age FLOAT,
            SibSp INT,
            Parch INT,
            Ticket VARCHAR(255),
            Fare FLOAT,
            Cabin VARCHAR(255),
            Embarked VARCHAR(1)
        )
    """)
    print("Table is created....")

    # Loop through the data frame and insert records into the MySQL table
    for i, row in titanicdata.iterrows():
        sql = """
            INSERT INTO passenger_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        cur.execute(sql, tuple(row))
        print("Record inserted")

    # Commit the changes
    conn.commit()

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    # Close the connection
    if conn.is_connected():
        cur.close()
        conn.close()
        print("MySQL connection is closed")
