import math
from math import exp
from math import sqrt
from math import log
from math import cos
from math import sin
from decimal import Decimal, getcontext

getcontext().prec = 102

def riemann(h,r):
    i=exp(h)*cos(r)
    j=exp(h)*sin(r)
    return i, j

b=1
c=1

total_ta = 0
total_tb = 0

for n in range (1,100000):
    h=-b*log(n)
    r=-c*log(n)
    i, j = riemann(h,r)
    total_ta += i
    total_tb += j
print(total_ta,total_tb)