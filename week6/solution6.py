def moveZeroes(nums: list[int]) -> list[int]:
  
  return [num for num in nums if num] + nums.count(0) * [0]

def main():

  nums = [1,2,2,3,0,4,0,0,2,4,5,7,9]
  print('Nums = ', nums)
  print('New nums =', moveZeroes(nums))
  
  if __name__ == '__main__':
    main()