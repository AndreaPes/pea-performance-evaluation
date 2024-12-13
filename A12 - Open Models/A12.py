import numpy as np
from scipy import linalg

S1 = 2
S2 = 20 / 1000
S3 = 100 / 1000
S4 = 70 / 1000

lam_in1 = 2.5
lam_in2 = 2

P = np.array([[0, 0.7, 0, 0],
              [0, 0, 0.25, 0.45],
              [0, 1, 0, 0],
              [0, 1, 0, 0]])

lam_in = np.zeros(4)
lam_sum = lam_in1 + lam_in2
lam_in[0] = lam_in1 / lam_sum
lam_in[1] = lam_in2 / lam_sum

Id = np.eye(4)

v = linalg.solve((Id - P).T, lam_in)

print("Visits of the AppServer: ", v[1])
print("Visits of the Storage: ", v[2])
print("Visits of the DBMS: ", v[3])

Sk = np.array([S1, S2, S3, S4])

Dk = v * Sk

X = lam_sum
print("System Throughput: ", X)

Uk = X * Dk

Nk = Uk / (1 - Uk)
Nk[0] = Uk[0]
N = np.sum(Nk)
print("Average Number of Jobs: ", N)

Rk = Dk / (1 - Uk)
Rk[0] = Dk[0]
R = np.sum(Rk)
print("Average Response Time [ms]: ", R * 1000)

lam_max = 1 / np.max(Dk)
print("Max Arrival rate: ", lam_max)
