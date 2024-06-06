Matriz = [
  [12, 5, 18, 22 ,7],
  [8, 19, 15, 2 ,11],
  [4, 13, 30, 1, 27],
  [20, 3, 9, 6, 16],
  [21, 14, 25, 28, 17]
]


soma_total = 0
for i in (Matriz):
  for j in i:
    soma_total +=j 

print(soma_total)