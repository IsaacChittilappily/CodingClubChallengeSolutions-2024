import sys

with open('config.txt','r') as f:
  # replace the number in config.txt with the week number
  folder = f.read().strip()

folderPath = './Week' + folder

if folderPath not in sys.path:
  sys.path.append(folderPath)

print(f'Running code for week {folder}...\n--------------------------\n')

getattr(__import__('solution'+folder), 'main')()
