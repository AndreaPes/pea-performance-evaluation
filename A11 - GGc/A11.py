import math
import numpy as np

# Erlang Distribution Parameters
k = 4
lam_e = 100
D = k / lam_e
m2 = k / lam_e**2 + (k / lam_e)**2
ca = 1 / math.sqrt(k)

# Initial Configuration
print("Initial Configuration")
# Poisson Distribution
lam = 20

rho = lam * D
print("Utilization (U):", rho)

w = lam * m2 / 2
R = D + w / (1 - rho)
print("Average Response Time [ms]:", R * 1000)

N = lam * R
print("Average Number of Jobs in the System:", N)

print("\nSecond Configuration")
# Hyper-Exponential Distribution Parameters
lam1_he = 40
lam2_he = 240
p1 = 0.8
p2 = 1 - p1

T = p1 / lam1_he + p2 / lam2_he
lam = 1 / T
m2 = 2 * (p1 / lam1_he**2 + p2 / lam2_he**2)
cv = math.sqrt(m2 - T**2) / T

c = int(np.ceil(lam * D))
print("Minimum number of servers for a stable system:", c)

rho = lam * D / c
print("Utilization (U):", rho)

R = D + ((cv**2 + ca**2) / 2) * (rho**2 * D) / (1 - rho**2)
print("Average Approximate Response Time [ms]:", R * 1000)

N = lam * R
print("Average Approximate Number of Jobs in the System:", N)
