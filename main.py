# python
import sys
from stats import get_number_of_words, num_characters, sorted_list_of_dictionaries


def get_book_text(filepath):
    """Reads the content of a book from a text file."""
    with open(filepath) as file:
        return file.read()   
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...\n----------- Word Count ------------")

    print(f"Found {get_number_of_words(get_book_text(book_path))} total words")

    print("--------- Character Count ------------")

    char_counts = num_characters(get_book_text(book_path))
    sorted_char_counts = sorted_list_of_dictionaries(
        [{'character': char, 'count': count} for char, count in char_counts.items()],
        key='count'
    )   

    print("Character counts (sorted):")
    for char_count in sorted_char_counts:
        print(f"  {char_count['character']}: {char_count['count']}")

    print("============= END ===============")

main()

