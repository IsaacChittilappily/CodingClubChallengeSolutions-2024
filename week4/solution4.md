# Week 4 - Digit Factorials - 04/06/24:
## Solution:

Alright, this week's problem can definitely seem a little tricky, but after some **decomposition** into logical steps, it becomes easy.

First, we need to make a function to find the factorial of a number. As stated in the problem, you can find the factorial of n by multiplying all the positive integers up to and including n together.

Another way of thinking about this is by saying the factorial of any number is just the factorial of the previous number multiplied by the chosen number. This leads us to a very nice example of where we could use **recursion**.

Recursion is the process where a function calls *itself* from within itself. At first glance this might seem like it will just make an infinite loop - but this is why when using recursion, we need to define one or more **base cases**, which are conditions for the recursion to stop.

Also each time we call the function within itself, it needs to be with a different input than the original function was called with (because otherwise we'd just be repeating the same thing over and over.)

Here's how we could make a recursive factorial function in python.

```
def factorial(n):

  if n <= 1:
    return 1

  else:
    return n * factorial(n-1)

```

Each time the function recurs, it recurs with the number n-1, so this acts as the loop and keeps decreasing n until it becomes 1 or less (I say or less because we need to account for if 0 is inputted).

The function itself returns n * factorial(n-1). When we get to n = 1 or less, well, 1 factorial is just 1, so we need to return 1 and break the recursion. Then the recursion will traverse back up the loop, doing all the multiplications, and reaching the final value, which is the factorial of our number.

As a small last step, we can make the function much more readable by using a **ternary operator** - which is essentially just an if else return statement mashed into one line:

```
return 1 if n <= 1 else n * factorial(n-1)
```

Now that we have a factorial function, lets do the 'curious number' part of the problem. We need a function that returns True if the input integer is a curious number.

Step one is to **cast** the input into a string, and loop through it, which looks something like this:
```
num = 145
for x in str(num):
  ...
```

Now we need to apply factorial() to each of the digits and then add them to a sum:

```
num = 145
sum = 0
for x in str(num):

  sum += factorial(int(x))
```

And now we can just check if the sum is equal to our original num:

```
if num == sum:
  return True
  
else:
  return False
```


Once again, this algorithm can be simplified and made more readable. We can utilise a **generator** which is a way of storing the results of a loop in a list, and then use the sum() function to add up all the values in said list, without even needing a sum variable. Finally we can return the result of the expression itself (no need for if num == sum) because expressions using operators like =, > or < will return booleans in python.

```
return sum(factorial(int(x)) for x in str(n)) == n
```

Now we have both the functions we need, we just need to apply them onto all the numbers from 3 until the largest curious number. (There must be a largest curious number otherwise how would you be able to add them all up?). 

However, we dont need to find the largest curious number, we can just take an educated guess and set an upper limit for curious numbers.

If we know that curious numbers have digit factorials that sum to themselves, well the largest single digit that we can have is 9. Now if we use trial and error, using larger and larger numbers, we find that the 7 digit number 9,999,999 has a sum of digit factorials of 2177280, which is less than the original number.

This tells us that no curious number can be greater than 2177280, because past here the factorial sum will always be smaller than the original number. (Adding a digit multiplies the value by 10, but only adds 9! = 362,880 to the factorial sum).

So we can set our upper limit to 2177280

Now that we have an upper limit, all thats left to do is to loop through integers from 3 to the limit, and check if they are curious or not. We can reuse the **generator** concept from before, as well as the sum function, and the code looks something like this:

```
sum(x for x in range(3, 2540160) if isCurious(x))
```

Now, we could leave it there, but if you test this code, it ends up taking almost a whole minute to run, which is terrible efficiency. So, optimisation is required.

A trick for optimisation is to find places where processes/calculations are being repeated unecessarily in the code, and to set a **cache** to store those calculations instead. That way, the values can be reused and there wont be extra processing time required.

In our case, looking at the curious number function, we only ever need to get the factorial of a single digit - that is, 0 through 9. No other factorials are ever needed. So instead of redoing the factorial each time, lets just store the values of those 10 factorials in our code.

We can do this with a **hashmap** (aka **dictionary**), and we can do it efficiently by using dictionary comprehension:

```
factorials = {i: factorial(i) for i in range(10)}
```
This code will create a dictionary with the values of 0-9, and their corresponding factorials. Yes, technically you could just hard-code the factorials into a dictionary by hand, but that's bad programming practice.

Now, we just need to adjust the curious function slightly to use the new factorials dictionary.

```
return sum(factorials[int(x)] for x in str(n)) == n
```
The change is barely noticeable - the factorial function has been replaced with factorials, the dictionary. And the normal brackets have changed to square brackets (because thats how you access items from a dictionary).

Finally, after all of this, we have a nice clean looking solution, written with a low line count, readable, and one that follows good programming practice. That was a long one huh.
