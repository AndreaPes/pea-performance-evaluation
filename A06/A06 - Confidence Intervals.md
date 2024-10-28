# Confidence Intervals
___

### Overview
This report examines two server scenarios where jobs are executed individually in arrival order without interruptions. The inter-arrival and service time distributions for each scenario are specified, and the performance indices are evaluated with 95% confidence intervals and a 2% relative error.

---

### Scenarios

#### Scenario I
- **Arrival Distribution**: Two-stage hyper-exponential
  - λ₁ = 0.025
  - λ₂ = 0.1
  - p₁ = 0.35
- **Service Distribution**: Weibull
  - Shape (k) = 0.333
  - Scale (λ) = 2.5

#### Scenario II
- **Arrival Distribution**: Erlang
  - Stages (k) = 8
  - Rate (λ) = 1.25
- **Service Distribution**: Uniform
  - Range: a = 1, b = 10

---

### Results

For each scenario, batches of M = 5000 jobs were used to compute the 95% confidence intervals of the following performance indices, with a 2% relative error.

#### Scenario I

- **Utilization**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Throughput**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Average Number of Jobs in System**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Average Response Time**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>

- **Number of Batches (K) for Required Accuracy**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>

#### Scenario II

- **Utilization**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Throughput**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Average Number of Jobs in System**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Average Response Time**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>

- **Number of Batches (K) for Required Accuracy**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>

---

### Graphs

For each scenario, figures show the confidence intervals for the performance indices.

- **Scenario I**
  ![Confidence Intervals - Scenario I](scenario_i.png)

- **Scenario II**
  ![Confidence Intervals - Scenario II](scenario_ii.png)

---

### Python Script

Python script that calculates all the above values and generates the graphs: [**A06.py**](A06.py)
