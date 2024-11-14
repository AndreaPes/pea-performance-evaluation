import numpy as np

M = 5000
RELATIVE_ERROR = 0.02
d_95 = 1.96

K0 = 10
maxK = 100000
delta_K = 10
K = K0
K_range = K

U1 = U2 = X1 = X2 = R1 = R2 = N1 = N2 = 0

# Scenario 1

# Arrival Distribution -> two-stages Hyper-Exponential
lambda_1 = 0.025
lambda_2 = 0.1
p1 = 0.35

# Service Distribution -> Weibull
shape_k = 0.333
scale_l = 2.5


# Scenario 2

# Arrival  Distribution -> Erlang
stages_k = 8
rate_l = 1.25

# Service Distribution -> Uniform
min_a = 1
max_b = 10


def hyper_distribution():
    u1_hyper = np.random.rand(M)
    u2_hyper = np.random.rand(M)
    return np.where(u1_hyper < p1, -np.log(u2_hyper) / lambda_1, -np.log(u2_hyper) / lambda_2)


def weibull_distribution():
    u_weibull = np.random.rand(M)
    return scale_l * (-np.log(u_weibull)) ** (1 / shape_k)


def erlang_distribution():
    u_erlang = np.random.rand(M, stages_k)
    return (-np.sum(np.log(u_erlang), axis=1)) / rate_l


def uniform_distribution():
    u_uniform = np.random.rand(M)
    return min_a + (max_b - min_a) * u_uniform


def calculate_confidence(mean, mean_square, k):
    e = mean / k
    e2 = mean_square / k
    delta = d_95 * np.sqrt(e2 - e ** 2) / np.sqrt(k)
    lower = e - delta
    upper = e + delta
    return lower, upper, 2 * (upper - lower) / (upper + lower)


while K <= maxK:

    for k in range(K_range):

        a_i = hyper_distribution()
        s_i = weibull_distribution()

        A_T = np.cumsum(a_i)
        C_T = np.zeros(M)

        C_T[0] = A_T[0] + s_i[0]
        for i in range(1, M):
            C_T[i] = s_i[i] + np.maximum(C_T[i - 1], A_T[i])

        B = np.sum(s_i)
        T = C_T[M - 1] - A_T[0]

        # Utilization
        Uk = B / T
        U1 += Uk
        U2 += (Uk ** 2)

        # Throughput
        Xk = len(A_T) / T
        X1 += Xk
        X2 += (Xk ** 2)

        # Average Response Time
        Rk = np.mean(C_T - A_T)
        R1 += Rk
        R2 += (Rk ** 2)

        # Average Number of Jobs
        Nk = Xk * Rk
        N1 += Nk
        N2 += (Nk ** 2)

    Ul, Uu, RelErrU = calculate_confidence(U1, U2, K)

    Xl, Xu, RelErrX = calculate_confidence(X1, X2, K)

    Rl, Ru, RelErrR = calculate_confidence(R1, R2, K)

    Nl, Nu, RelErrNl = calculate_confidence(N1, N2, K)

    if RelErrU < RELATIVE_ERROR and RelErrX < RELATIVE_ERROR and RelErrR < RELATIVE_ERROR and RelErrNl < RELATIVE_ERROR:
        break

    K += delta_K
    Krange = delta_K

print("95% confidence interval of U: ", Ul, Uu)
print("95% confidence interval of X: ", Xl, Xu)
print("95% confidence interval of R: ", Rl, Ru)
print("95% confidence interval of N: ", Nl, Nu)
print("Solution obtained in ", K, " iterations")

K0 = 10
maxK = 100000
delta_K = 10
K = K0
K_range = K

U1 = U2 = X1 = X2 = R1 = R2 = N1 = N2 = 0

while K <= maxK:

    for k in range(K_range):

        a_i = erlang_distribution()
        s_i = uniform_distribution()

        A_T = np.cumsum(a_i)
        C_T = np.zeros(M)

        C_T[0] = A_T[0] + s_i[0]
        for i in range(1, M):
            C_T[i] = s_i[i] + np.maximum(C_T[i - 1], A_T[i])

        B = np.sum(s_i)
        T = C_T[M - 1] - A_T[0]

        # Utilization
        Uk = B / T
        U1 += Uk
        U2 += (Uk ** 2)

        # Throughput
        Xk = len(A_T) / T
        X1 += Xk
        X2 += (Xk ** 2)

        # Average Response Time
        Rk = np.mean(C_T - A_T)
        R1 += Rk
        R2 += (Rk ** 2)

        # Average Number of Jobs
        Nk = Xk * Rk
        N1 += Nk
        N2 += (Nk ** 2)

    Ul, Uu, RelErrU = calculate_confidence(U1, U2, K)

    Xl, Xu, RelErrX = calculate_confidence(X1, X2, K)

    Rl, Ru, RelErrR = calculate_confidence(R1, R2, K)

    Nl, Nu, RelErrNl = calculate_confidence(N1, N2, K)

    if RelErrU < RELATIVE_ERROR and RelErrX < RELATIVE_ERROR and RelErrR < RELATIVE_ERROR and RelErrNl < RELATIVE_ERROR:
        break

    K += delta_K
    Krange = delta_K

print("95% confidence interval of U: ", Ul, Uu)
print("95% confidence interval of X: ", Xl, Xu)
print("95% confidence interval of R: ", Rl, Ru)
print("95% confidence interval of N: ", Nl, Nu)
print("Solution obtained in ", K, " iterations")
