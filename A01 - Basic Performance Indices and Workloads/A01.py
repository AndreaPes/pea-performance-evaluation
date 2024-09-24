import numpy as np
import matplotlib.pyplot as plt

# Load data from the files
A_T = np.loadtxt('Logger1.csv', delimiter=',')
C_T = np.loadtxt('Logger2.csv', delimiter=',')

# Number of cars
C = len(A_T)

# Total Time
T = C_T[-1]

# Arrival Rate
lam = C / T

# Throguhput
X = C / T

# Inter-Arrival Time
inter_arrival_times = np.diff(A_T)
# Average Inter-Arrival Time
average_inter_arrival_time_v1 = 1 / lam
average_inter_arrival_time_v2 = np.mean(inter_arrival_times)

# Response Times
r_i = C_T - A_T
# Average Response Time
R = np.mean(r_i)

# Number of Jobs with Little's Law
N = X * R

# Service Times
service_times = np.zeros(C)
service_times[0] = C_T[0] - A_T[0]
for i in range (1, C):
    service_times[i] = C_T[i] - max(A_T[i], C_T[i - 1])

# Average Service Time
S = np.mean(service_times)

# Busy Time
B = S * C

# Utilization Law
U = B / T

print(f"Number of cars: {C} cars")
print(f"Total time: {T} min")
print(f"Average time per car: {lam} cars/min")
print(f"Throughput: {X} cars/min")
print(f"Average Inter-Arrival Time v1: {average_inter_arrival_time_v1} min")
print(f"Average Inter-Arrival Time v2: {average_inter_arrival_time_v2} min")
print(f"Average Service Time: {S} min")
print(f"Busy Time: {B} min")
print(f"Utilization: {U} min")
print(f"Average Response Time: {R} min")
print(f"Number of jobs: {N} jobs")