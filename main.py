import sys

from stats import get_numb_words
from stats import get_numb_chars
from stats import get_sorted_characters

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def print_report(path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    print("----------- Word Count ----------")
    print(f"Found {get_numb_words(path)} total words")

    print("--------- Character Count -------")
    sorted_characters = get_sorted_characters(path)

    for item in sorted_characters:
        char = item["char"]
        if char.isalpha():
            print(f"{char}: {item['num']}")
    print("============= END ===============")

def main():
    print_report(book_path)

main()