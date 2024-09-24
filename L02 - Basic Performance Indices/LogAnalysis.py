import numpy as np
import matplotlib.pyplot as plt


trace = np.loadtxt('LogFile.csv', delimiter=";")
C = len(trace)
print("Completion: ", C)

A_T = np.cumsum(trace[:,0]).reshape(-1,1)
print(A_T)

# Inizializza C_T come un vettore colonna
C_T = np.zeros((C, 1))

# Calcola il primo tempo di completamento
C_T[0, 0] = trace[0, 1] + A_T[0, 0]

# Usa un ciclo for per calcolare i tempi di completamento successivi
for i in range(1, C):
    C_T[i, 0] = max(C_T[i - 1, 0], A_T[i, 0]) + trace[i, 1]

T = C_T[-1,0]
print("Time: ", T)

# Visualizza il risultato
print(C_T)


plt.plot(A_T[:,0], np.r_[0:C])
plt.plot(C_T[:,0], np.r_[0:C])
plt.show()


X = C / T
lam = C / T

B = np.sum(trace[:,1])
U = B / T
S = B / C

print("Throughput: ", X)
print("Lambda: ", lam)
print("Busy Time: ", B)
print("Utilization: ", U)
print("Service time: ", S)

r_i = C_T - A_T
R = np.mean(r_i)
N = X * R

print("Response Time: ", R)
print("Number of Jobs: ", N)