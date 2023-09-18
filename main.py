import random, os, time
list1 = []

while len(list1) <= 8:
  a = random.randint(0, 90)
  list1.append(a)
  list1.sort()
print()

def list(t):
  list2 = []
  list3 = [] 
  
  for c in t:
    if len(list2) <= 2:
      list2.append(c)
    else:
      list3.append(list2)
      list2 = []
      list2.append(c)
  list3.append(list2)
  list3[1][1] = 'BINGO'
  return list3


def printer(d):
  r = '   _________________________'
  print("\033[1;33m   David's Nan's Bingo Card Generator.")
  print()
  print()
  for i in d:
    for j in i:
      if i.index(j) == 2:
        print(f'\033[1;33m{j:^10}', end='')
      else:
        print(f'\033[1;33m{j:^10}', end='|')
      
    print()
    if d.index(i) != 2:
      print(f'{r}')
    print()

y = 0
k = 0
while True:
  if y <= 0:
    b = list(list1)
    printer(b)
  ask = int(input('    What number comes next: '))
  if ask in list1:
    h = list1.index(ask)
    list1[h] = 'X'
    k += 1
  else:
    print()
    print('\033[31mNumber not in there!')
    print()
  time.sleep(1)
  os.system('clear')
  b = list(list1)
  printer(b)
  y += 1
  if k == 8:
    print()
    print('\033[0mYou have won this game!')
    break