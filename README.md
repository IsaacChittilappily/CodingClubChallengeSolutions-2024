# Coding Club Challenges

This replit will contain the solution(s) to each weeks challenge(s) and I will update it at the end of each Tuesday session, so that students who tried and failed at a solution can take a look at where they went wrong. Each solution will have its own python file, labelled with the date the challenge was set so you can find previous solutions easily.

### NOTE - If you want to run some of the solutions yourself and dont want to copy and paste, fork this repl and then click on the 3 dots next to the add file button and select 'Show hidden files', then in the .replit file replace the name of the file in the first line with the name of the file that you want to run

Bear in mind that I am not a coding grandmaster by any means so if you find any inefficiencies or straight errors in my code, feel free to tell me at the next session.

In this markdown I will record my thought process for solving each problem, and anything else notable about it.


---


# 07.05.24 - Alphabet Check:

### Problem:
Given a string containing only lowercase english letters (no spaces, punctuation etc), return True if the string contains at least one occurence of every letter in the alphabet, and False otherwise.

Source - Saw it on a youtube short

### Solution:

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

# 14.05.24 - Anagram Check:

### Problem:
Given two strings of any length and with any characters, check if they are anagrams of each other.

Source - Leetcode

### Solution:

This is a rather interesting problem which can be approached in many ways - the real trick is finding the most efficient method.

The first and most obvious method to solving this might be to first check if the strings are the same length, and then loop through both strings and for each character, check if that character is in the other string. Multiple people wrote code that went something like this:

```
for letter in str1:
  if letter not in str2:
    found = False

for letter in str1:
  if letter not in str2:
    found = False
```

This does work (provided you also do a length check) but we can clearly see repeated code, and of course, that breaks one of our coding principles - DRY (Dont Repeat Yourself). Not only that, but the time complexity of this is absurdly higher than it needs to be. 

So how do we fix it?

Well, instead of looping through each letter individually, we need to find a way of 'converting' both of the strings in a way that if they contain the exact same letters, then in their converted form, they will be the same. Since they are anagrams, we essentially need a way of ignoring the order of the letters.

Some people might jump to converting both strings to sets, because sets are unordered, however this would not actually work, because sets will also remove all duplicates from the string - this would result in 'hello' being seen as an anagram of 'helloo'. You'd be checking if the unique letters are anagrams of each other, not the original strings.

Instead, we need a something that keeps the letter count the same, but just puts them into the same order - this could simply be done by sorting both strings, which a couple of students realised:

```
print(sorted(str1) == sorted(str2))
```

Many people might stop there, and be happy with this one liner, however we can take it a step further and make it more efficient. Sorting of any kind will have a minimum time complexity of nLogn, and we can beat this by using a **hashmap**.

A hashmap (also known as a dictionary in python) is another data structure, that utilises key-value pairs, rather than just being an indexed list. Each 'key' in a hashmap will have a corressponding 'value'.

In this case, we can use the Counter function (imported from the typing module) to convert our strings into hashmaps - it will make a dictionary with the letters being keys, and the number of occurences of the letter being values.

Of course, you can also just program the Counter function into your code to avoid having to import it, but seeing as it is a widely standardised python function already, there isn't much point - use available modules where you can, your life will become a lot easier.

So, using Counter on 'Hello' would return:

```
{
'H':1,
'e':1',
'l':2,
'o':1
}
```

This would be the same if you converted 'elloH', hence we have the function to convert both strings into the same format, now we can simply compare them and print the result.

The conversion has a time complexity of N, so we have significantly reduced the complexity of our solution just by using a hashmap rather than a sort. Useful right?

# 21.05.24 - Minimum Currency:

### Problem:

Given an input decimal, representing a sum of money in pounds and pence (e.g. 2.50), return the fewest number of British currency coins and/or notes that could be used to make that sum.
(PS: £50 notes do exist)

Source - Variation of Q31 from Project Euler

### Solution:

This was perhaps one of the more confusing problems, but after breaking it down step by step it becomes simple.

The first minor thing to address is the input - the input is given in pounds and pence, but for simplification we should convert it into only pennies. The best way to achieve this is by **parsing** each section of the input, rather than multiplying the input by 100.

Multiplying by 100 was the first thought of many solutions, however this leads to **floating point errors**, which is a little quirk in programming which means that any time a float is multiplied, it can result in some answers that are off by tiny fractions of the true value, due to the way computers store numbers in binary.

(To test this, if you used a x100 method, try inputting £5.10 into your code - you might see it output 4, when the output should be 2. This is caused by a floating point error when multiplying by 100.)

So, lets parse the input, using a line like this:
```
cash = int(cash.split('.')[0]) * 100 + int(cash.split('.')[1])
```
It looks confusing, I know, but all we're doing here is splitting the input into 2 parts - numbers before the dot and after the dot. This is stored in a list. Then we're multiplying the amound before the dot (i.e the pounds) by 100 (making sure to cast it to an integer) and then adding the part after the dot, to get the total cash in pennies. 

Then we're just overwriting the original variable with that number. (If you're still confused I can explain in person.)

Anyway, now we have our cash in a simple integer format.

The next step is to create an array with the values of all the notes and coins in British currency. I saw some people trying to give a named variable to each note and coin, but if you're ever in situations like this, where you need to store a list with pre-determined values, just always default to using an array.
```
coins = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
```

The final variable we will define will just be a simple counter variable, to count the running total of coins that we need.

Now for the proper logic - a lot of students got confused here, especially on where to start. When you encounter problems like these, its helpful to work through an example in your head, or on paper, to help with your thought process. You can even draw a flowchart to help.

The process goes something like this:

Input = 560\
Whats the highest value currency that goes into this? £5 (500)\
560 divided by 500 is 1 remainder 60\
New input = 60\
Whats the highest value currency that goes into this? 50p\
60 divided by 50 is 1 remainder 10\
New input is 10
Whats the highest value currency that goes into this? 10p\
10 divided by 10 is 1 remainder 0\
1+1+1 = 3\
Hence, it takes 3 currency items to represent 560

Now, once you figure out this chain of calculation, you simply need to translate it into code.

Since we're starting with the largest coin and going down, we need to make sure the list of coins is in descending order (which it is). Then we need to start looping through it using a for loop.
```
for coin in coins:
```
We first need to check wether the coin is smaller than the sum in the first place, which we can do through a simple comparison operator
```
if cash >= coin:
```
Remember that even if its the same, we still need to count it, so use >=.\

Next, once we know that the coin is smaller than the cash, we need to divide it and take the remainder, and we can do this by using the DIV and MOD operators, which in Python are represented as // and % respectively.
```
count = count + cash // coin
cash = cash % coin
```
We add the 'rounded down' result of cash/coin (think of // as dividing and rounding down to the nearest integer) to the count variable, and then we overwrite the cash variable to be the remainder after the division, just like we did in our thought process..

To make this code slightly more **pythonic**, we should use a contraction like this:
```
count += cash // coin
cash %= coin
```

Finally, since we have made this as a function with a parameter being the input, we need to return the value of count once the code has finished the for loop. 
```
return count
```
And thats the completed code! I did see some methods that used repeated subtraction to achieve the same result, however this would be much less efficient than just dividing if numbers get larger.