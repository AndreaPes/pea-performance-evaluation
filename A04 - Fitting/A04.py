import math
import numpy as np
from scipy.optimize import minimize
from scipy.special import gamma
from matplotlib import pyplot as plt

parameters_1 = {}
parameters_2 = {}


def calculate_trace_stats(trace):
    # The Mean
    mean = np.mean(trace)
    # The second Moment
    moment_2 = np.mean(trace ** 2)
    # The third Moment
    moment_3 = np.mean(trace ** 3)
    # The Variance
    variance = np.var(trace)
    # Coefficient of Variation
    cv = np.sqrt(variance) / mean

    stats = {
        'Mean': mean,
        'Second Moment': moment_2,
        'Third Moment': moment_3,
        'Variance': variance,
        'CV': cv
    }

    return stats


# Load data
trace1 = np.loadtxt('Trace1.csv', delimiter=',')
trace2 = np.loadtxt('Trace2.csv', delimiter=',')

stats_1 = calculate_trace_stats(trace1)
stats_2 = calculate_trace_stats(trace2)

t = np.r_[1:1001] / 10
N = len(trace1)
py = np.arange(1, N + 1, 1) / N

srt_1 = trace1.copy()
srt_2 = trace2.copy()
srt_1.sort()
srt_2.sort()


def fit_to_uniform(stats):
    a = stats['Mean'] - (1 / 2) * np.sqrt(12 * (stats['Second Moment'] - stats['Mean'] ** 2))
    b = stats['Mean'] + (1 / 2) * np.sqrt(12 * (stats['Second Moment'] - stats['Mean'] ** 2))
    return a, b


def uniform_cdf(a, b, x):
    return np.where(x < a, 0, np.where(x > b, 1, (x - a) / (b - a)))


def fit_to_exponential(stats):
    return 1 / stats['Mean']


def exponential_cdf(lam, x):
    return 1 - np.exp(-lam * x)


def fit_to_erlang(stats):
    k = int(np.round(1 / stats['CV'] ** 2))
    lam = k / stats['Mean']
    return k, lam


def erlang_cdf(k, lam, x):
    cdf = np.zeros_like(x, dtype=float)
    for i in range(k):
        cdf += ((lam * x) ** i) / math.factorial(i)
    return 1 - cdf * np.exp(-lam * x)


def fit_to_weibull(stats):
    def fun(x):
        l1 = x[0]
        k = x[1]

        M1d = l1 * gamma(1 + 1 / k)
        M2d = l1 ** 2 * gamma(1 + 2 / k)
        return np.abs(M1d / stats['Mean'] - 1) ** 2 + np.abs(M2d / stats['Second Moment'] - 1) ** 2

    initial_guess = np.array([0.001, 0.001])
    bounds = ((0.001, 100), (0.1, 100))
    result = minimize(fun, initial_guess, bounds=bounds)

    l1d = result.x[0]
    kd = result.x[1]

    return l1d, kd


def weibull_cdf(k, lam, x):
    return 1 - np.exp(-(x / lam) ** k)


def fit_to_pareto(stats):
    def fun(x):
        a = x[0]
        m = x[1]

        M1d = a * m / (a - 1)
        M2d = a * m ** 2 / (a - 2)

        return np.abs(M1d / stats['Mean'] - 1) ** 2 + np.abs(M2d / stats['Second Moment'] - 1) ** 2

    initial_guess = np.array([3, 1])
    bounds = ((1.1, 100.0), (0.001, 100.0))
    constraints = {
        'type': 'ineq',
        'fun': lambda x: x[1] - x[0] - 0.001
    }
    result = minimize(fun, initial_guess, bounds=bounds, constraints=constraints)

    ad = result.x[0]
    md = result.x[1]

    return ad, md


def pareto_cdf(alpha, xm, x):
    return np.where(x >= xm, 1 - (xm / x) ** alpha, 0)


def fit_to_hyper(stats, srt):
    def fun(x):
        l1 = x[0]
        l2 = x[1]
        p1 = x[2]
        p2 = 1 - p1

        return -np.sum(np.log(p1 * l1 * np.exp(-l1 * srt) + p2 * l2 * np.exp(-l2 * srt)))

    initial_guess = np.array([0.8 / stats["Mean"], 1.2 / stats["Mean"], 0.4])
    bounds = ((0.001, 100.0), (0.001, 100.0), (0.001, 0.999))
    constraints = {
        'type': 'ineq',
        'fun': lambda x: x[1] - x[0] - 0.001
    }

    result = minimize(fun, initial_guess, bounds=bounds, constraints=constraints)

    l1d = result.x[0]
    l2d = result.x[1]
    p1d = result.x[2]

    return l1d, l2d, p1d


def hyper_cdf(l1d, l2d, p1d):
    return 1 - p1d * np.exp(-t * l1d) - (1 - p1d) * np.exp(-t * l2d)


def fit_to_hypo(stats, srt):
    def fun(x):
        l1 = x[0]
        l2 = x[1]

        if l1 == l2:
            return -1000000 - l1 - l2
        else:
            return -np.sum(np.log(l1 * l2 / (l1 - l2) * (np.exp(-l2 * srt) - np.exp(-l1 * srt))))

    initial_guess = np.array([1 / (0.7 * stats["Mean"]), 1 / (0.3 * stats["Mean"])])
    bounds = ((0.001, 100.0), (0.001, 100.0))
    constraints = {
        'type': 'ineq',
        'fun': lambda x: x[1] - x[0] - 0.001
    }
    result = minimize(fun, initial_guess, bounds=bounds, constraints=constraints)

    l1d = result.x[0]
    l2d = result.x[1]

    return l1d, l2d


def hypo_cdf(l1d, l2d):
    return 1 - 1 / (l2d - l1d) * (l2d * np.exp(-l1d * t) - l1d * np.exp(-l2d * t))


# Uniform
parameters_1["Uniform Min"], parameters_1["Uniform Max"] = fit_to_uniform(stats_1)
parameters_2["Uniform Min"], parameters_2["Uniform Max"] = fit_to_uniform(stats_2)

F_uniform_1 = uniform_cdf(parameters_1["Uniform Min"], parameters_1["Uniform Max"], t)
F_uniform_2 = uniform_cdf(parameters_2["Uniform Min"], parameters_2["Uniform Max"], t)

# Exponential
parameters_1["Exp Rate"] = fit_to_exponential(stats_1)
parameters_2["Exp Rate"] = fit_to_exponential(stats_2)

F_exp_1 = exponential_cdf(parameters_1["Exp Rate"], t)
F_exp_2 = exponential_cdf(parameters_2["Exp Rate"], t)

# Erlang
parameters_1["Erlang Stages"], parameters_1["Erlang Rate"] = fit_to_erlang(stats_1)
parameters_2["Erlang Stages"], parameters_2["Erlang Rate"] = fit_to_erlang(stats_2)

F_erlang_1 = erlang_cdf(parameters_1["Erlang Stages"], parameters_1["Erlang Rate"], t)
F_erlang_2 = erlang_cdf(parameters_2["Erlang Stages"], parameters_2["Erlang Rate"], t)

# Weibull
parameters_1["Weibull Scale"], parameters_1["Weibull Shape"] = fit_to_weibull(stats_1)
parameters_2["Weibull Scale"], parameters_2["Weibull Shape"] = fit_to_weibull(stats_2)

F_weibull_1 = weibull_cdf(parameters_1["Weibull Shape"], parameters_1["Weibull Scale"], t)
F_weibull_2 = weibull_cdf(parameters_2["Weibull Shape"], parameters_2["Weibull Scale"], t)

# Pareto
parameters_1["Pareto Shape"], parameters_1["Pareto Scale"] = fit_to_pareto(stats_1)
parameters_2["Pareto Shape"], parameters_2["Pareto Scale"] = fit_to_pareto(stats_2)

F_pareto_1 = pareto_cdf(parameters_1["Pareto Shape"], parameters_1["Pareto Scale"], t)
F_pareto_2 = pareto_cdf(parameters_2["Pareto Shape"], parameters_2["Pareto Scale"], t)

# Hyper
parameters_1["Hyper First Rate"], parameters_1["Hyper Second Rate"], parameters_1["Hyper Probability 1"] = fit_to_hyper(
    stats_1, srt_1)
parameters_2["Hyper First Rate"], parameters_2["Hyper Second Rate"], parameters_2["Hyper Probability 1"] = fit_to_hyper(
    stats_2, srt_2)

F_hyper_1 = hyper_cdf(parameters_1["Hyper First Rate"], parameters_1["Hyper Second Rate"],
                      parameters_1["Hyper Probability 1"])
F_hyper_2 = hyper_cdf(parameters_2["Hyper First Rate"], parameters_2["Hyper Second Rate"],
                      parameters_2["Hyper Probability 1"])

# Hypo
parameters_1["Hypo First Rate"], parameters_1["Hypo Second Rate"] = fit_to_hypo(stats_1, srt_1)
parameters_2["Hypo First Rate"], parameters_2["Hypo Second Rate"] = fit_to_hypo(stats_2, srt_2)

F_hypo_1 = hypo_cdf(parameters_1["Hypo First Rate"], parameters_1["Hypo Second Rate"])
F_hypo_2 = hypo_cdf(parameters_2["Hypo First Rate"], parameters_2["Hypo Second Rate"])

# Print of all the parameters
for key, value in stats_1.items():
    print(f"{key}: {value}")
for key, value in parameters_1.items():
    print(f"{key}: {value}")
print()
for key, value in stats_2.items():
    print(f"{key}: {value}")
for key, value in parameters_2.items():
    print(f"{key}: {value}")


# Plotting
def plot_distribution(empirical, f_dist, title):
    plt.plot(empirical, py, linestyle='-', color='lightblue', label='Trace')
    plt.plot(t, f_dist, linestyle='-', color='lightcoral', label=title)
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(0, 50)
    plt.show()


# Plot distributions for Trace 1
plot_distribution(srt_1, F_uniform_1, "Uniform - Trace 1")
plot_distribution(srt_1, F_exp_1, "Exponential - Trace 1")
plot_distribution(srt_1, F_erlang_1, "Erlang - Trace 1")
plot_distribution(srt_1, F_weibull_1, "Weibull - Trace 1")
plot_distribution(srt_1, F_pareto_1, "Pareto - Trace 1")
plot_distribution(srt_1, F_hyper_1, "Hyper - Trace 1")
plot_distribution(srt_1, F_hypo_1, "Hypo - Trace 1")

# Plot distributions for Trace 2
plot_distribution(srt_2, F_uniform_2, "Uniform")
plot_distribution(srt_2, F_exp_2, "Exponential")
plot_distribution(srt_2, F_erlang_2, "Erlang")
plot_distribution(srt_2, F_weibull_2, "Weibull")
plot_distribution(srt_2, F_pareto_2, "Pareto")
plot_distribution(srt_2, F_hyper_2, "Hyper")
plot_distribution(srt_2, F_hypo_2, "Hypo")

# Combined plot with all distributions for Trace 1
plt.plot(srt_1, py, '-', label='Empirical CDF')
plt.plot(t, F_uniform_1, label='Uniform')
plt.plot(t, F_exp_1, label='Exponential')
plt.plot(t, F_erlang_1, label='Erlang')
plt.plot(t, F_weibull_1, label='Weibull')
plt.plot(t, F_pareto_1, label='Pareto')
plt.plot(t, F_hyper_1, label='Hyper')
plt.plot(t, F_hypo_1, label='Hypo')
plt.title("All Distributions CDF for Trace 1")
plt.xlim(0, 50)
plt.legend()
plt.show()

# Combined plot with all distributions for Trace 2
plt.plot(srt_2, py, '-', label='Empirical CDF')
plt.plot(t, F_uniform_2, label='Uniform')
plt.plot(t, F_exp_2, label='Exponential')
plt.plot(t, F_erlang_2, label='Erlang')
plt.plot(t, F_weibull_2, label='Weibull')
plt.plot(t, F_pareto_2, label='Pareto')
plt.plot(t, F_hyper_2, label='Hyper')
plt.plot(t, F_hypo_2, label='Hypo')
plt.title("All Distributions CDF for Trace 1")
plt.xlim(0, 50)
plt.legend()
plt.show()
