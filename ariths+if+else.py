
x = float(input("a: "))
y = float(input("b: "))
op = input("operation: ")

def add(x, y):
  return x + y

def diff(x, y):
  return x - y

def prod(x, y):
  return x * y

def quo(x, y):
  return x/y

if op == '+':
  print(add(x, y))
elif op == '-':
  print(diff(x, y))
elif op == '*':
  print(prod(x, y))
elif op == '/':
  print(quo(x, y))
