from stats import count_words,count_characters,sorted_count_characters
import sys

def get_book_test(filePath: str):
    with open(filePath) as f:
        fileContents = f.read()
    return fileContents

def main():
    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_test(sys.argv[1])
    num_words = count_words(book_text)
    num_characters = sorted_count_characters(book_text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character in num_characters:
        print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")

main()