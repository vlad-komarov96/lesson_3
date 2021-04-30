#Задание 1

def div(*args):

    try:
        arg1 = int(input("Введите первый аргумент: "))
        arg2 = int(input("Введите второй аргумент: "))
        res = arg1 / arg2
    except ValueError:
        return 'Ошибка!'
    except ZeroDivisionError:
        return 'Ошибка! На 0 делить нельзя.'

    return res

print(f'result  {div()}')


#Задание 2

def my_func (name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(my_func(surname = 'Komarov', name = 'Vladislav', year = '1996', city = 'Moscow', email = 'vlad-komarov@mail.ru', telephone = '8-900-300-30-30'))


#Задание 3

def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Result - {my_func(int(input("Введите первый аругмент: ")), int(input("Введите первый аругмент: ")), int(input("Введите первый аругмент: ")))}')


#Задание 4

def power(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res
 
 
print(power(float(input("Первое значение - ")), int(input("Второе значение - "))))

#Задание 5

def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите строку чисел через пробел: ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Текущая сумма составляет: {sum_res}')
    print(f'Финальная сумма составляет: {sum_res}')


my_sum()

#Задание 6

def int_func (*args):
    word = input("Введите слово: ")
    print(word.title())
    return
int_func()
