# M/M/c Models Analysis
___

### Overview

This report analyzes the performance of a server system handling jobs with different load conditions. The system initially has one server, then scales up to multiple servers, and finally migrates to the cloud with infinite scalability. Each configuration is modeled using different M/M/c queueing theories, where jobs arrive according to a Poisson process, and are served in a first-come-first-served manner.

The following analysis includes:
1. Utilization of the system.
2. Probability of having exactly two jobs in the system.
3. Probability of having fewer than five jobs in the system.
4. Average queue length.
5. Average response time.
6. Probability that the response time exceeds 2 seconds.
7. The 95th percentile of the response time distribution.

---

### Initial Configuration: Single Server (M/M/1 Queue)

- **Arrival Rate (λ)**: 1 job every 2 seconds (λ = 0.5 jobs/s)
- **Service Rate (μ)**: 1 job every 1.6 seconds (μ = 0.625 jobs/s)

#### Results:

- **Utilization**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Probability of Exactly 2 Jobs in System**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Probability of Less Than 5 Jobs in System**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Average Queue Length**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Average Response Time**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Probability Response Time > 2s**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **95th Percentile of Response Time**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>

---

### Second Configuration: Two Servers (M/M/2 Queue)

After one year, the load increases to **λ = 1 job/s**, making the single-server setup inadequate. A second server is added, and jobs are load-balanced between the two servers. This configuration is modeled as an **M/M/2 queue**.

#### Results:

- **Total Utilization**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Average Utilization per Server**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Probability of Exactly 2 Jobs in System**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Probability of Less Than 5 Jobs in System**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Average Queue Length**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Average Response Time**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>

---

### Third Configuration: Minimum Number of Servers for Stability (M/M/c Queue)

In the following year, the load increases further to **λ = 4 jobs/s**, making the two-server setup inadequate. The system administrator must determine the minimum number of servers **c** required to stabilize the system, and analyze its performance as an **M/M/c queue**.

#### Results:

- **Minimum Number of Servers (c)**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Total Utilization**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Average Utilization per Server**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Probability of Exactly 2 Jobs in System**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Probability of Less Than 5 Jobs in System**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Average Queue Length**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Average Response Time**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>

---

### Final Configuration: Cloud Migration with Infinite Scalability (M/M/∞ Queue)

Finally, the system migrates to the cloud, employing automatic scaling that provides an effectively infinite number of servers. This configuration is modeled as an **M/M/∞ queue** with an arrival rate of **λ = 10 jobs/s**.

#### Results:

- **Total Utilization**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Probability of Exactly 2 Jobs in System**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Probability of Less Than 5 Jobs in System**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>
- **Average Response Time**: <span style="color:lightgreen;font-weight:bold">_TBD_</span>

---

### Python Script

Python script that calculates all the above values: [**A09.py**](A09.py)
