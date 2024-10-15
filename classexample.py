import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv('student-mat.csv', encoding='ISO-8859-1') 

print(df)

df.columns = ['hours', 'score']
X = df[['hours']]  # Feature: hours learned
y = df['score']  # Target: exam score

# Split the dataset into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Evaluate the model by calculating Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Display the intercept and slope (coefficient)
print("Intercept (beta0):", model.intercept_)
print("Slope (beta1):", model.coef_)


# Predict the score for a student who studied 7 hours
hours_studied = pd.DataFrame([[12]],columns=["hours"]) 
predicted_score = model.predict(hours_studied)
print(f"Predicted score for the entered hours of study: {predicted_score[0]:.2f}")



# Coefficients and intercept from your model
intercept = model.intercept_
coefficient = model.coef_



with open('predicted_scores.txt', 'a') as f:
    f.write(f"Hours Studied: {hours_studied['hours'].iloc[0]}, Predicted Score: {predicted_score[0]:.2f}\n")

print("Results saved to predicted_scores.txt")
