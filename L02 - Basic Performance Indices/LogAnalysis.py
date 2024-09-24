import numpy as np
import matplotlib.pyplot as plt

# loads the traces
intrace = np.loadtxt("LogFile.csv",delimiter=";")
inrows = intrace.shape[0]

# A(T) is created summing the inter-arrival times
A_T = np.zeros((inrows,1))
A_T[:,0] = np.cumsum(intrace[:,0])  # np.cumsum() sums the element of intrace

# C(T) is created using either the completion of the previous job, or the arrival time
C_T = np.zeros((inrows,1))
C_T[0,0] = intrace[0,1] + A_T[0,0]
for i in range(1, inrows):
    C_T[i,0] = max(C_T[i-1,0], A_T[i,0]) + intrace[i,1]

## plots the arrival and departure curves    
plt.plot(A_T[0:250,0], np.r_[0:250]);
plt.plot(C_T[0:250,0], np.r_[0:250]);
plt.show()

## defines the total time, as the arrival time of the last job.
## many alternative definitions are possible
T = A_T[-1,0]
## Computes the basic performance indices
B = np.sum(intrace[:,1]) ## since here the second column of "intrace" are service times
U = B / T
X = inrows / T ## since the number of rows of "intrace" represents the completed jobs
S = U / X

## compute the response time of the jobs in r_i
r_i = C_T - A_T
R = np.mean(r_i)
## The number of jobs is computed using Little's law
N = X * R 

## compute the P(R>15) as the fraction of jobs where r_i > 15, given by np.sum(r_i > 15)
pRg15 = np.sum(r_i > 15) / inrows

## prints the results
print("T = ", T)
print("B = ", B)
print("U = ", U)
print("X = ", X)
print("S = ", S)
print("R = ", R)
print("N = ", N)
print("p(R > 15) = ", pRg15)

## creates in AC_T a 2 * inrows array where the first column represents the t_i
## in slide 20 of lesson 2, and in the second column +1 for arrival, and -1 for service
AC_T = np.block([[A_T, np.ones((inrows,1))],[C_T, -np.ones((inrows,1))]])
AC_T = AC_T[AC_T[:, 0].argsort()]
## by summing the second column, computes the number of jobs in each time segment
AC_T[:,1] = np.cumsum(AC_T[:,1])

## dTN_T is a matrix that contains in the first row the time spent with the number
## specified in the second column
dTN_T = (np.c_[[AC_T[1:-1,0] - AC_T[0:-2,0], AC_T[:-2,1]]]).T

## in this case, too increase the precision a little bit, T is defined as the sum of times
## in the first column of dTN_T, which due to its definition can be computed more
## efficiently as the difference between the time of the last departure
## and the time of the first arrival
TforP = AC_T[-1,0] - AC_T[0,0]

## Plots the queue length distribution
PN = [0]*26
PNL = [0]*26
for i in range(0,26):
    PNL[i] = i
    PN[i] = np.sum(dTN_T[dTN_T[:,1] == i,0]) / TforP
    
plt.bar(PNL, PN)    
plt.show()

## Plots the response time distribution
PR  = [0]*101
PRT = [0]*101
for i in range(0,101):
    t = i / 10
    PRT[i] = t
    PR[i] = sum(r_i < t) / inrows
    
plt.plot(PRT, PR);
plt.show()
    