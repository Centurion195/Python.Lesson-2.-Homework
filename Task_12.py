# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя
# делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать
# задуманные Петей числа.

b = -int(input("Сумма чисел: "))
c = int(input("Произведение чисел: "))

d = b * b - 4 * c
x1 = round(float((-b + d ** (1 / 2)) / 2), 2)
x2 = round(float((-b - d ** (1 / 2)) / 2), 2)

print(f"Корень х1: {x1}")
print(f"Корень х2: {x2}")
