from stats import count_words,count_characters

def get_book_test(filePath: str):
    with open(filePath) as f:
        fileContents = f.read()
    return fileContents

def main():
    book_text = get_book_test("books/frankenstein.txt")
    num_words = count_words(book_text)
    num_characters = count_characters(book_text)
    print(f"Found {num_words} total words")
    print(num_characters)

main()