# Week 3 - Minimum Currency:
## Solution:

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
And thats the completed code! I did see some methods that used repeated subtraction to achieve the same result, however this would be much less efficient than just dividing once numbers get larger.