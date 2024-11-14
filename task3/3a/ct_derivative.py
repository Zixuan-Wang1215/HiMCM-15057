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

# Differentiate C(t) with respect to t
C_t_derivative = sp.diff(C_t, t)

# Solve for t where C'(t) = 0
t_solution = sp.solve(C_t_derivative, t)

# Display the solution(s)
print(t_solution[1])

