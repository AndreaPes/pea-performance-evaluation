# Random Number Generation
___

### Overview
The goal is to generate random samples (N = 10000) for various distributions using a uniform random number generator and then compare the empirical distribution to the theoretical one. The distributions and parameters are as follows:

1. **Exponential Distribution**: λ = 0.25
2. **Pareto Distribution**: a = 2.5, m = 3
3. **Erlang Distribution**: k = 8, λ = 0.8
4. **Hypo-Exponential Distribution**: λ₁ = 0.25, λ₂ = 0.4
5. **Hyper-Exponential Distribution**: λ₁ = 1, λ₂ = 0.05, p₁ = 0.75

--- 

### Results

### Exponential Distribution
#### ✔️ Rate Parameter λ: <span style="color:lightgreen;font-weight:bold">0.25</span>
- **Empirical CDF**: The CDF derived from the generated samples is shown alongside the theoretical CDF.

![Exponential Distribution CDF](exp.png)

---

### Pareto Distribution
#### ✔️ Shape Parameter a: <span style="color:lightgreen;font-weight:bold">2.5</span>
#### ✔️ Scale Parameter m: <span style="color:lightgreen;font-weight:bold">3</span>
- **Empirical CDF**: The CDF derived from the generated samples is shown alongside the theoretical CDF.

![Pareto Distribution CDF](pareto.png)

---

### Erlang Distribution
#### ✔️ Shape Parameter k: <span style="color:lightgreen;font-weight:bold">8</span>
#### ✔️ Rate Parameter λ: <span style="color:lightgreen;font-weight:bold">0.8</span>
- **Empirical CDF**: The CDF derived from the generated samples is shown alongside the theoretical CDF.

![Erlang Distribution CDF](erlang.png)

---

### Hypo-Exponential Distribution
#### ✔️ Rate Parameters λ₁, λ₂: <span style="color:lightgreen;font-weight:bold">0.25, 0.4</span>
- **Empirical CDF**: The CDF derived from the generated samples is shown alongside the theoretical CDF.

![Hypo-Exponential Distribution CDF](hypo.png)

---

### Hyper-Exponential Distribution
#### ✔️ Rate Parameters λ₁, λ₂: <span style="color:lightgreen;font-weight:bold">1, 0.05</span>
#### ✔️ Probability p₁: <span style="color:lightgreen;font-weight:bold">0.75</span>
- **Empirical CDF**: The CDF derived from the generated samples is shown alongside the theoretical CDF.

![Hyper-Exponential Distribution CDF](hyper.png)

---

### Python Script

Python script that calculates all the above values and generates the graphs: [**A05.py**](A05.py)
