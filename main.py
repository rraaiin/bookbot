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
    
    for i in range(0, len(lower_chars)):
        character_count[lower_chars[i]] = i

    print(character_count)
char_count()
