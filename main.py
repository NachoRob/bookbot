from stats import get_num_words, counting_characters, sort_dict, sort_on
import sys

def get_book_text(filepath):
    """
    Reads the content of a book file and returns it as a string.
    """
    with open(filepath) as f:
        return f.read()

def main(filepath):
    """ 
    Main function to print the content of a book file.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    
    print("============ BOOKBOT ============") 
    print(f"Analyzing book found at {book_path}...")   
    
    
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    num_char = counting_characters(book_text)
    new_list = sort_dict(num_char)
    print("----------- Word Count ----------")
    print(num_words)
    print("--------- Character Count -------")
    for key in new_list:
        if key["char"].isalpha():
            print(f"{key["char"]}: {key["num"]}")
    print("============= END ===============")


main("")