import math
import numpy as np

D = 1.6


# Utility Functions

def calculate_probabilities(lam, c):
    rho = lam * D / c
    p0 = sum([(c * rho) ** n / math.factorial(n) for n in range(c)]) + ((c * rho) ** c) / (
            math.factorial(c) * (1 - rho))
    p0 = 1 / p0
    return rho, p0


# Configurations

def initial_configuration(lam):
    print("Initial Configuration")
    rho = lam * D

    # Utilization
    U = rho
    print("Utilization of the system (U):", U)

    # Probability Calculations
    p2 = (1 - rho) * (rho ** 2)
    print("Probability of having exactly 2 jobs in the system:", p2)

    pNlt5 = sum((1 - rho) * (rho ** i) for i in range(5))
    print("Probability of having less than 5 jobs in the system:", pNlt5)

    # Average Queue Length
    N = rho / (1 - rho)
    Nq = N - U
    print("Average queue length: ", Nq)

    # Average Response Time
    R = D / (1 - rho)
    print("Average response time (R):", R)

    # Probability that Response Time > 2
    pRtg2 = np.exp(-2 / R)
    print("Probability that the response time is greater than 2:", pRtg2)

    # 95th Percentile
    p95 = -R * np.log(0.05)
    print("Percentile 95th:", p95)
    print("")


def second_configuration(lam):
    print("Second Configuration")
    rho = lam * D / 2

    # Utilization
    Ub = rho
    U = Ub * 2
    print("Total Utilization of the system (U):", U)
    print('Average Utilization of the system:', Ub)

    # Probability Calculations
    pi = np.zeros(5)
    pNlti = np.zeros(5)

    pi[0] = (1 - rho) / (1 + rho)
    pNlti[0] = pi[0]

    for i in range(1, 5):
        pi[i] = 2 * pi[0] * (rho ** i)
        pNlti[i] = pNlti[i - 1] + pi[i]

    print("Probability of having exactly 2 jobs in the system:", pi[2])
    print("Probability of having less than 5 jobs in the system:", pNlti[-1])

    # Average Queue Length
    N = 2 * rho / (1 - rho ** 2)
    Nq = N - U
    print("Average queue length: ", Nq)

    # Average Response Time
    R = D / (1 - rho ** 2)
    print("Average response time (R):", R)
    print("")


def third_configuration(lam):
    print("Third Configuration")
    c = int(np.ceil(lam * D))
    rho, p0 = calculate_probabilities(lam, c)

    # Utilization
    Ub = rho
    U = Ub * c
    print('Total Utilization of the system (U):', U)
    print("Average Utilization of the system:", Ub)

    # Probability Calculations
    pi = np.zeros(5)
    pNlti = np.zeros(5)

    pi[0] = p0
    pNlti[0] = pi[0]

    for n in range(1, 5):
        if n < c:
            pi[n] = pi[n - 1] * (c * rho) / n
        else:
            pi[n] = pi[n - 1] * rho
        pNlti[n] = pNlti[n - 1] + pi[n]

    print("Probability of having exactly 2 jobs in the system:", pi[2])
    print("Probability of having less than 5 jobs in the system:", pNlti[-1])

    # Average Queue Length
    NSum = sum([(c * rho) ** i / math.factorial(i) for i in range(c)])
    N = c * rho + (rho / (1 - rho)) / (1 + (1 - rho) * (math.factorial(c) / ((c * rho) ** c)) * NSum)
    Nq = N - U
    print("Average queue length: ", Nq)

    # Average Response Time
    R = N / lam
    print("Average response time (R):", R)
    print("")


def final_configuration(lam):
    print("Final Configuration")
    rho = lam * D

    # Utilization
    U = rho
    print("Utilization of the system (U):", U)

    # Probability Calculations
    pi = np.zeros(5)
    pNlti = np.zeros(5)

    pi[0] = np.exp(-rho)
    pNlti[0] = pi[0]

    for i in range(1, 5):
        pi[i] = pi[i - 1] * rho / i
        pNlti[i] = pNlti[i - 1] + pi[i]

    print("Probability of having exactly 2 jobs in the system:", pi[2])
    print("Probability of having less than 5 jobs in the system:", pNlti[-1])

    # Average Response Time
    N = U
    R = N / lam
    print("Average response time (R):", R)


# Function Call
initial_configuration(1 / 2)
second_configuration(1)
third_configuration(4)
final_configuration(10)
