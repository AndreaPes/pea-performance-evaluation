# Terminal as Reference Station

X = 0.3755
XA = 0.0367
XB = 0.0055
XC = 0.3333
RA = 535.4408
RB = 540.6370
RC = 243.2171

R = (XA * RA + XB * RB + XC * RC) / X
print("Average System Response Time if Terminal as Reference Station:", R)

# Web Server as Reference Station

RA = 97.6016
RB = 253.7903
RC = 243.2171

R = (XA * RA + XB * RB + XC * RC) / X
print("Average System Response Time if Web Server as Reference Station:", R)
