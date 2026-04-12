import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

data = pd.DataFrame({
    "traffic": [1,2,3,1,2,3],
    "severity": [30,60,90,40,70,95]
})

X = data[['traffic']]
y = data['severity']

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, "models/model.pkl")

print("Model trained!")