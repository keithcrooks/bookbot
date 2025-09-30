import sys
from stats import get_character_frequency, get_characters_sorted_by_frequency, get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    args = sys.argv

    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = args[1]
    book_contents = get_book_text(filepath)
    book_word_count = get_num_words(book_contents)
    book_char_frequency = get_character_frequency(book_contents)
    book_char_frequency_sorted = get_characters_sorted_by_frequency(book_char_frequency)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")

    for char in book_char_frequency_sorted:
        if not char["char"].isalpha():
            continue

        print(f"{char["char"]}: {char["count"]}")

    print("============= END ===============")

main()
