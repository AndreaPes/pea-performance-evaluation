# G/G/c Queue Models Analysis
___

### Overview

This report analyzes the performance of a web server system that receives jobs with varying load conditions. Initially, jobs are served following an Erlang distribution. After a year, the traffic increases in both rate and variability, and the job duration can be modeled using a Hyper-Exponential distribution. The system's capacity is expanded with additional servers and a load-balancer that ensures requests are handled efficiently.

The following analysis includes:
1. Utilization of the system.
2. Average response time.
3. Average number of jobs in the system.
4. Minimum number of servers required for stability.

---

### Initial Configuration: Erlang Service (G/G/c Queue)

The web server initially receives jobs according to a **Poisson process** with rate **λ = 20 jobs/s**. The service time is distributed according to an **Erlang distribution** with rate **λe = 100 jobs/s** and **k = 4**.

#### Results:

- **Utilization**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Average Response Time**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Average Number of Jobs in System**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>

---

### Second Configuration: Increased Traffic and Variability (G/G/c Queue)

After a year, the traffic rate and variability increase, and the service time is now modeled with a **Hyper-Exponential distribution** with **λ₁ = 40 jobs/s**, **λ₂ = 240 jobs/s**, and **p₁ = 80%**. To manage the increased load, new servers are added along with a **load-balancer** that holds requests in a single queue and dispatches them to the first available server.

#### Results:

- **Minimum Number of Servers (c)**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Average Utilization of the System**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Approximate Average Response Time**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Approximate Average Number of Jobs in System**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>

---

### Python Script

Python script that calculates all the above values: [**A11.py**](A11.py)

---