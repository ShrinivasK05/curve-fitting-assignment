# ==============================================================
#  Curve Fitting Assignment
#  Author: [Your Name]
#  Repository: curve-fitting-assignment
# --------------------------------------------------------------
#  Fits given (x, y) data to the parametric equations:
#
#  x = t*cos(θ) - e^(M|t|)*sin(0.3t)*sin(θ) + X
#  y = 42 + t*sin(θ) + e^(M|t|)*sin(0.3t)*cos(θ)
#
#  Optimizes θ, M, X using SciPy to minimize L1 distance.
# ==============================================================

import numpy as np
import pandas as pd
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# ==============================================================
#  Load Data
# ==============================================================
data = pd.read_csv("xy_data.csv")
print("✅ Data loaded successfully!")
print(f"Number of points: {len(data)}")
print(data.head())

# ==============================================================
#  Parametric Equations
# ==============================================================
def parametric_curve(t, theta, M, X):
    x = t * np.cos(theta) - np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.sin(theta) + X
    y = 42 + t * np.sin(theta) + np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.cos(theta)
    return x, y

# ==============================================================
#  Objective Function (L1 Loss)
# ==============================================================
t_values = np.linspace(6, 60, len(data))

def objective(params):
    theta, M, X = params
    x_pred, y_pred = parametric_curve(t_values, theta, M, X)
    L1 = np.mean(np.abs(data["x"] - x_pred) + np.abs(data["y"] - y_pred))
    return L1

# ==============================================================
#  Optimization Setup
# ==============================================================
initial_guess = [np.deg2rad(25), 0, 50]
bounds = [(np.deg2rad(0), np.deg2rad(50)), (-0.05, 0.05), (0, 100)]

print("\n🚀 Running optimization...")
result = minimize(objective, initial_guess, bounds=bounds, method="L-BFGS-B")

theta_opt, M_opt, X_opt = result.x

print("\n✅ Optimization Complete!")
print(f"Theta = {theta_opt:.5f} rad = {np.degrees(theta_opt):.2f}°")
print(f"M = {M_opt:.5f}")
print(f"X = {X_opt:.2f}")
print(f"L1 Loss = {result.fun:.4f}")

# ==============================================================
#  Visualization
# ==============================================================
x_pred, y_pred = parametric_curve(t_values, theta_opt, M_opt, X_opt)

plt.figure(figsize=(8,6))
plt.scatter(data["x"], data["y"], s=10, color="blue", alpha=0.6, label="Data Points")
plt.plot(x_pred, y_pred, 'r-', linewidth=2, label="Fitted Curve")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Parametric Curve Fitting")
plt.legend()
plt.grid(True)
plt.show()

# ==============================================================
#  Output Final Equation
# ==============================================================
print("\n==================== FINAL RESULTS ====================")
print(f"Theta = {theta_opt:.5f} rad = {np.degrees(theta_opt):.2f}°")
print(f"M = {M_opt:.5f}")
print(f"X = {X_opt:.2f}")
print("\nDesmos Equation:")
print(f"(t*cos({theta_opt:.5f}) - e^({M_opt:.5f}*abs(t))*sin(0.3t)*sin({theta_opt:.5f}) + {X_opt:.2f},")
print(f" 42 + t*sin({theta_opt:.5f}) + e^({M_opt:.5f}*abs(t))*sin(0.3t)*cos({theta_opt:.5f}))")
print("\nValid for 6 ≤ t ≤ 60")
print("========================================================")
