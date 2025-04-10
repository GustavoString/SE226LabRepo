from string_package import reverse_string, capitalize_words, remove_punctuation, count_characters, count_words, average_word_length

s = input("Write a sentence: ")

print("Reversed:", reverse_string(s))
print("Capitalized:", capitalize_words(s))
print("Removed punctuation:", remove_punctuation(s))
print("Word count:", count_words(s))
print("Average word length:", average_word_length(s))
