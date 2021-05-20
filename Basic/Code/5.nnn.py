""" Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615 """

number = str(input("Enter a Number : "))
size = int(input("Enter range : "))
listOfNumbers = []

newNumber = ""

for i in range(1, size):
    print("size : ",size)
    for j in range(1, i):
        print("i is : ",i)
        number = number+f"{number}"
        print(number)
    listOfNumbers.append(number)
print(listOfNumbers)

