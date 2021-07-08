from math import * 
A = float(input()) 
T = floor(A) 
P = A - T 
T100 = T50= T20 = T10 = T5 = T2 = T1 = P50 = P25 = P10 = P5 = P1 = 0 
if A>=100: 
    T100 = int(A/100) 
    A = A%100 
if A>=50: 
   T50 = int(A/50) 
   A = A%50 
if A>=20: 
   T20 = int(A/20) 
   A = A%20 
if A>=10: 
   T10 = int(A/10) 
   A = A%10 
if A>=5: 
   T5 = int(A/5) 
   A = A%5 
if A>=2: 
   T2 = int(A/2) 
   A = A%2 
if A>=1: 
   T1 = int(A/1) 
   A = A%1 
if A>=0.5: 
   P50 = int(A/0.5) 
   A = A%0.5 
if A>=0.25: 
   P25 = int(A/0.25) 
   A = A%0.25 
if A>=0.10: 
   P10 = int(A/0.10) 
   A = A%0.10 
if A>=0.05: 
   P5 = int(A/0.05) 
   A = A%0.05 
else: 
  P1 = int(A/0.01) 
print("NOTAS:") 
print("%d nota(s) de R$ 100.00" % T100) 
print("%d nota(s) de R$ 50.00" % T50) 
print("%d nota(s) de R$ 20.00" % T20) 
print("%d nota(s) de R$ 10.00" % T10) 
print("%d nota(s) de R$ 5.00" % T5) 
print("%d nota(s) de R$ 2.00" % T2) 
print("MOEDAS:") 
print("%d moeda(s) de R$ 1.00" % T1) 
print("%d moeda(s) de R$ 0.50" % P50) 
print("%d moeda(s) de R$ 0.25" % P25) 
print("%d moeda(s) de R$ 0.10" % P10) 
print("%d moeda(s) de R$ 0.05" % P5) 
print("%d moeda(s) de R$ 0.01" % P1)