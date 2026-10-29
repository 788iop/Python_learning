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