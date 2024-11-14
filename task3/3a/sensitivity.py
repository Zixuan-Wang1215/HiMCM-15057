import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define the variable t
t = sp.symbols('t')

# Define variables and constants
a = 0.02224047547  # variable
y = [0, 0.020188178122662336, 0.1225081883, 0.078741188055, -0.0285203182168, -0.0295473656974, -0.011642530584, -0.0132673499159, -0.029730321387]  # variable
P0s = [0, 2.57257724315717 / 100, 5.71347424779 / 100, 8.84428961504 / 100, 13.7077831592 / 100, 10.2933465787 / 100, 38.0984231375 / 100, 18.7471645629 / 100, 1.85999662082 / 100]  # constant
k = [0, 230, 48, 11.5, 24, 12, 820, 490, 600]  # constant

# Define E(t) as an explicit function of t
E = 1911.38 * (1 + a * t)

# Define each P_i(t) based on the given formula
P = [0] + [P0s[i] * (1 + y[i] * t) for i in range(1, 9)]

# Normalize P to make the sum equal to 1
P_sum = sum(P)
P = [p_i / P_sum for p_i in P]
# Define C(t) as per the summation form
C_t = E * (P[1] * k[1] + P[2] * k[2] + P[3] * k[3] + P[4] * k[4] +
           P[5] * k[5] + P[6] * k[6] + P[7] * k[7] + P[8] * k[8])

# Define a function to calculate C(t) for given a and y
def calculate_C_t(a, y):
    E = 1911.38 * (1 + a * t)
    P = [0] + [P0s[i] * (1 + y[i] * t) for i in range(1, 9)]
    C_t = E * (P[1] * k[1] + P[2] * k[2] + P[3] * k[3] + P[4] * k[4] +
               P[5] * k[5] + P[6] * k[6] + P[7] * k[7] + P[8] * k[8])
    return C_t

# Sensitivity analysis for variable 'a'
a_values = [0.8 * a, a, 1.2 * a]
y_values = [y, [0.8 * yi for yi in y], [1.2 * yi for yi in y]]

# Define the range of t values
t_values = np.linspace(0, 40, 100)  # Adjust the range as needed

plt.figure(figsize=(10, 6))

# Define line styles and colors
line_styles = ['-', '-', '-']
colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown']

# Calculate and plot C(t) for different values of 'a'
for i, a_val in enumerate(a_values):
    C_t = calculate_C_t(a_val, y)
    C_t_func = sp.lambdify(t, C_t, 'numpy')
    C_t_values = C_t_func(t_values)
    plt.plot(t_values, C_t_values, label=f"C(t) with α={a_val:.5f}", linestyle=line_styles[i], color=colors[i])

# Calculate and plot C(t) for different values of 'y'
for i, y_val in enumerate(y_values):
    C_t = calculate_C_t(a, y_val)
    C_t_func = sp.lambdify(t, C_t, 'numpy')
    C_t_values = C_t_func(t_values)
    plt.plot(t_values, C_t_values, label=f"C(t) with γ scaled", linestyle=line_styles[i], color=colors[i + 3])

plt.xlabel("t")
plt.ylabel("C(t) gCO2/h")
plt.title("Sensitivity Analysis of Average CO2 Emissions per Hour Over Time")
plt.legend()
plt.grid(False)

# Adjust x-axis labels to show t + 2023
ax = plt.gca()
ax.set_xticklabels([int(label) + 2023 for label in ax.get_xticks()])

# Disable scientific notation for the y-axis
ax.yaxis.get_major_formatter().set_scientific(False)

# Save the plot to the /predictions directory
plt.savefig('task3/3a/predictions/sensitivity_ct_plot.png')

plt.show()