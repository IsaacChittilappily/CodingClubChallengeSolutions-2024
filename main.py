import sys

with open('config.txt','r') as f:
  folder = f.read().strip()

folderPath = './Week' + folder

if folderPath not in sys.path:
  sys.path.append(folderPath)

print(f'Running code for week {folder}...\n--------------------------\n')

getattr(__import__('solution'+folder), 'main')()
