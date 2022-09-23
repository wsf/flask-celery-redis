from app import divide
task = divide.delay(1, 2)

a = 1
while a == 0:
    a = int(input('Ing valor '))

