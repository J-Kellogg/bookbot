def main():
    book = "github.com/J-Kellogg/bookbot/books/frankenstein.txt"
    book_text = get_book_text(book)
    create_report(book_text, book)

def get_book_text(book):
    with open(book) as f:
        return f.read()

def word_count(book_text):
    words = book_text.split()
    return (len(words))
    
def character_count(book_text):
    text = book_text.lower()
    letters = {}
    for char in text:
        if char.isalpha():
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
    return letters

def create_letter_list(letter_dict):
    return [{"letter": key, "num": letter_dict[key]} for key in letter_dict]

    return letter_list

def sort_by_count(letter_list):
    return letter_list["num"]

def create_report(book_text, book):
    print(f"--- Begin report of {book} ---")
    print(f"{word_count(book_text)} words found in the document")
    print()
    letter_list = create_letter_list(character_count(book_text))
    letter_list.sort(reverse=True, key=sort_by_count)
    for letter in letter_list:
        print(f"The \'{letter["letter"]}\' character was found {letter["num"]} times")
    

    print("--- End Report ---")
    

main()