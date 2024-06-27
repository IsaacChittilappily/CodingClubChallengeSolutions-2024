def evenSum(nums):
  return sum([num for num in nums if num % 2 == 0])

def addOther(nums, add):
  return [num + add for index, num in enumerate(nums) if index % 2 == 0]

def shiftList(nums, shift):
  return nums[-shift:] + nums[:-shift]



list = [1,2,3,5,6,8,10]

print(evenSum(list))
print(addOther(list, 4))
print(shiftList(list, 3))