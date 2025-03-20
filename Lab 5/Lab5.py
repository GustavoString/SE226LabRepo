

import random
import string
passwords = []
for _ in range(5):
    password = ''.join(random.choices(string.ascii_lowercase, k=15))
    passwords.append(password)


letters = dict()

print("Choose 10 characters (lowercase only) and assign 5 replacement options each:\n")

for _ in range(5):
    letter = input("Enter a lowercase letter: ")
    if len(letter) != 1 or letter not in string.ascii_lowercase:
        print("Please enter a single lowercase letter")
        continue

    replacements = set()
    for _ in range(3):
        replacement = input("Enter a replacement letter for '" + letter + "': ")
        replacements.add(replacement)

    letters[letter] = replacements

modifiedPasswords = []
for password in passwords:

    print(password)

    replacedCount = 0
    modified = password
    for letter in letters:
        while letter in modified:
            replacement = random.choice(list(letters[letter]))
            modified = modified.replace(letter, replacement, 1)
            replacedCount += 1

    modifiedPasswords.append((modified, replacedCount))

categorizedPasswords = {"strong": [], "weak": []}
for modifiedPassword, count in modifiedPasswords:
    if count > 4:
        categorizedPasswords["strong"].append(modifiedPassword)
    else:
        categorizedPasswords["weak"].append(modifiedPassword)

print("\nGenerated Passwords:\n")

print("STRONG PASSWORDS:")
for sp in categorizedPasswords["strong"]:
    print(sp)

print("\nWEAK PASSWORDS:")
for wp in categorizedPasswords["weak"]:
    print(wp)