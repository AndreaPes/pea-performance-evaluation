# Basic Performance Evaluation
___

### Overview
The enclosed files [Logger1.csv](Logger1.csv) and [Logger2.csv](Logger2.csv) are the same as the two columns in Example 1. They represent, respectively, the inter-arrival time between two requests to a server, and the service time required by each request. The value is expressed in minutes.

---

### Results

#### ✔️ Maximum Arrival Rate (expressed in [cars/min.])
Consider an increase in the workload, that reduces the inter-arrival time by a fraction 𝑎, that is:  
𝑎′𝑖 = 𝛼 ∙ 𝑎𝑖  

Which is the maximum arrival rate [expressed in jobs per minute] that can be handled with an average response time of 20 minutes?  

<span style="color:lightgreen;font-weight:bold">0.3615 cars/min</span>

#### ✔️ Required Service Time Reduction
Consider now a fraction 𝑎 that produces an arrival rate of 1.2 jobs per minute.

Which should be the fraction 𝛽 at which we must reduce the service time, i.e.  
𝑠′𝑖 = 𝛽 ∙ 𝑠𝑖  
so that the average response time is less than 15 minutes?  

<span style="color:lightgreen;font-weight:bold">0.3194</span>

---

### Python Script

Python script that calculates the results for these questions: [**A02.py**](A02.py)
