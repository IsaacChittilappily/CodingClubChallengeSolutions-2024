from typing import Counter

def isAnagram(str1, str2):
  return Counter(str1) == Counter(str2)


def main():
  print(isAnagram(*input().split(' ')))


if __name__ == '__main__':
  main()
  