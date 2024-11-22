# Basic Performance Indices and Workloads
___

### Overview
The enclosed files [Logger1.csv](Logger1.csv) and [Logger2.csv](Logger2.csv) are two log files taken from a sensor monitoring the flow of cars in a traffic road section. Cars first pass through the first sensor, then through the second. The road segment is single lane, so no overtaking is possible. The values are expressed in minutes.

---

### Results

#### ✔️ Arrival Rate and Throughput (expressed in [cars/min.]): <span style="color:lightgreen;font-weight:bold">1.5693 cars/min</span>

#### ✔️ Average Inter-Arrival Time (expressed in [min.]): <span style="color:lightgreen;font-weight:bold">0.6370 min</span>

#### ✔️ Utilization: <span style="color:lightgreen;font-weight:bold">92.41%</span>

#### ✔️ Average Service Time (expressed in [min.]): <span style="color:lightgreen;font-weight:bold">0.5889 min</span>

#### ✔️ Average Number of Jobs: <span style="color:lightgreen;font-weight:bold">10.6820 jobs</span>

#### ✔️ Average Response Time (expressed in [min.]): <span style="color:lightgreen;font-weight:bold">6.8068 min</span>

---

### Graphs

#### ✔️ Distribution of the Number of Cars in the Road Segment (from 0 to 25)
![Car Distribution](number_f_cars_distribution.png)

#### ✔️ Response Time Distribution (between 1 and 40 minutes, with a granularity of 1 min.)
![Response Time Distribution](response_time_distribution.png)

#### ✔️ Service Time Distribution (between 0.1 and 5 minutes, with a granularity of 0.1 minutes)
![Service Time Distribution](service_time_distribution.png)

---

### Python Script

Python script that calculated all the above values and generated the graphs: [**A01.py**](A01.py)
