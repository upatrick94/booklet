def count_words(text: str):
    words = text.split()
    return len(words)

def count_characters(text: str):
    counter = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
    return counter


def sorted_count_characters(text: str):
    counter = count_characters(text)


