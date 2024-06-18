# Week 5 - Single Number - 11/06/24

### Solution

There are multiple ways to approach this problem, but there is only one which is the most efficient. For example, one approach would be just to iterate through the whole list and check the 'count' of each number in the list - as soon as we find a count of 1, then we know we've found our number.

```
for num in nums:
  if nums.count(num) == 1:
    return num

```

This works fine, and even quite well since it has O(n) time. This would be acceptable for the first part of the problem. However, for the second part of the problem, we need a more efficient solution, one that doesnt use an if statement at all.

We can in fact solve this using the XOR operator in Python.

An XOR (exclusive OR) is a type of logic gate, which takes 2 binary inputs and gives one binary output.

XOR's work like this:

A|B|Output\
0|0|0\
0|1|1\
1|0|1\
1|1|0

A and B are the inputs (in binary), and the output is shown next to them. XOR outputs 1 if either of the two inputs are 1, but not both. So 00 outputs 0 (because neither input is 1), 01 and 10 output 1, (because one input is 1), and 11 outputs 0, (because both inputs are 1). This differs from a regular OR gate because a that would output 1 if the input was 11.

Now, why is this useful? Well, Python actually has a built-in bitwise operator for all of the common logic gates - the XOR operator is ^. (Yea, you all thought that was the exponential operation right?)

Now comes the tricky part - implementing the XOR gate to solve the problem. 

Lets take an example array of [1,1,2,3,3]\
And a starting variable that we'll call result, which starts at 0

Now, lets loop through this array and apply the XOR function to 'result' and the item we are currently on. (I've kept track of the value stored in 'result' for each iteration)

Iteration 1: result = 0\
result = 0 ^ 1 = 1

Iteration 2: result = 1\
result = 1 ^ 1 = 0

Iteration 3: result = 0\
result = 0 ^ 2 = 2

Iteration 4: result = 2\
result = 2 ^ 3 = 2 (the value doesnt change as both of the inputs are not 0)

Iteration 5: result = 2\
result = 2 ^ 3 = 2

Now that we have looped through the list, our final value stored in result is 2, which is indeed the single number in the list.

Notice how when there is a pair of numbers that are the same, the XOR operator 'cancels' them out and ends up at 0 again? This is the weird quirk of the XOR operator allows us to solve this problem. 

The code looks like this:
```
for num in nums:
  result ^= num
```

And with this, we have sucessfully solved the problem without needing the if statement, and staying within the bounds of constant space complexity and linear time complexity.