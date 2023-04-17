# Задача 2: Найдите сумму цифр трехзначного числа.

a = int(input("Введите число "))
sum = 0
while a > 0:
    x = a % 10
    sum = sum + x
    a = a // 10
print(sum)

# a = str(input("Введите трехзначное число "))
# # sum = ((b = a[0]) + (c = a[1]) + (d = a[2]))
# b = int(a[0])
# c = int(a[1])
# d = int(a[2])
# sum = b + c + d
# print(sum)

# a = str(input("Введите число "))
# sum = 0
# for i in a:
#     sum = sum + int(i)
# print(sum)

# a = str(input("Введите число "))
# sum = 0
# for i in range(3):
#     sum = 0
#     for j in range(3):
#         sum = sum + int(i)
# print(sum)