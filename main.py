import sys

with open('config.txt','r') as f:
  # replace the number in config.txt with the problem number you want to run
  folder = f.read().strip()

folderPath = './week' + folder

if folderPath not in sys.path:
  sys.path.append(folderPath)

print(f'Running code for week {folder}...\n--------------------------\n')

try:
  getattr(__import__('solution'+folder), 'main')()

except ModuleNotFoundError:
  print("The solution for that week hasn't been released yet")
