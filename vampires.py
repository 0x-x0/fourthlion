#!usr/bin/python
from collections import OrderedDict
from math import factorial

vampnum = []
res = 0

''' function to generate all permutations'''
def permutations(l):
    permutations=[]
    length=len(l)
    for x in xrange(factorial(length)):
        available=list(l)
        newPermutation=[]
        for radix in xrange(length, 0, -1):
            placeValue=factorial(radix-1)
            index=x/placeValue
            newPermutation.append(available.pop(index))
            x-=index*placeValue
        permutations.append(newPermutation)
    return permutations

''' function to convert list to a number'''
def listtonum(numList):         
    s = map(str, numList)   
    s = ''.join(s)          
    s = int(s)              
    return s


for x in range(1001,10000):
	vamplist = list(str(x))
	per = permutations(vamplist)		#get all permutations
	for li in per:
		lfang = li[0:2]					#left fang
		rfang = li[2:4]					#right fang
		lfang = listtonum(lfang)
		rfang = listtonum(rfang)
		res = lfang * rfang
		if res == x:
			vampnum.append(x)

vampnum = list(OrderedDict.fromkeys(vampnum))	# eliminate dups
print "Following are all 4-digit vampire numbers"  
for item in range(len(vampnum)):
	print vampnum[item]
