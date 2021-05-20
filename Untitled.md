Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:


```python
word = input()
letter, digit = 0, 0

for i in word:
    if ("a" <= i and i <= "z") or ("A" <= i and i <= "Z"):
        letter += 1
    if "0" <= i and i <= "9":
        digit += 1

print("LETTERS {0}\nDIGITS {1}".format(letter, digit))
```

    hello
    LETTERS 5
    DIGITS 0
    


```python

```
