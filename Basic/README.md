# Question 1

Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
```
Sample data : 3, 5, 7, 23  
Output :  
List : ['3', ' 5', ' 7', ' 23']  
Tuple : ('3', ' 5', ' 7', ' 23')

```

## Answer

<details><summary>Show</summary>


```python
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
```

    Enter size : 4
    Enter element : 1
    Enter element : 2
    Enter element : 3
    Enter element : 4
    The list is : [1, 2, 3, 4]
    The tuple is :(1, 2, 3, 4)

</details>

<br>

# Question 2

Write a Python program to accept a filename from the user and print the extension of that
```
Sample filename : abc.java
Output : java
```

## Answer
<details><summary>Show</summary> 

```python
import os

fileName, fileExtension = os.path.splitext("file.txt")

print(f"Extension is : \n{fileExtension}")
```

    Extension is : 
    .txt
</details>
<br>

# Question 3

Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"] 

## Answer

<details><summary>Show</summary> 

```python
color_list = ["Red","Green","White" ,"Black"]

print(color_list[0], " " ,color_list[-1])
```

    Red   Black

</details>
<br>

# Question 4

Write a Python program to display the examination schedule. 
```
(extract the date from exam_st_date) exam_st_date = (11, 12, 2014)
```

## Answer

<details><summary>Show</summary> 

```python
exam_st_date = (11, 12, 2014)
print("The examination will start from : %i/%i/%i "%exam_st_date)
```

    The examination will start from : 11/12/2014 
    
</details>
<br>

