def factorial(n: int) -> int:
  return 1 if n <= 1 else n * factorial(n-1)

factorials = {i: factorial(i) for i in range(10)}

def isCurious(n: int) -> bool:
  return sum(factorials[int(x)] for x in str(n)) == n

def main():
  
  print('This code takes a second to run...')
  print(sum(x for x in range(3, 2540160) if isCurious(x)))

if __name__ == '__main__':
  main()
