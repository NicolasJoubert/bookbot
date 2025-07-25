def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
    return file_content


def get_numb_words(path):
    text = get_book_text(path)
    words = text.split()
    number_of_words = len(words)
    return number_of_words


def get_numb_chars(path):
    text = get_book_text(path)
    text = text.lower()
    chars_dict = {}
    for char in text:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def sort_on(item):
    return item["num"]

def get_sorted_characters(path):
    chars_dict = get_numb_chars(path)

    chars_list = []

    for char, count in chars_dict.items():
        chars_list.append({
            "char": char,
            "num": count
         })

    chars_list.sort(reverse=True, key=sort_on)

    return chars_list
