# Fitting
___

### Overview
The enclosed files [Trace1.csv](Trace1.csv) and [Trace2.csv](Trace2.csv) contain a single column that reports the service times of two different file servers.

---

### Results

### Trace1

#### ✔️ Mean: <span style="color:lightgreen;font-weight:bold">5.4948</span>

#### ✔️ Second Moment: <span style="color:lightgreen;font-weight:bold">36.4073</span>

#### ✔️ Third Moment: <span style="color:lightgreen;font-weight:bold">294.3437</span>

#### ✔️ Variance: <span style="color:lightgreen;font-weight:bold">6.2141</span>

#### ✔️ Coefficient of Variation: <span style="color:lightgreen;font-weight:bold">0.4537</span>

#### ✔️ Fit to Uniform Distribution: <span style="color:lightgreen;font-weight:bold">Min: 1.1771, Max: 9.8125</span>

#### ✔️ Fit to Exponential Distribution: <span style="color:lightgreen;font-weight:bold">Rate: 0.1820</span>

#### ✔️ Fit to Erlang Distribution: <span style="color:lightgreen;font-weight:bold">Stages: 5, Rate: 0.9099</span>

#### ✔️ Fit to Weibull Distribution: <span style="color:lightgreen;font-weight:bold">Scale: 6.2009, Shape: 2.3419</span>

#### ✔️ Fit to Pareto Distribution: <span style="color:lightgreen;font-weight:bold">Shape: 3.4197, Scale: 3.8888</span>

#### ✔️ Fit to Two-Stage Hyper-Exponential Distribution: <span style="color:lightgreen;font-weight:bold">First Rate: 0.1810, Second Rate: 0.1820, Probability 1: 0.0010</span>

#### ✔️ Fit to Two-Stage Hypo-Exponential Distribution: <span style="color:lightgreen;font-weight:bold">First Rate: 0.3635, Second Rate: 0.3645</span>

---

### Trace2

#### ✔️ Mean: <span style="color:lightgreen;font-weight:bold">3.6139</span>

#### ✔️ Second Moment: <span style="color:lightgreen;font-weight:bold">469.5959</span>

#### ✔️ Third Moment: <span style="color:lightgreen;font-weight:bold">941390.0074</span>

#### ✔️ Variance: <span style="color:lightgreen;font-weight:bold">456.5358</span>

#### ✔️ Coefficient of Variation: <span style="color:lightgreen;font-weight:bold">5.9124</span>

#### ✔️ Fit to Uniform Distribution: <span style="color:lightgreen;font-weight:bold">Min: -33.3943, Max: 40.6221</span>

#### ✔️ Fit to Exponential Distribution: <span style="color:lightgreen;font-weight:bold">Rate: 0.2767</span>

#### ✔️ Fit to Erlang Distribution: <span style="color:lightgreen;font-weight:bold">Stages: 0, Rate: 0.0</span>

#### ✔️ Fit to Weibull Distribution: <span style="color:lightgreen;font-weight:bold">Scale: 0.3231, Shape: 0.2880</span>

#### ✔️ Fit to Pareto Distribution: <span style="color:lightgreen;font-weight:bold">Shape: 2.0175, Scale: 2.0185</span>

#### ✔️ Fit to Two-Stage Hyper-Exponential Distribution: <span style="color:lightgreen;font-weight:bold">First Rate: 0.0726, Second Rate: 0.7515, Probability 1: 0.1834</span>

#### ✔️ Fit to Two-Stage Hypo-Exponential Distribution: <span style="color:lightgreen;font-weight:bold">First Rate: 0.3953, Second Rate: 0.9224</span>

---

### Graphs

#### ✔️ Empirical CDF Comparison
For each trace, draw a figure comparing the empirical CDF with the CDFs of the fitted distributions.

- **Trace1**
  ![Trace1 CDF Comparison](all_CDF_trace1.png)

- **Trace2**
  ![Trace2 CDF Comparison](all_CDF_trace2.png)

---

### Python Script

Python script that calculates all the above values and generates the graphs: [**A04.py**](A04.py)
