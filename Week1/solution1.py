def allAlpha(string):
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  found = True
  
  for letter in alpha:
    if letter not in string:
      found = False
      
  return found

def main():
  print(allAlpha(input()))

if __name__ == '__main__':
  main()
  