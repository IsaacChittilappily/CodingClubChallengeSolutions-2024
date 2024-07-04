def squareSum(n: int) -> int:

  return abs(sum([x**2 for x in range(n+1)]) - sum(x for x in range(n+1)) ** 2)


print(squareSum(100))