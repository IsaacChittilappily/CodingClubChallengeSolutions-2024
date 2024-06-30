def evenSum(nums: list[int]) -> int:
  return sum([num for num in nums if num % 2 == 0])

def addOther(nums: list[int], add: int) -> list[int]:
  return [num + add for index, num in enumerate(nums) if index % 2 == 0]

def shiftList(nums: list[int], shift: int) -> list[int]:
  return nums[-shift:] + nums[:-shift]



list = [1,2,3,5,6,8,10]

print(evenSum(list))
print(addOther(list, 4))
print(shiftList(list, 3))