#! /usr/bin/env python3.3
import math

result = 0

for i in range(2520,math.factorial(20),20):
	for d in [4,6,8,9,10,11,12,13,14,15,16,17,18,19,20]:
		if i % d != 0:
			break
		elif d == 20:
			result = i
	if result > 0: break

print( result )
