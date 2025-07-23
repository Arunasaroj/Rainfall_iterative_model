import numpy as np
import matplotlib.pyplot as plt

months = np.array([1, 2, 3])
rainfall_actual = np.array([20.0, 60.0, 95.0])  # Reference

# Hypothetical predictions
predictions = {}

# Iteration 1
hypo1 = np.array([15.0, 58.0, 100.0])
predictions['Iteration 1'] = np.poly1d(np.polyfit(months, hypo1, 2))

# Iteration 2
hypo2 = np.array([16.5, 60.0, 97.0])
predictions['Iteration 2'] = np.poly1d(np.polyfit(months, hypo2, 2))

# Iteration 3
hypo3 = np.array([18.0, 62.5, 94.0])
predictions['Iteration 3'] = np.poly1d(np.polyfit(months, hypo3, 2))

# Iteration 4
hypo4 = np.array([19.5, 64.0, 92.5])
predictions['Iteration 4'] = np.poly1d(np.polyfit(months, hypo4, 2))

# Smooth curve x-values
x_smooth = np.linspace(1, 3, 100)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(months, rainfall_actual, 'ko', label='Original Actual Data', markersize=8)

colors = ['r', 'g', 'b', 'm']
for i, (label, model) in enumerate(predictions.items()):
    y_smooth = model(x_smooth)
    plt.plot(x_smooth, y_smooth, color=colors[i], label=label)

plt.title("Rainfall Modeling – Hypothetical Data (April–June 2025)")
plt.xlabel("Month (1 = Apr, 2 = May, 3 = Jun)")
plt.ylabel("Rainfall (mm)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
