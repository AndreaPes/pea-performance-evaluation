import numpy as np
from scipy import linalg

N = 100

# Service times
S = np.array([40, 50 / 1000, 2 / 1000, 80 / 1000, 80 / 1000, 100 / 1000])
Z = S[0]

# Transition probability matrix
P = np.array([[0, 1, 0, 0, 0, 0],
              [0, 0, 0.35, 0.6, 0, 0],
              [0, 0, 0, 0, 0.65, 0.35],
              [0, 1, 0, 0, 0, 0],
              [0, 0.9, 0, 0, 0, 0.1],
              [0, 0.9, 0, 0, 0.1, 0]])

# Visits
v = linalg.solve(np.eye(6) - P.T, np.array([1, 0, 0, 0, 0, 0]))

# Demands
Dk = v * S

Nk = np.zeros(6)

for n in range(1, N + 1):
    Rk = Dk * (1 + Nk)
    Rsys = np.sum(Rk[1:])
    X = n / (Rsys + Z)
    Nk = Rk * X

Uk = Dk * X
Xk = X * v

# Output Results
print("Demand on Disk1 [ms]:", Dk[4] * 1000)
print("Demand on Disk2 [ms]:", Dk[5] * 1000)
print("System Throughput:", X)
print("Average System Response Time [ms]:", Rsys * 1000)
print("Utilization of the AppServer:", Uk[1])
print("Utilization of the DBMS:", Uk[3])
print("Utilization of Disk1:", Uk[4])
print("Utilization of Disk2:", Uk[5])
print("Throughput of Disk1:", Xk[4])
print("Throughput of Disk2:", Xk[5])
