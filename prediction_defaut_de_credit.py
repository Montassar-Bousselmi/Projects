from ucimlrepo import fetch_ucirepo
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import tensorflow as tf
from tensorflow.keras import layers, models

data = fetch_ucirepo(id=350)
X = data.data.features
y = data.data.targets
y = y.squeeze()
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
model = models.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
history = model.fit(X_train, y_train, epochs=30, batch_size=32, validation_split=0.2)
y_pred = (model.predict(X_test) > 0.5).astype("int32")
print(classification_report(y_test, y_pred))

def get_user_input(randomize=True):
    if randomize:
        input_data = [
            np.random.randint(10000, 500000),
            np.random.choice([1, 2]),
            np.random.choice([1, 2, 3, 4]),
            np.random.choice([1, 2, 3]),
            np.random.randint(21, 70),
        ]
        input_data += list(np.random.choice([-2, -1, 0, 1, 2], 6))
        input_data += list(np.random.randint(0, 100000, 6))
        input_data += list(np.random.randint(0, 50000, 6))
    else:
        input_data = []
        input_data.append(int(input("Credit Limit (LIMIT_BAL): ")))
        input_data.append(int(input("Sex (1=Male, 2=Female): ")))
        input_data.append(int(input("Education (1=Grad, 2=University, 3=High school, 4=Others): ")))
        input_data.append(int(input("Marriage (1=Married, 2=Single, 3=Others): ")))
        input_data.append(int(input("Age: ")))
        for i in range(6):
            input_data.append(int(input(f"Repayment status PAY_{i} (-2 to 2): ")))
        for i in range(1, 7):
            input_data.append(int(input(f"Bill Amount Month {i}: ")))
        for i in range(1, 7):
            input_data.append(int(input(f"Payment Amount Month {i}: ")))
    return np.array(input_data).reshape(1, -1)

def predict_default(model, scaler, input_data):
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0][0]
    print(f"\n🔍 Predicted Probability of Default: {prediction:.2f}")
    if prediction > 0.5:
        print("❌ HIGH RISK of default!")
    else:
        print("✅ LOW RISK of default.")

randomize = input("Do you want to generate random values? (y/n): ").lower() == 'y'
user_input = get_user_input(randomize)
print(user_input)
predict_default(model, scaler, user_input)