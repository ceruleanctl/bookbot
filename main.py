from stats import get_chars_dict, get_chars_list, get_word_count
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)
    total_words = get_word_count(text)
    chars_dict = get_chars_dict(text)
    sorted_chars_list = get_chars_list(chars_dict)
    print_book_report(book_path, total_words, sorted_chars_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_book_report(book_path, total_words, sorted_chars_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f'Found {total_words} total words')
    print("--------- Character Count -------")
    for item in sorted_chars_list:
        if not item["char"].isalpha():
            continue
        print(f"{item["char"]}: {item["num"]}")

main()
