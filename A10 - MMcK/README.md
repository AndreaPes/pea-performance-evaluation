# M/M/c/K Models Analysis
___

### Overview

This report analyzes the performance of a web server system handling incoming requests with various configurations. Initially, the web server receives requests and serves them individually, but the system is limited in the number of requests it can handle simultaneously. Over time, the load increases, requiring additional servers to accommodate the growing demand.

The following analysis includes:
1. Utilization of the system.
2. Loss probability (probability that incoming requests are discarded).
3. Average number of jobs in the system.
4. Drop rate (rate of discarded requests).
5. Average response time.
6. Average waiting time in the queue.

---

### Initial Configuration: Single Server with Capacity Limit (M/M/1/K)

- **Arrival Rate (λ)**: 240 requests per minute
- **Service Rate (μ)**: 1 job every 200 milliseconds (μ = 300 jobs/min)
- **System Capacity (K)**: 16 requests

#### Results:

- **Utilization**: <span style="color:lightgreen;font-weight:bold">0.7954</span>
- **Loss Probability**: <span style="color:lightgreen;font-weight:bold">0.576%</span>
- **Average Number of Jobs in System**: <span style="color:lightgreen;font-weight:bold">3.6084</span>
- **Drop Rate**: <span style="color:lightgreen;font-weight:bold">1.382 req/min</span>
- **Average Response Time**: <span style="color:lightgreen;font-weight:bold">907.319 ms</span>
- **Average Queue Waiting Time**: <span style="color:lightgreen;font-weight:bold">707.319 ms</span>

---

### Second Configuration: Two Servers with Capacity Limit (M/M/2/K)

After one year, the load increases to **λ = 360 req/min**, making the single-server setup inadequate. A second server is added, along with a load balancer to distribute requests between the servers. This configuration is modeled as an **M/M/2/K** queue.

#### Results:

- **Total Utilization**: <span style="color:lightgreen;font-weight:bold">1.1998</span>
- **Average Utilization per Server**: <span style="color:lightgreen;font-weight:bold">0.5999</span>
- **Loss Probability**: <span style="color:lightgreen;font-weight:bold">0.0141%</span>
- **Average Number of Jobs in System**: <span style="color:lightgreen;font-weight:bold">1.8715</span>
- **Drop Rate**: <span style="color:lightgreen;font-weight:bold">0.051 req/min</span>
- **Average Response Time**: <span style="color:lightgreen;font-weight:bold">311.958 ms</span>
- **Average Queue Waiting Time**: <span style="color:lightgreen;font-weight:bold">111.958 ms</span>

---

### Final Configuration: Multi-Server System with Loss Probability Threshold (M/M/c/K)

If the workload increases further to **λ = 960 req/min**, the system administrator must determine the number of servers **c** required to maintain a loss probability below 1%. In this scenario, the system is modeled as an **M/M/c/K** queue.

#### Results:

- **Minimum Number of Servers (c)**: <span style="color:lightgreen;font-weight:bold">4</span>
- **Total Utilization**: <span style="color:lightgreen;font-weight:bold">3.1729</span>
- **Average Utilization per Server**: <span style="color:lightgreen;font-weight:bold">0.7932</span>
- **Loss Probability**: <span style="color:lightgreen;font-weight:bold">0.8475%</span>
- **Average Number of Jobs in System**: <span style="color:lightgreen;font-weight:bold">5.0632</span>
- **Drop Rate**: <span style="color:lightgreen;font-weight:bold">8.136 req/min</span>
- **Average Response Time**: <span style="color:lightgreen;font-weight:bold">319.153 ms</span>
- **Average Queue Waiting Time**: <span style="color:lightgreen;font-weight:bold">119.153 ms</span>

---

### Python Script

Python script that calculates all the above values: [**A10.py**](A10.py)