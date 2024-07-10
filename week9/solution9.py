def romanToInt(roman: str) -> int:
  symbols = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
  }

  ans = 0

  for i in range(len(roman)):
      if i < len(roman) - 1 and symbols[roman[i]] < symbols[roman[i+1]]:
          ans -= symbols[roman[i]]
      else:
          ans += symbols[roman[i]]

  return ans