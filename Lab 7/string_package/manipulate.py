import string


def reverse_string(s):
    ret = ""
    for char in reversed(s):
        ret += char
    return ret

def capitalize_words(s):
    x = s.split(" ")
    ret = ""
    for word in x:
        ret += word.capitalize()
        ret += " "
    return ret

def remove_punctuation(s):
    for char in string.punctuation:
        if char in s:
            s = s.replace(char, "")
    return s