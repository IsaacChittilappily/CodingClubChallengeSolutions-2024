def moveZeroes(nums: list[int]) -> list[int]:
  
  return [num for num in nums if x != 0] + nums.count(0) * [0]

def main():

  nums = []
  print('Nums = ', nums)
  print('New nums =', moveZeroes(nums))
  
  if __name__ == '__main__':
    main()