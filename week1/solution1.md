# Week 1 - Alphabet Check - 07/05/24:
## Solution:

The most efficient way to solve this would be just using loops - loop through the whole alphabet and check if the letter is in the string for each one.

We can achieve this by defining the alphabet as a string first, then defining a **boolean** to be the value we return at the end of the process.

A good trick to use for when you're checking if all the items of some iterable match some condition is to set your boolean to True to begin with, and then check for the opposite of the condition, by using the ```not``` keyword, hence you set the boolean to False if the condition is ever not met:

```  
if letter not in string: 
  found = False
```

Thats pretty much it, the full solution is barely 7 lines.

However there is a 'joke' method that we could use here that would allow for a 1 line solution. 
This solution is not efficient and would definitely not be used in a practical setting, but its still interesting nonetheless, and its achieved by using a **set**. 

A set is a type of data structure in python, similar to lists, but with some key differences, and one of them is that they cannot contain duplicate entries. This means that if we turn the input string into a set, we can simply check if that set is of length 26 (because there are 26 letters in the alphabet), and if its not, then we know that the list cannot contain all of the alphabet. The line looks like this:
```
print(len(set(input())) == 26)
```

This may seem crazily efficient because of the low line count, but in reality, converting to a set in python is much more computationally intensive than the simple loop we were using before, so it would take longer than our original solution. Still kinda cool tho right?