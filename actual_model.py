import numpy as np
import matplotlib.pyplot as plt

# Months: 1 = April, 2 = May, 3 = June
months = np.array([1, 2, 3])
rainfall_actual = np.array([20.0, 60.0, 95.0])

# Store predictions
predictions = {}

# Iteration 1: Hardcoded
coeffs1 = np.polyfit(months, rainfall_actual, 2)
model1 = np.poly1d(coeffs1)
predictions['Iteration 1'] = model1

# Iteration 2: Keyboard input (simulated)
rainfall_keyboard = np.array([22.0, 63.0, 92.0])
model2 = np.poly1d(np.polyfit(months, rainfall_keyboard, 2))
predictions['Iteration 2'] = model2

# Iteration 3: File input (simulated)
rainfall_file = np.array([18.0, 65.0, 90.0])
model3 = np.poly1d(np.polyfit(months, rainfall_file, 2))
predictions['Iteration 3'] = model3

# Iteration 4: Final
rainfall_final = np.array([21.0, 66.5, 94.5])
model4 = np.poly1d(np.polyfit(months, rainfall_final, 2))
predictions['Iteration 4'] = model4

# Smooth curve x-values
x_smooth = np.linspace(1, 3, 100)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(months, rainfall_actual, 'ko', label='Original Actual Data', markersize=8)

colors = ['r', 'g', 'b', 'm']
for i, (label, model) in enumerate(predictions.items()):
    y_smooth = model(x_smooth)
    plt.plot(x_smooth, y_smooth, color=colors[i], label=label)

plt.title("Rainfall Modeling – Actual Data (April–June 2025)")
plt.xlabel("Month (1 = Apr, 2 = May, 3 = Jun)")
plt.ylabel("Rainfall (mm)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
