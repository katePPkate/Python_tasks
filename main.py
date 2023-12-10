'''Напишите простой калькулятор, который считывает с пользовательского
ввода три строки: первое число, второе число и операцию, после чего
применяет операцию к введённым числам ("первое число" "операция" "второе
число") и выводит результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить
строку "Деление на 0!".'''

x1 = float(input())
x2 = float(input())
operation = str(input())
if operation == '+':
  print (x1+x2)
if operation == '-':
  print (x1-x2)
if operation == '*':
  print (x1*x2)
if operation == 'pow':
  print (x1**x2)
if (operation == 'mod' and x2 != 0):
  print (x1%x2)
if (operation == '/' and x2 != 0):
  print (x1/x2)
if (operation == 'div' and x2 != 0):
  print (x1//x2)
if ((operation == 'mod' or operation == 'div' or operation == '/') and x2 == 0):
  print ('Деление на 0!')