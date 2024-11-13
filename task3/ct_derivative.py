import sympy as sp

# Define the variable t
t = sp.symbols('t')

# Define E(t) as an explicit function of t
E = 42.51 * t - 84086.35

# Define each P function of t
P_bio = 0.0005193564761916456*100 * t - 1.0249323789041274*100
P_solar = 0.006999473791285229 *100* t - 14.1028007372921*100
P_wind = 0.006964098717905855*100* t - 13.99992881017315*100
P_hydro = -0.003909503377416621*100 * t + 8.04600316410604*100
P_nuclear = -0.0030414127561043908*100 * t + 6.2557114713864*100
P_coal = -0.004435620565799054*100 * t + 9.354244635986639*100
P_gas = -0.002487251921876305*100 * t + 5.219182283584952*100
P_oil = -0.0005529829731568147*100* t + 1.1372845209044042*100

# Define constants k values symbolically
k_bio, k_solar, k_wind, k_hydro, k_nuclear, k_coal, k_gas, k_oil = sp.symbols('k_bio k_solar k_wind k_hydro k_nuclear k_coal k_gas k_oil')

# Define the expression for C(t)
C_t = E * (P_bio * k_bio + P_solar * k_solar + P_wind * k_wind + 
           P_hydro * k_hydro + P_nuclear * k_nuclear + 
           P_coal * k_coal + P_gas * k_gas + P_oil * k_oil)

# Differentiate C(t) with respect to t
C_t_derivative = sp.diff(C_t, t)

# Substitute the provided values for k constants
k_values = {
    k_bio: 230,
    k_coal: 820,
    k_gas: 490,
    k_hydro: 24,
    k_nuclear: 12,
    k_oil: 600,
    k_solar: 48,
    k_wind: 11.5
}

# Substitute the k values into the derivative expression
C_t_prime_with_k_values = C_t_derivative.subs(k_values)

# Solve for t where C'(t) = 0
t_solution = sp.solve(C_t_prime_with_k_values, t)

# Display the solution(s)
print(t_solution)
