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
inter_arrival_times = np.diff(A_T)
# Average Inter-Arrival Time
average_inter_arrival_time = 1 / lam

# Response Times
r_i = C_T - A_T
# Average Response Time
R = np.mean(r_i)

# Number of Jobs with Little's Law
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

# Definire l'intervallo e la granularità per il tempo di risposta
tau_values = np.arange(1, 41, 1)  # Da 1 a 40 minuti con passo di 1 minuto
response_distribution = []

for tau in tau_values:
    prob = np.sum(r_i < tau) / C
    response_distribution.append(prob)

# Grafico della distribuzione del tempo di risposta
plt.plot(tau_values, response_distribution, label="Response Time Distribution")
plt.title('Response Time Distribution')
plt.xlabel('Response Time (minutes)')
plt.ylabel('Cumulative Probability')
plt.grid(True)
plt.show()

# Istogramma del tempo di risposta
plt.hist(r_i, bins=np.arange(1, 41, 1), density=True, alpha=0.75, edgecolor='black')
plt.title('Response Time Histogram')
plt.xlabel('Response Time (minutes)')
plt.ylabel('Probability Density')
plt.grid(True)
plt.show()

# Definire l'intervallo e la granularità per il tempo di servizio
tau_service_values = np.arange(0.1, 5.1, 0.1)  # Da 0.1 a 5 minuti con passo di 0.1 minuti
service_distribution = []

for tau in tau_service_values:
    prob = np.sum(s_i < tau) / C
    service_distribution.append(prob)

# Grafico della distribuzione del tempo di servizio
plt.plot(tau_service_values, service_distribution, label="Service Time Distribution")
plt.title('Service Time Distribution')
plt.xlabel('Service Time (minutes)')
plt.ylabel('Cumulative Probability')
plt.grid(True)
plt.show()

# Istogramma del tempo di servizio
plt.hist(s_i, bins=np.arange(0.1, 5.1, 0.1), density=True, alpha=0.75, edgecolor='black')
plt.title('Service Time Histogram')
plt.xlabel('Service Time (minutes)')
plt.ylabel('Probability Density')
plt.grid(True)
plt.show()


print(f"Number of cars: {C} cars")
print(f"Total time: {T} min")
print(f"Arrival Rate: {lam} cars/min")
print(f"Throughput: {X} cars/min")
print(f"Average Inter-Arrival Time: {average_inter_arrival_time} min")
print(f"Average Service Time: {S} min")
print(f"Busy Time: {B} min")
print(f"Utilization: {U * 100} %")
print(f"Average Response Time: {R} min")
print(f"Number of jobs: {N} jobs")
