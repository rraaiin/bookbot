def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

print(main())


def word_count():
    words = main().split()
    count = 0
    for i in words:
        count += 1
    return count

print("words:", word_count())


def char_count():
    character_count = {}

    lower_words = main().lower()
    lower_chars = list(lower_words)

    for char in lower_chars:
        if char in character_count:
            character_count[char] += 1
            else:
            character_count[char] = 1
    
    return character_count

print(char_count())





