import random

counter = 0

def is_valid(n):
    if n.isdigit():
        n = int(n)
        if 1 <= n <= righthand_boundary_number:
            return True
        else:
            return False
    else:
        return False


def boundary_number():
    print('Введите правую границу для случайного выбора числа')
    while True:
        global righthand_boundary_number
        righthand_boundary_number = input()
        if righthand_boundary_number.isdigit():
            if int(righthand_boundary_number) > 1: 
                righthand_boundary_number = int(righthand_boundary_number)
                global number
                number = random.randint(1, righthand_boundary_number)
                break
            else:
                print('Введите положительное число от 2 до бесконечности включительно')
        else:
            print('Это неположительное число!')

boundary_number()

print('Добро пожаловать в числовую угадайку')
while True:
    print('Введите число:')
    num = input()
    if is_valid(num):
        counter += 1
        num = int(num)
        if num < number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif num > number:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif num == number:
            print('Вы угадали, поздравляем!')
            print('Вы сделали', counter, 'попыток')
            print('Спасибо, что играли в числовую угадайку. Хотите ли сыграть ещё раз? Напишите "да" или "нет"')
            yes_or_no = input()
            while not(yes_or_no == 'нет' or yes_or_no == 'да'):
                print('Напишите "да" или "нет"')
                yes_or_no = input()
            else:
                if yes_or_no == 'нет':
                    break
                elif yes_or_no == 'да':
                    counter = 0
                    boundary_number()
    else:
        print('А может быть все-таки введем целое число от 1 до ' + str(righthand_boundary_number) + '?')