def get_book_text():
    with open('./books/frankenstein.txt') as f:
        file_content = f.read()
    return file_content

def get_number_of_words():
    text = get_book_text()
    words = text.split()
    number_of_words = len(words)
    return number_of_words



def main():
  print(f'{get_number_of_words()} words found in the document')

main()