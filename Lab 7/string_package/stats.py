def count_characters(s):
    count = 0
    for char in s:
        count += 1
    return count

def count_words(s):
    x = s.split(" ")
    count = 0
    for word in x:
        count += 1
    return count

def average_word_length(s):
    x = s.split(" ")
    sum = 0
    for word in x:
        sum += len(word)
    return sum/len(x)
