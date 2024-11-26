import numpy as np

# Initial Configuration M/M/1
print("Initial Configuration")

lam = 1 / 2
D = 1.6
rho = lam * D

U = rho
print("Utilization of the system (U):", rho)

p2 = (1 - rho) * (rho ** 2)
print("Probability of having exactly 2 jobs in the system:", p2)

pNlt5 = sum((1 - rho) * (rho ** i) for i in range(5))
print("Probability of having less than 5 jobs in the system:", pNlt5)

N = rho / (1 - rho)
Nq = N - U
print("Average queue length: ", Nq)

R = D / (1 - rho)
print("Average response time (R):", R)

pRtg2 = np.exp(-2 / R)
print("Probability that the response time is greater than 2:", pRtg2)

p95 = -R * np.log(0.05)
print("Percentile 95th:", p95)

print("")
# Second Configuration M/M/2
print("Second Configuration")

lam = 1
rho = lam * D / 2

Ub = rho
U = Ub * 2
print("Total Utilization of the system (U):", U)
print('Average Utilization of the system:', Ub)

p2 = 2 * (1 - rho) / (1 + rho) * (rho ** 2)
print("Probability of having exactly 2 jobs in the system:", p2)

pi = np.zeros(5)
pNlti = np.zeros(5)

pi[0] = (1 - rho) / (1 + rho)
pNlti[0] = pi[0]

for i in range(1, 5):
    pi[i] = 2 * pi[0] * (rho ** i)
    pNlti[i] = pNlti[i - 1] + pi[i]

print("Probability of having exactly 2 jobs in the system:", pi[2])
print("Probability of having less than 5 jobs in the system:", pNlti)

N = 2 * rho / (1 - rho ** 2)
Nq = N - U
print("Average queue length: ", Nq)

R = D / (1 - rho ** 2)
print("Average response time (R):", R)

print("")
# Third Configuration M/M/c
print("Third Configuration")
lam = 4
c = np.ceil(lam * D)
rho = lam * D / c

Ub = rho
U = Ub * c
print("Average Utilization of the system:", Ub)
print('Total Utilization of the system (U):', U)
