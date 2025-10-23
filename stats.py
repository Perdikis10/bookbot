def get_number_of_words(text):
    """Returns the number of words in the given text."""
    words = text.split()
    return len(words) 

def num_characters(text):
    lowercase_text = text.lower()
    num_chars = {}
    for char in lowercase_text:
        if char.isalpha():
            if char in num_chars:
                num_chars[char] += 1
            else:
                num_chars[char] = 1
    return num_chars    


def sorted_list_of_dictionaries(list_of_dicts, key):
    """Sorts a list of dictionaries based on the specified key."""
    return sorted(list_of_dicts, key=lambda x: x[key])