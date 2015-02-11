#!usr/bin/python
from collections import Counter

T=int(raw_input())
if T < 1 or T > 10:
	print "Constrains Violated"
	exit(0)
for i in range(T):
	N = int(raw_input())
	if N < 1 or N > 100000:
		print "Constrains Violated"
		exit(0)
	arr = raw_input().split()
	size = len(arr)
	if size < 1 or size > 100000:
		print "Constrains violated"
		exit(0)
#	arr.sort()
	counter = Counter(arr)
	counter = counter.values()
	foo = max(counter)
	minop =  size - foo
	print minop
