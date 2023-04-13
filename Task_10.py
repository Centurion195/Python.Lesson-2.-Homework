# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
from random import random, randint

n = randint(5,20)
up = int(random()*n)
down = n - up

print(f"Всего монет: {n}")
print(f"Монеты вверх решкой: {up}")
print(f"Монеты вверх гербом: {down}")

if up > down:
    print(f"Следует перевернуть монеты, лежащие гербом вверх, в количестве {down} штук")
else:
    print(f"Следует перевернуть монеты, лежащие решкой вверх, в количестве {up} штук")