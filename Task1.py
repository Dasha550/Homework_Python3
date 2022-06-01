#Найти НОК двух чисел

num1 = 10
num2 = 11
NOK = 1
while True:
    if NOK%num1==0 and NOK%num2==0:
        print(NOK)
        break
    else:
        NOK=NOK+1
