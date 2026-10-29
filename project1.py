def double_list(numbers):
    result = []
    for i in numbers:
        result.append(i*2)
    return result
print(double_list([4,5,3,3]))




def word_length(text):
    new_list = text.split()
    result = []
    for words in new_list:
        result.append(len(words))
    return result
print(word_length("Hello world"))



def positive_numbers(*numbers):
    result = [x for x in numbers if x > 0]
    return result
print(positive_numbers(3,5,3,2,5,0,-1,-99))


def count_fruits(fruits):
    result = {}
    for fruit in fruits:
        if fruit not in result:
            result[fruit] = 1
        else:
            result[fruit] += 1
    return result
print(count_fruits(["Яблоко","Яблоко","Банан"]))




def total_price(products):
    result = sum([x["price"] for x in products])
    return result
products = [
    {"name": "Хлеб", "price": 50},
    {"name": "Сыр", "price": 300},
    {"name": "Молоко", "price": 80}
]
print(total_price(products))



def has_pair(numbers,pair):
    for i in range(len(numbers)-1):
        if numbers[i] + numbers[i+1] == pair:
            return "YES"
    return "NO"
print(has_pair([1,2,3,4],5))