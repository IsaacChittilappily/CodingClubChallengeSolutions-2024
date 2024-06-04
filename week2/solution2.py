from typing import Counter

def isAnagram(str1: str, str2: str) -> bool:
  return Counter(str1) == Counter(str2)


def main():
  
  print(isAnagram(*input('Input two strings separated by a space:\n').split(' ')))


if __name__ == '__main__':
  main()
  