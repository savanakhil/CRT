def Collatz_Sequence(n):
   sequence = []
    
   while n >= 1:
      sequence.append(n)
        
      if n == 1:
         break
      elif n % 2 == 0:
         n = n // 2
      else:
         n = 3 * n + 1
    
   return sequence



def Collatz_Sequence(n: int)-> List:
   pass
if __name__ == '__main__':
   n = int(input())
   print(Collatz_Sequence(n))