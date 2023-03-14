print("Введите трехзначное число ")
numbers = int(input())
sum = 0
secondnumber = numbers // 10
if numbers > 100 and numbers < 1000:
    sum = numbers % 10 + numbers // 100 + secondnumber % 10
    print(sum)
else:
    print("Введено не трехзначное число ")

