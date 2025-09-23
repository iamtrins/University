import random
n = random.randint(1,100)
count = 0
while True:
  m = input()
  if m.lower().strip() == ('выход'):
    print('Вы вышли из игры')
    break
  if not m.isdigit():
    print('Введите число или «Выход» для звершения игры')
    break
  m = int(m)
  count += 1
  if n > m:
    print('Ваше число меньше!')
  elif n < m:
    print('Ваше число больше!')
  else:
    if count % 10 == 1:
      print(f"Поздравляем, вы угадали число за {count} попытку")
    elif count % 10 == 2 or count % 10 == 3 or count % 10 == 4:
      print(f"Поздравляем, вы угадали число за {count} попытки")
    else:
      print(f"Поздравляем, вы угадали число за {count} попыток")
    break
