def shift_right(numbers):
    result = []
    result.append(numbers[-1])
    result.append(numbers[:-2])
    return result
print(shift_right([1,2,3,4,5]))




def unique_items(numbers):
    total = []
    for I in range(len(numbers)):
        if numbers[I] not in total:
            yield numbers[I]
            total.append(numbers[I])
for num in unique_items([1,2,2,2,3,4,4,5,6]):
    print(num)




import functools
def hello(func):
    def wrapper():
        print(f'Привет! Начинаю работу!')
        func()
        print(f'Готово')
    return wrapper
@hello
def test():
    print(f'Пишу Hello world!')
test()



import functools
def repeat_three_times(func):
    def wrapper(*args,**kwargs):
        for I in range(3):
           func(*args,**kwargs)
    return wrapper
@repeat_three_times
def say_hi(name):
    print(f'Привет, {name}!')
say_hi("Иван")



import functools
def check_age(func):
    def wrapper(age):
        if age < 18:
            print(f'Доступ запрещен')
            return
        else:
            return func(age)
    return wrapper
@check_age
def buy_alhocol(age_1):
    print(f'Покупка прошла успешно!')
buy_alhocol(18)
