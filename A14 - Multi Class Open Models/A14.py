import numpy as np
from scipy import linalg

# Arrival rates (jobs/min)
lamA = XA = 1.5 / 60
lamB = XB = 2.5 / 60
lamC = XC = 2 / 60

# Service times (minutes)
S1A, S1B, S1C = 8, 3, 4
S2A, S2B, S2C = 10, 2, 7

# Probabilities
p21A, p21B, p21C = 0.1, 0.08, 0.12

PA = np.array([[0, 1], [p21A, 0]])
PB = np.array([[0, 1], [p21B, 0]])
PC = np.array([[0, 1], [p21C, 0]])

# Visits
vA = linalg.solve((np.eye(2) - PA.T), np.array([1, 0]))
vB = linalg.solve((np.eye(2) - PB.T), np.array([1, 0]))
vC = linalg.solve((np.eye(2) - PC.T), np.array([1, 0]))

# Demands
D1A, D1B, D1C = vA[0] * S1A, vB[0] * S1B, vC[0] * S1C
D2A, D2B, D2C = vA[1] * S2A, vB[1] * S2B, vC[1] * S2C

# Utilization
U1 = lamA * D1A + lamB * D1B + lamC * D1C
U2 = lamA * D2A + lamB * D2B + lamC * D2C
print("Utilization of Station 1:", U1)
print("Utilization of Station 2:", U2)

# Response Times
R1A, R1B, R1C = D1A / (1 - U1), D1B / (1 - U1), D1C / (1 - U1)
R2A, R2B, R2C = D2A / (1 - U2), D2B / (1 - U2), D2C / (1 - U2)
RA, RB, RC = R1A + R2A, R1B + R2B, R1C + R2C

NA = lamA * RA
NB = lamB * RB
NC = lamC * RC
print("Average Number of Jobs in the System for Class A:", NA)
print("Average Number of Jobs in the System for Class B:", NB)
print("Average Number of Jobs in the System for Class C:", NC)

print("Average System Response Time for Class A:", RA)
print("Average System Response Time for Class B:", RB)
print("Average System Response Time for Class C:", RC)

# Class-Independent Metrics
X = XA + XB + XC
N1 = XA * R1A + XB * R1B + XC * R1C
N2 = XA * R2A + XB * R2B + XC * R2C
N = N1 + N2
print("Average Number of Jobs in the System:", N)

R = (XA * RA + XB * RB + XC * RC) / (XA + XB + XC)
print("Average System Response Time:", R)
