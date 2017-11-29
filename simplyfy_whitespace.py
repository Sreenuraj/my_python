import string
import sys


def main():
    text = input("Enter the text: ")
    result = simplify(text)
    print('result:', result)


def simplify(text, whitespace=string.whitespace, delete=""):
    result = []
    word = ""
    for char in text:
        if char in delete:
            continue
        elif char in whitespace:
            if word:
                result.append(word)
                word = ""
        else:
            word += char
    if word:
        result.append(word)
    return " ".join(result)

main()
