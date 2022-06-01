#Составить список простых множителей натурального числа N
from re import I

List = [1]
num = 28
for i in range (2, num+1):
    if num!=1:
        while num%i==0:
            num= num/i
            List.append(i)
    elif num>1:
        List.append(num)
        break

print(List)