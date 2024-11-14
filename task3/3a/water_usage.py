import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define the variable t
t = sp.symbols('t')

# Define variables and constants
a = 0.02224047547  # variable
y = [0, 0.020188178122662336, 0.1225081883, 0.078741188055, -0.0285203182168, -0.0295473656974, -0.011642530584, -0.0132673499159, -0.029730321387]  # variable
P0s = [0, 2.57257724315717 / 100, 5.71347424779 / 100, 8.84428961504 / 100, 13.7077831592 / 100, 10.2933465787 / 100, 38.0984231375 / 100, 18.7471645629 / 100, 1.85999662082 / 100]  # constant
#bio, solar, wind, hydro, nuclear, coal, gas, oil
k= [0, 537.234, 1.126 , 0.279, 69.93, 2.103, 2.325, 0.847, 3.19]  # constant

# Define E(t) as an explicit function of t
E = 1911.38 * (1 +  a * t)

# Define each P_i(t) based on the given formula
P = [0] + [P0s[i] * (1 + y[i] * t) for i in range(1, 9)]

# Normalize P to make the sum equal to 1
P_sum = sum(P)
P = [p_i / P_sum for p_i in P]
# Define C(t) as per the summation form
W_t = E * (P[1] * k[1] + P[2] * k[2] + P[3] * k[3] + P[4] * k[4] +
           P[5] * k[5] + P[6] * k[6] + P[7] * k[7] + P[8] * k[8])

# Convert W_t to a numerical function
W_t_func = sp.lambdify(t, W_t, 'numpy')

# Define the range of t values
t_values = np.linspace(0, 40, 100)  # Adjust the range as needed
W_t_values = W_t_func(t_values)


# Plot C(t)
plt.figure(figsize=(10, 6))
plt.plot(t_values, W_t_values, label="C(t)", color='b')
plt.xlabel("t")
plt.ylabel("C(t) gCO2/h")
plt.title("Prediction of Average CO2 Emissions per Hour Over Time")
plt.legend()
plt.grid(False)

# Adjust x-axis labels to show t + 2023
ax = plt.gca()
ax.set_xticklabels([int(label) + 2023 for label in ax.get_xticks()])

# Save the plot to the /predictions directory
plt.savefig('task3/3a/predictions/water_usage_plot.png')

plt.show()
