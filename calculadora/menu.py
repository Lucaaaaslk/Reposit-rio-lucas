import function

def menuPrincipal():
  print("bem vindo a calculadora básica")
  print("qual operação você deseja fazer?")
  print("1. somar")
  print("2. subtrair")
  print("3. multiplicar")
  print("4. dividir")
  resposta = input("qual opção")
  if resposta == "1":
    menuSomar()
  elif resposta == "2":
    menuSubtrair()
  elif respota == "3":
    menuMultiplicar()
  elif resposta == "4":
    menudividir()

def menuSomar():
  print("Bem vindo a soma")
  n1 = int(input("digite o primeiro número"))
  n2 = int(input("digite o segundo número"))
  resultado = function.somar(n1, n2)
  print(f"A soma dos valores é {resultado}")

def menuSubtrair():
  print("Bem vindo a subtração")
  n1 = int(input("digite o primeiro número"))
  n2 = int(input("digite o segundo número"))
  resultado = function.subtrair(n1, n2)
  print(f"A subtração dos valores é {resultado}")

def menuMultiplicar():
  print("Bem vindo a multiplicação")
  n1 = int(input("digite o primeiro número"))
  n2 = int(input("digite o segundo número"))
  resultado = function.multiplicar(n1, n2)

def menuDividir():
  print("Bem vindo a divisão")
  n1 = int(input("digite o primeiro número"))
  n2 = int(input("digite o segundo número"))
  resultado = function.dividir(n1, n2)
  print(f"A divisão dos valores é {resultado}")
    