def moveZeroes(nums: list[int]) -> list[int]:
  
  return [x for x in nums if x != 0] + nums.count(0) * [0]
  