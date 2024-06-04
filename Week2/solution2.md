# Week 2 - Anagram Check - 14/04/24:
## Solution:

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