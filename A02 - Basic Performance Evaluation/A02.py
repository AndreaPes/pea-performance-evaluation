import numpy as np

# Load data from the files
a_i = np.loadtxt('Logger1.csv', delimiter=',')
s_i = np.loadtxt('Logger2.csv', delimiter=',')

# Number of cars
C = len(a_i)

# Average Inter-Arrival Time
A_ = np.mean(a_i)

# Arrival Rate
lam = 1 / A_

# Target Response Time
R_target = 20
R_current = 0
alpha = 1
a_mod = a_i * alpha

# Loop to find the best approximation for alpha
while R_current < R_target:
    alpha -= 0.0001
    a_mod = a_i * alpha

    A_T = np.cumsum(a_mod)
    C_T = np.zeros(C)
    C_T[0] = A_T[0] + s_i[0]
    for i in range(1, C):
        C_T[i] = np.maximum(A_T[i], C_T[i - 1]) + s_i[i]
    R_current = np.mean(C_T - A_T)

# Arrival Rate for new value of alpha
lam_mod = 1 / np.mean(a_mod)

print(f"Arrival Rate: {lam_mod} cars/min")

# New given value for lambda
lam_mod = 1.2
# Target Response Time
R_target = 15
R_current = 100
beta = 1
# Calculate the new alpha based on the new value of lambda
alpha = lam / lam_mod
# Calculate the new inter arrival times based on the new value of alpha
a_mod = a_i * alpha

# Loop to find the best approximation for beta
while R_current > R_target:
    beta -= 0.0001
    s_mod = s_i * beta

    A_T = np.cumsum(a_mod)
    C_T = np.zeros(C)
    C_T[0] = A_T[0] + s_mod[0]
    for i in range(1, C):
        C_T[i] = np.maximum(A_T[i], C_T[i - 1]) + s_mod[i]
    R_current = np.mean(C_T - A_T)

print(f"Beta: {beta}")
