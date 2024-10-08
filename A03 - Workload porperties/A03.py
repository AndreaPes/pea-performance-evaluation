import numpy as np
import matplotlib.pyplot as plt


def calculate_trace_stats(trace, trace_name):
    """
    Calculate the required statistics for a given input.

    Args:
        trace (ndarray): Array of inter-arrival times (trace data).
        trace_name (str): Name of the trace file for labeling outputs.

    Returns:
        dict: Calculated statistics.
    """

    # The Mean
    mean = np.mean(trace)
    # The second Moment
    moment_2 = np.mean(trace ** 2)
    # The third Moment
    moment_3 = np.mean(trace ** 3)
    # The fourth Moment
    moment_4 = np.mean(trace ** 4)

    # The Variance
    var = np.mean((trace - mean) ** 2)
    # The third Central Moment
    central_moment_3 = np.mean((trace - mean) ** 3)
    # The fourth Central Moment
    central_moment_4 = np.mean((trace - mean) ** 4)

    # The Standard Deviation
    standard_deviation = np.sqrt(var)

    # The Skewness
    skewness = np.mean(((trace - mean) / standard_deviation) ** 3)
    # The fourth Standardized Moment
    standardized_moment_4 = np.mean(((trace - mean) / standard_deviation) ** 4)

    # The Coefficient of Variation
    coeff_of_variation = standard_deviation / mean
    # The Excess Kurtosis
    excess_kurtosis = standardized_moment_4 - 3

    # The first Quartile
    quartile_1 = np.percentile(trace, 25)
    # The Median
    median = np.median(trace)
    # The third Quartile
    quartile_3 = np.percentile(trace, 75)
    # The fifth Percentile
    percentile_5 = np.percentile(trace, 5)
    # The ninetieth Percentile
    percentile_90 = np.percentile(trace, 90)

    stats = {
        'Mean': mean,
        'Second Moment': moment_2,
        'Third Moment': moment_3,
        'Fourth Moment': moment_4,
        'Variance': var,
        'Third Central Moment': central_moment_3,
        'Fourth Central Moment': central_moment_4,
        'Skewness': skewness,
        'Fourth Standardized Moment': standardized_moment_4,
        'Standard Deviation': standard_deviation,
        'Coefficient of Variation': coeff_of_variation,
        'Excess Kurtosis': excess_kurtosis,
        '1st Quartile': quartile_1,
        'Median': median,
        '3rd Quartile': quartile_3,
        '5th Percentile': percentile_5,
        '90th Percentile': percentile_90
    }

    # Print the results
    print(trace_name)
    for key, value in stats.items():
        print(f"{key}: {value}")
    print()

    # The minimum value for Lag
    min_lag = 1
    # The maximum value for Lag
    max_lag = 100
    correlations = []
    # The size of the trace
    N = len(trace)

    for m in range(min_lag, max_lag + 1):
        correlations.append(((trace[m:] - mean) * (trace[:-m] - mean)).sum() / ((N - m) * var))

    # Plot of the Pearson Correlation Coefficients for Lags from 1 to 100
    lags = np.arange(min_lag, max_lag + 1)
    plt.plot(lags, correlations, linestyle='-', color='skyblue')
    plt.title(f'Pearson Correlation Coefficient for Lags (1 to 100) - {trace_name}')
    plt.xlabel('Lag')
    plt.ylabel('Pearson Correlation Coefficient')
    plt.grid(True)
    plt.show()

    sorted_trace = np.copy(trace)
    sorted_trace.sort()

    py = np.arange(1, N + 1, 1) / N

    plt.plot(sorted_trace, py, linestyle='-', color='lightcoral')
    plt.title(f'Approximated CDF - {trace_name}')
    plt.xlabel('Values')
    plt.ylabel('CDF approximated value')
    plt.grid(True)
    plt.show()

    return stats


# Load the data from the files
trace1 = np.loadtxt('Trace1.csv', delimiter=',')
trace2 = np.loadtxt('Trace2.csv', delimiter=',')
trace3 = np.loadtxt('Trace3.csv', delimiter=',')

trace1_stats = calculate_trace_stats(trace1, "Trace1")
trace2_stats = calculate_trace_stats(trace2, "Trace2")
trace3_stats = calculate_trace_stats(trace3, "Trace3")
