# Week 6 - Move Zeroes - 18/06/24

### Solution:

I saw many weird and wonderful attempts to solve this question, some of which were innovative, other which were confusing, over-engineered and wayy longer than they could have been, seeing as this problem can actually be solved with a one-liner!

But before we get there, lets understand the problem first.

This problem is based around list manipulation - can you move around items in a list. But remember the one constraint of the question - the elements of the list must remain in the same order. This eliminates any method that would involve sorting, (which I saw some people using) because sorting will immediately lose the original order of the list.

Lets decompose the problem - first we need to remove all the 0's from the list, and then we need to add them back onto the end of the list.

Removing the 0's is simple - we can loop through the list, and if the number is 0, then we remove it using the .remove() method:
```
for num in nums:
  if num == 0:
    nums.remove(0)
```
And then if we want to subsequently add this 0 to the end of the list, we can use the .append() method.

```
for num in nums:
  if num == 0:
    nums.remove(0)
    nums.append(0)
```

This code works fine, and has O(n) time complexity. However, we can do better. The .remove() method is rather resource intensive (as it needs to search through the whole list to find a 0), so instead, lets first make a new list with all the numbers that are NOT 0, by using list comprehension:
```
noZeroes = [num for num in nums if num != 0]
```
List comprehension is known to be more efficient than basic loops, so this increases our efficiency. Now that we have a list with all the non-zero numbers, we just need to get a list with n zeroes in it, where n is the number of zeros in the original list.
```
zeroes = nums.count(0) * [0]
```
Here, we're using nums.count(0) to count the number of 0's in the list originally, and then we're multiplying the list [0] by that count. Remember that lists can be multiplied just like you'd think - [0] * 5 = [0,0,0,0,0]. 

After that we just need to add the two lists together - adding one list to another will append one list to the end of the other one.

```
return noZeroes + zeroes
```

But of course, we can just make this into a one-liner by removing the variables and just returning the result of the operations directly:

```
return [num for num in nums if x != 0] + nums.count(0) * [0]
```

And there you have it -  a nice little one line solution.