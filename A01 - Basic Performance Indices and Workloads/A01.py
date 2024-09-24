import numpy as np
import matplotlib.pyplot as plt

# Caricare i dati dai file CSV
data_logger1 = np.loadtxt('Logger1.csv', delimiter=',')
data_logger2 = np.loadtxt('Logger2.csv', delimiter=',')

# Verificare i dati caricati
print("Logger1 data:", data_logger1)
print("Logger2 data:", data_logger2)

# Total Time
T = data_logger2[-1] - data_logger1[0]
print("Total time:", T)

# Number of cars
num_cars = len(data_logger1)
print("Number of cars:", num_cars)

# Arrival rate
A_T = num_cars/T
print("Average time per car:", A_T)