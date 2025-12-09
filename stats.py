def get_num_words(text: str) -> str:
    """
    Counts the number of words in a string.
    """
    num_words = 0
    for word in text.split():
        num_words += 1
    return f"Found {num_words} total words"

def counting_characters(text: str) -> str:
    """
    Counts de number of letters in a text
    """
    num_char = {}
    for character in text.lower():
        num_char[character] = 0 
    for character in text.lower():
        num_char[character] += 1
    return num_char

def sort_dict(num_char: dict[str, int]) -> int:
    """
    Sorts a dictionary by its values in descending order.
    """
    new_list = []
    for key, value in num_char.items():
        new_list.append({"char": key, "num": value})
    new_list.sort(key=sort_on, reverse=True)
    return new_list

def sort_on(items):
    """
    Helper function to sort dictionary items by 'num' key.
    """
    return items["num"]
    