import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv(r"D:\DS_AI_Internship\src\day14_feature_eng\housing.csv")

print("Dataset Columns : ")
print(df.columns)

# Select feature and target
X = df[['Area']]
y = df['Price']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------
# Linear Regression
# -----------------------
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

y_pred_linear = linear_model.predict(X_test)

r2_linear = r2_score(y_test, y_pred_linear)

print("\nLinear Regression Result")
print("R^2 score (Linear Features):", r2_linear)

# -----------------------
# Polynomial Features
# -----------------------
poly = PolynomialFeatures(degree=2)

X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

y_pred_poly = poly_model.predict(X_test_poly)

r2_poly = r2_score(y_test, y_pred_poly)

print("\nPolynomial Regression Result")
print("R^2 score (Polynomial Features):", r2_poly)

# -----------------------
# Comparison
# -----------------------
print("\nComparison")

if r2_poly > r2_linear:
    print("Polynomial features improved the model.")
else:
    print("Polynomial features did NOT improve the model.")

print("\nImprovement:", r2_poly - r2_linear)
