import numpy as np
import matplotlib.pyplot as plt

# Load data from the files
A_T = np.loadtxt('Logger1.csv', delimiter=',')
C_T = np.loadtxt('Logger2.csv', delimiter=',')

# Number of cars
C = len(A_T)

# Total Time
# it is possible to pick it many other different ways
T = C_T[-1]

# Arrival Rate
lam = C / T

# Throguhput
X = C / T

# Inter-Arrival Time
a_i = np.diff(A_T)
# Average Inter-Arrival Time
A_ = np.mean(a_i)

# Response Times
r_i = C_T - A_T
# Average Response Time
R = np.mean(r_i)

# Average Number of Jobs with Little's Law
N = X * R

# Service Times
s_i = C_T - np.maximum(A_T, np.roll(C_T, 1))
s_i[0] = C_T[0] - A_T[0]
# Average Service Time
S = np.mean(s_i)

# Busy Time
B = S * C

# Utilization Law
U = B / T

print(f"Arrival Rate: {lam} cars/min")
print(f"Throughput: {X} cars/min")
print(f"Average Inter-Arrival Time: {A_} min")
print(f"Utilization: {U * 100} %")
print(f"Average Service Time: {S} min")
print(f"Number of jobs: {N} jobs")
print(f"Average Response Time: {R} min")

# Values of the range requested for the Response Time Distribution
R_values = np.arange(1, 41, 1)
R_distribution = []

for val in R_values:
    P = np.sum(r_i < val) / C
    R_distribution.append(P)

# Plot of the Response Time Distribution between 1 and 40 minutes
plt.plot(R_values, R_distribution, label="Response Time Distribution", marker='o', linestyle='-',
         color='skyblue', markersize=8)
plt.title('Response Time Distribution')
plt.xlabel('Response Time (minutes)')
plt.ylabel('Probability')
plt.xticks(R_values)
plt.grid(True)
plt.show()

# Values of the range requested for the Service Time Distribution
S_values = np.arange(0.1, 5.1, 0.1)
S_distribution = []

for val in S_values:
    P = np.sum(s_i < val) / C
    S_distribution.append(P)

# Plot of the Service Time Distribution between 0.1 and 5 minutes
plt.plot(S_values, S_distribution, label="Service Time Distribution", marker='o', linestyle='-',
         color='lightcoral', markersize=8)
plt.title('Service Time Distrbution')
plt.xlabel('Service Time (minutes)')
plt.ylabel('Probability')
plt.xticks(S_values)
plt.grid(True)
plt.show()

# Reshape A_T and C_T into column vectors and concatenate them with +1 for arrivals and -1 for completions
AC_T = np.block([[A_T.reshape(-1, 1), np.ones((C, 1))],
                 [C_T.reshape(-1, 1), -np.ones((C, 1))]])
AC_T = AC_T[AC_T[:, 0].argsort()]
AC_T[:, 1] = np.cumsum(AC_T[:, 1])

# Calculate the intervals between events and keep track of the Number of Cars in the system
AC_T = np.c_[[AC_T[1:, 0] - AC_T[0:-1, 0], AC_T[0:-1, 1]]].T

# Values of the range requested for the Number of Cars Distribution
N_values = np.arange(0, 26, 1)
N_distribution = []

for val in N_values:
    N_distribution.append(np.sum(AC_T[AC_T[:, 1] == val, 0]) / T)

# Plot of the Number of Cars Distribution between 0 and 25
plt.bar(N_values, N_distribution, color='lightgreen', edgecolor='black')
plt.title('Queue Length Distribution')
plt.xlabel('Number of Cars in the road segment')
plt.ylabel('Probability')
plt.xticks(N_values)
plt.grid(True, axis='y')
plt.show()
