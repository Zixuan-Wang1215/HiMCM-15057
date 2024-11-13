import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define the constants
k_values = {
    'k_bio': 230,
    'k_solar': 48,
    'k_wind': 11.5,
    'k_hydro': 24,
    'k_nuclear': 12,
    'k_coal': 820,
    'k_gas': 490,
    'k_oil': 600
}

# Define E(t) and each P function in terms of numpy
def E(t):
    return 42.51 * t - 84086.35

def P_bio(t):
    return 0.0005193564761916456 * t - 1.0249323789041274

def P_solar(t):
    return 0.006999473791285229 * t - 14.1028007372921

def P_wind(t):
    return 0.006964098717905855 * t - 13.99992881017315

def P_hydro(t):
    return -0.003909503377416621 * t + 8.04600316410604

def P_nuclear(t):
    return -0.0030414127561043908 * t + 6.2557114713864

def P_coal(t):
    return -0.004435620565799054 * t + 9.354244635986639

def P_gas(t):
    return -0.002487251921876305 * t + 5.219182283584952

def P_oil(t):
    return -0.0005529829731568147 * t + 1.1372845209044042

# Define C(t) based on the values of k
def C(t):
    return E(t) * (P_bio(t) * k_values['k_bio'] + P_solar(t) * k_values['k_solar'] + 
                   P_wind(t) * k_values['k_wind'] + P_hydro(t) * k_values['k_hydro'] + 
                   P_nuclear(t) * k_values['k_nuclear'] + P_coal(t) * k_values['k_coal'] + 
                   P_gas(t) * k_values['k_gas'] + P_oil(t) * k_values['k_oil'])

# Generate t values for plotting from 2018 to 2060
t_values = np.linspace(2018, 2060, 500)
C_values = C(t_values)

# Plot C(t) with the specified range
plt.figure(figsize=(10, 6))
plt.plot(t_values, C_values, label="C(t)", color="blue")
plt.xlabel("Year")
plt.ylabel("C(t)")
plt.title("Plot of C(t) from 2018 to 2060")
plt.legend()
plt.grid(True)
plt.show()
