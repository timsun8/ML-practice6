from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import joblib

iris = load_iris()
X = iris.data
y = iris.target

model = LogisticRegression(max_iter=200)
model.fit(X, y)

joblib.dump(model, "model.joblib")

print("Model trained and saved as model.joblib")