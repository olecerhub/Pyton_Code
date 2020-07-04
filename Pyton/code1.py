import math

x = 11
y = (math.exp( -x )-4*math.log10(x))/(math.log(x)-math.cos(math.fabs(x+1)))
print(y)
