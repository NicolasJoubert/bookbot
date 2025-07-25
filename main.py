def get_book_text():
    with open('./books/frankenstein.txt') as f:
        file_content = f.read()
    return file_content

def main():
    print(get_book_text())

main()
