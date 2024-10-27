# #Задание 1
# text = 'Hello, World!'
# print(len(text))
# lon = text[::-1]
# print(lon)
# n = text.replace('l', 't')
# print(n)

# #Задание 2
# zapros_imy = input('Здраствуйте какое у вас имя?')
# zapros_let = int(input('Здраствуйте какой у вас возраст?'))
# print('Ваше имя:', zapros_imy, 'ваш возраст:',  zapros_let)

# #Задание 3
# slovo = 'Программирование'
# print(slovo[3:8])

# #Задание 4
# def lilili(a, b, c):
#     return(a + b + c)
# result = lilili(1, 2, 3)
# print(result)

# #Задание 5
# for i in range(2, 21, 2):
#     print(i)
# #Задание 6
from random import randint
def ugat():
    uu = randint(1, 100)
    pop = 0


    while True:
        popit = int(input('Введите число от 1 до 100'))
        pop += 1

        if popit < uu:
            print('Загаданное число больше вашего')
        elif popit > uu:
            print('Загаданное число меньше вашего')
        else:
            print(f'Поздравляем ты угадал число' , uu, 'pop')