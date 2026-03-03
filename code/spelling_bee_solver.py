#Speling Bee NYT Game
def uses_only(word, letters):
    """Returns True if all the letters in the word are in the list of letters."""
    for letter in word:
        if letter not in letters:
            return False
    return True 

# print(uses_only('cake', 'kcboela'))
# print(uses_only('babson', 'kcboela'))

def must_use(word, letter):
    """Does word use the required letter?"""
    for char in word:
        if char == letter:
            return True
    return False

# print(must_use('cake', 'a'))
# print(must_use('python', 'a'))

def if_valid(word, letters, required):
    """Is word valid?"""
    # Spelling Bee rules: 4+ letters, uses only allowed letters, must include required letter
    return uses_only(word, letters) and must_use(word, required) and len(word) >= 4

def find_words(letters, required):
    """Print all valid words."""
    with open("data/words.txt") as word_file:
        for word in word_file:
            word = word.strip().lower()

            # optional: skip blank lines / weird words (apostrophes, hyphens, etc.)
            if word == "":
                continue
            if not word.isalpha():
                continue

            if if_valid(word, letters, required):
                print(word)

def main():
    letters = "kcboela"   # your 7 letters
    required = "a"        # center letter (must be used)

    print(uses_only('cake', letters))
    print(uses_only('babson', letters))
    print(must_use('cake', required))

    print(if_valid('cake', letters, required))
    print(if_valid('babson', letters, required))

    find_words(letters, required)

if __name__ == '__main__':
    main()