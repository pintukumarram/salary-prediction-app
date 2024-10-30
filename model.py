import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# load dataset

df = pd.read_csv("salary_predict.csv")

# Separate features and target
X = df[['experience']]
y = df['salary']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Function to make predictions
def predict_salary(experience):
    years_of_experience = np.array([[experience]])
    return model.predict(years_of_experience)[0]
