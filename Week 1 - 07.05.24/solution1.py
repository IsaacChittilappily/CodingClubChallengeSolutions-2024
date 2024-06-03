alpha = 'abcdefghijklmnopqrstuvwxyz'
string = 'abfergegcdefsrhghijkaehhhrlmnopqshtrshtrhsrttuvwxyzehhrthrt'
found = True

for letter in alpha:
  if letter not in string:
    found = False
    
print(found)
