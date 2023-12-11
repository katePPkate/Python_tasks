'''Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по
спирали, выходящей из левого верхнего угла и закрученной по часовой
стрелке'''

n = int(input())
b =1
c = [[0 for j in range(n)] for i in range(n)]
for g in range (n//2 + n%2):
  min = g
  max = n - g - 1
  i, j = min, min
  for a in range(1, (max-min)*4+1):
    c[i][j] = b
    b+=1
    if i == min and j !=max:
      j += 1
    elif j == max and i != max:
      i += 1
    elif i == max and j != min:
      j -=1
    elif j == min and i != min:
      i -= 1
if n % 2 == 1:
  c[n//2][n//2]=n**2

for i in range (n):
  print (*c[i], sep=' ')