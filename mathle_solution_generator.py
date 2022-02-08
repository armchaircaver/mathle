"""
generates all the valid solutions for mathle, to use in a solver

finds solutions of the form
a x b = c, where a,b,c are numbers and x is an operator + or -
assumptions:

- a is positive.

- none of the components a,b,c is zero

- c is positive 

"""
from itertools import product
import sys

def generate_solutions():

  for a in range(1,1000):
    for b in range(10**(3-len(str(a))), 10**(4-len(str(a)))):

      r = str(a+b).zfill(3)
      if len(r) == 3:
         yield str(a) + '+' + str(b) + '=' + r

      if a>b:
        r = str(a-b).zfill(3)
        if len(r) == 3:
           yield str(a) + '-' + str(b) + '=' + r
    
#-----------------------------------------------------------------------------
def bitmap(word):
  return sum( 2**(ord(c)) for c in set(word) )


from time import perf_counter

f = open('mathledict.py', 'w')
sys.stdout = f

print ( "mathleDict = {" )
starttime= perf_counter()
count=0
for x in generate_solutions():
  count+=1
  print ( '"'+ x + '" :' + str(bitmap(x))+',' )
endtime= perf_counter()
print('}')

print ("#total expressions: ", count, ", ", endtime-starttime,"sec")

f.close()
