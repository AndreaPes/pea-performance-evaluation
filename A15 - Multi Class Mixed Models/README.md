# Multi-class Mixed Models Analysis
___

### Overview

This report evaluates the performance of a warehouse management system handling orders from three types of users: **customers**, **employees**, and **maintainers**. Each class interacts with the system's resources—web server, checkout service, warehouse, and packing facility—with distinct usage patterns.

The analysis addresses the following performance metrics:

1. **Utilization of the four stations (excluding terminals).**
2. **Average number of users in the system for customers, employees, and maintainers.**
3. **Average number of users in the web server.**
4. **Average system response time for customers, employees, and maintainers.**
5. **Throughput of the warehouse.**
6. **Class-independent average number of jobs in the system (N).**
7. **Class-independent average system response time (R), excluding the think-time.**

---

### System Diagram

![System Diagram](a15_graph.png)

---

### Results

#### 1. Utilization of the Stations

- **Web Server Utilization**: <span style="color:lightgreen;font-weight:bold">0.9999</span>
- **Checkout Service Utilization**: <span style="color:lightgreen;font-weight:bold">0.8333</span>
- **Warehouse Utilization**: <span style="color:lightgreen;font-weight:bold">0.8817</span>
- **Packing Facility Utilization**: <span style="color:lightgreen;font-weight:bold">0.1375</span>

#### 2. Average Number of Users in the System per Class

- **Customers (N_c)**: <span style="color:lightgreen;font-weight:bold">81.0724</span>
- **Employees (N_e)**: <span style="color:lightgreen;font-weight:bold">20.0000</span>
- **Maintainers (N_m)**: <span style="color:lightgreen;font-weight:bold">3.0000</span>

#### 3. Average Number of Users in the Web Server

- **Web Server (N_ws)**: <span style="color:lightgreen;font-weight:bold">94.0905</span>

#### 4. Average System Response Time per Class

- **Customers (R_c)**: <span style="color:lightgreen;font-weight:bold">243.2171</span>
- **Employees (R_e)**: <span style="color:lightgreen;font-weight:bold">535.4408</span>
- **Maintainers (R_m)**: <span style="color:lightgreen;font-weight:bold">540.6370</span>

#### 5. Throughput of the Warehouse

- **Warehouse Throughput**: <span style="color:lightgreen;font-weight:bold">0.0330</span>

#### 6. Class-Independent Average Number of Jobs in the System

- **Average Number of Jobs (N)**: <span style="color:lightgreen;font-weight:bold">104.0724</span>

#### 7. Class-Independent Average System Response Time

- **Average System Response Time (R)**: <span style="color:lightgreen;font-weight:bold">276.1343</span>

---

### Python Script

Python script that calculates all the above values: [**A15.py**](A15.py)
