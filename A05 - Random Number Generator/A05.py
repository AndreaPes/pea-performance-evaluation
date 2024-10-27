import math

import matplotlib.pyplot as plt
import numpy as np

N = 10000
t = np.arange(1, N + 1, 1) / 50
py = np.arange(1, N + 1, 1) / N

# Exponential Distribution
l_exp = 0.25
u_exp = np.random.rand(N)
X_exp = -np.log(u_exp) / l_exp
X_exp.sort()

F_exp = 1 - np.exp(-l_exp * t)

plt.plot(X_exp, py, ".", color='lightcoral', label="Empirical CDF")
plt.plot(t, F_exp, linestyle='-', color='lightgreen', label="Theoretical CDF")
plt.title('Exponential')
plt.legend()
plt.show()

# Pareto Distribution
a = 2.5
m = 3
u_pareto = np.random.rand(N)
X_pareto = m / u_pareto ** (1 / a)
X_pareto.sort()

F_pareto = np.where(t >= m, 1 - (m / t) ** a, 0)

plt.plot(X_pareto, py, ".", color='lightcoral', label="Empirical CDF")
plt.plot(t, F_pareto, linestyle='-', color='lightgreen', label="Theoretical CDF")
plt.title('Pareto')
plt.legend()
plt.show()

# Erlang Distribution
k_erlang = 8
l_erlang = 0.8
u_erlang = np.random.rand(N, k_erlang)
X_erlang = (- np.sum(np.log(u_erlang), axis=1)) / l_erlang
X_erlang.sort()

cdf = np.zeros_like(t, dtype=float)
for i in range(k_erlang):
    cdf += ((l_erlang * t) ** i) / math.factorial(i)
F_erlang = 1 - cdf * np.exp(-l_erlang * t)

plt.plot(X_erlang, py, ".", color='lightcoral', label="Empirical CDF")
plt.plot(t, F_erlang, linestyle='-', color='lightgreen', label="Theoretical CDF")
plt.title('Erlang')
plt.legend()
plt.show()

# Hypo-Exponential Distribution
l1_hypo = 0.25
l2_hypo = 0.4
u1_hypo = np.random.rand(N)
u2_hypo = np.random.rand(N)
X_Hypo = -np.log(u1_hypo) / l1_hypo - np.log(u2_hypo) / l2_hypo
X_Hypo.sort()

F_Hypo = 1 - 1 / (l2_hypo - l1_hypo) * (l2_hypo * np.exp(-l1_hypo * t) - l1_hypo * np.exp(-l2_hypo * t))

plt.plot(X_Hypo, py, ".", color='lightcoral', label="Empirical CDF")
plt.plot(t, F_Hypo, linestyle='-', color='lightgreen', label="Theoretical CDF")
plt.title('Hypo-Exponential')
plt.legend()
plt.show()

# Hyper-Exponential Distribution
l1_hyper = 1
l2_hyper = 0.05
p1 = 0.75
p2 = 1 - p1
u1_hyper = np.random.rand(N)
u2_hyper = np.random.rand(N)

XHyper = np.where(u1_hyper < p1, -np.log(u2_hyper) / l1_hyper, -np.log(u2_hyper) / l2_hyper)
XHyper.sort()

FHyper = 1 - p1 * np.exp(-t * l1_hyper) - p2 * np.exp(-t * l2_hyper)

plt.plot(XHyper, py, ".", color='lightcoral', label="Empirical CDF")
plt.plot(t, FHyper, linestyle='-', color='lightgreen', label="Theoretical CDF")
plt.title('Hyper-Exponential')
plt.legend()
plt.show()
