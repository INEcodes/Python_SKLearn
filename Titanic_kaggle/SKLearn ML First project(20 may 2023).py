import pandas as pd    
import mysql.connector as msql
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Connect to the database
connection = msql.connect(
    host='localhost',
    user='root',
    password='12345',
    database='titanic'
)

# Read data into a Pandas DataFrame
df = pd.read_sql('SELECT * FROM passenger_data', con=connection)
print(df)
# Prepare the data
X = df[['Survived','Pclass']]
y = df['Sex']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create a logistic regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Close the connection
connection.close()




'''
This is code for the project or task for the kaggle question
Question Task: Titanic - Machine Learning from Disaster
Question Link: https://www.kaggle.com/competitions/titanic
'''