def main():
    text = input("Enter the text to check: ")
    result = check_brackets(text)
    print('result:', result)


def check_brackets(text, brackets="{}[]()<>"):
    """
    >>> check_brackets('skdjd[sdjhsjdh[sjdhsjdh')
    False
    >>> check_brackets('[sdsd]{sdsd}')
    True
    """
    counts = {}
    left_for_right = {}
    for left, right in zip(brackets[::2], brackets[1::2]):
        assert left != right, "the bracket characters must differ"
        counts[left] = 0
        left_for_right[right] = left
    for c in text:
        if c in counts:
            counts[c] += 1
        elif c in left_for_right:
            value = left_for_right[c]
            if counts[value] == 0:
                return False
            counts[value] -= 1
    return not any(counts.values())


if __name__ == '__main__':
    import doctest
    doctest.testmod()

