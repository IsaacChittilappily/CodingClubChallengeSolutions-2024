def factorial(n: int) -> int:
  return 1 if n <= 1 else n * factorial(n-1)


def isCurious(n: int):
  return sum([factorial(int(x)) for x in str(n)]) == n

def main():
  # the longest number that can be curious is 7 digits long
  print('This code takes a minute to run...')
  print(sum([x for x in range(3, 9999999) if isCurious(x)]))

if __name__ == '__main__':
  main()
