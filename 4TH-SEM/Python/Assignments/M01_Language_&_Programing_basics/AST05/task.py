from typing import List 
def Collatz_Sequence(n: int)-> List[int]:
   Sequence = [n]
   while n!=1:
      if n%2==0:
         n=n//2 
      else:
         n=3*n+1 
      Sequence.append(n)
   return Sequence
