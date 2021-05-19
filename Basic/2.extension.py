""" Write a Python program to accept a filename from the user and print the extension of that.
Sample filename : abc.java
Output : java """

import os

fileName, fileExtension = os.path.splitext("file.txt")

print(f"Extension is : \n{fileExtension}")

