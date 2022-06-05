#Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
#Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

numbers = [1, 2, 3, 5, 1, 5, 3, 10]

def uniNumbers(numbers):
    uniList = []

    for number in numbers:
        if number in uniList:
            continue
        else:
            uniList.append(number)
    return uniList

print(uniNumbers(numbers))
