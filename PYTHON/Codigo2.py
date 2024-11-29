import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Datos históricos de demanda (hora del día, temperatura, ventas pasadas)
# Ejemplo: (hora, temperatura, ventas) -> demanda
X = np.array([[8, 25, 50],  # 8 AM, 25°C, 50 ventas pasadas
              [12, 30, 100], # 12 PM, 30°C, 100 ventas pasadas
              [18, 20, 80],  # 6 PM, 20°C, 80 ventas pasadas
              [22, 15, 30]]) # 10 PM, 15°C, 30 ventas pasadas

y = np.array([60, 120, 100, 50])  # Demanda observada

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X, y)

# Predecir la demanda para un nuevo conjunto de datos (por ejemplo, 5 PM, 25°C, 90 ventas pasadas)
new_data = np.array([[17, 25, 90]])
predicted_demand = model.predict(new_data)

print(f"Predicción de la demanda: {predicted_demand[0]}")
