square=float(input("Введите длину стороны квадрата: "))
s=(square ** 2)
print("Площадь:", (s))
p=(square*4)
print("Периметр:", p)

a=float(input("Введите длину стороны прямоугольника: "))
b=float(input("Введите ширину стороны прямоугольника: "))
s2=(a * b)
print("Площадь:",s2)
p2=(2*(a+b))
print("Периметр:", p2)


str_user = input("Введите символ: ")#
d = int(p+s2)
print(str_user * d)
str_user = input()


pay = int(input("Введите заработную плату в месяц: "))
percent = int(input("Введите, какой процент(%) уходит на ипотеку: "))
c = int(input("Введите, какой процент(%) уходит на жизнь: "))


mortgage = pay * percent / 100 * 12
accomulation = pay * (1 - (c / 100) - (percent / 100)) * 12 
print("Вывод")
print("На ипотеку было потрачено", mortgage)
print("Было накоплено", accomulation)