import math
import numpy as np


def calculate_metrics(lam, mu, c, K, config_name):
    print(config_name)

    rho = lam / (c * mu)

    p0_sum = sum([(c * rho) ** k / math.factorial(k) for k in range(c)])
    p0_sum += ((c * rho) ** c / math.factorial(c)) * ((1 - rho ** (K - c + 1)) / (1 - rho))
    p0 = 1 / p0_sum

    p_n = np.zeros(K + 1)
    for n in range(c):
        p_n[n] = (p0 / math.factorial(n)) * (c * rho) ** n
    for n in range(c, K + 1):
        p_n[n] = (p0 * (c ** c) * rho ** n) / (math.factorial(c))

    U = sum(i * p_n[i] for i in range(1, c + 1)) + c * sum(p_n[i] for i in range(c + 1, K + 1))
    print("Total Utilization of the system (U):", U)

    Ub = U / c
    print("Average Utilization:", Ub)

    pL = p_n[K]
    print("Loss Probability [%]: ", pL * 100)

    N = sum(i * p_n[i] for i in range(1, K + 1))
    print("Average Number of Jobs in the System:", N)

    Dr = lam * pL
    print("Drop Rate [req/min]:", Dr)

    R = N / (lam * (1 - pL))
    print("Average Response Time [ms]:", R * 60 * 1000)

    Wq = R - (1 / mu)
    print("Average Queue Waiting Time [ms]:", Wq * 60 * 1000)
    print()


# Initial Configuration
calculate_metrics(lam=240, mu=300, c=1, K=16, config_name="M/M/1/K")

# Second Configuration
calculate_metrics(lam=360, mu=300, c=2, K=16, config_name="M/M/2/K")

# Final Configuration
# I computed c with brute force and got c = 4
calculate_metrics(lam=960, mu=300, c=4, K=16, config_name="M/M/c/K")
