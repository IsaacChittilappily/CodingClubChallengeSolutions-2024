def singleNum(nums: list[int]) -> int:

  result = 0
  for num in nums:
    result ^= num

  return result

def main():

  nums = [1,2,3,3,4,2,1]
  print('Nums = ', nums)
  print('Single number =', singleNum(nums))

if __name__ == '__main__':
  main()