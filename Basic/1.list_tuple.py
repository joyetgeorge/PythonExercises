"""  Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23') """

def convert(list):
    return tuple(list)

list = []
len =int(input("Enter size : ")) 
for i in range(0 , len) :
    element = int(input("Enter element : "))
    list.append(element)
print("The list is : ", end="")
print(list)
print("The tuple is :", end="")
print(convert(list))