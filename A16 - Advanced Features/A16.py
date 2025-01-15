# Data From Simulation Result
SYSTEM_THROUGHPUT = 0.0794 # job/s
SYSTEM_RESPONSE_TIME = 605.7936 # s
THINK_TIME = 10 # min
UTILIZATION_NODE1 = 0.00438
UTILIZATION_NODE2 = 0.00679
NODE1_THREADS = 32
NODE2_THREADS = 24
QUEUE_TIME = 1.2185
ARRIVAL_RATE = 38.3214

print("Average Response TIme of one Job [s]: ", SYSTEM_RESPONSE_TIME - (THINK_TIME * 60))
print("System Throughput [job/min]: ", SYSTEM_THROUGHPUT * 60)
print("Total Utilization of Node 1 [%]: ", UTILIZATION_NODE1 * NODE1_THREADS * 100)
print("Total Utilization of Node 2 [%]: ", UTILIZATION_NODE2 * NODE2_THREADS * 100)
print("Average Number of Tasks Waiting to enter the System: ", QUEUE_TIME * ARRIVAL_RATE)
