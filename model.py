# loading dataset
import pandas as pd
data=pd.read_csv("salary.csv")
print("Dataset has been loaded ..")

# Creating features and target.
feature=data["YearsExperience"].values.reshape(30,1)
target=data["Salary"]

# loading LinearRegression
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(feature,target)
print("Model has been created ...")

# Now, our model has been trained

#predict
exp=int(input("Enter years of experience: "))
pred=model.predict([[exp]])
print("Expected Salary is ",round(pred[0],2)," INR.")