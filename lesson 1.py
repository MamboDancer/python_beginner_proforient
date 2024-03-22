number = input("Введіть число для пошуку: ")
for i in range(0, 50, 2):
    print("Я на кроці під номером ", i)
    if i == int(number):
        print("Я знайшов ваше число!")