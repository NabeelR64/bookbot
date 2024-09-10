def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    # print(count_words(text))
    dicc = count_letter(text)
    ne = dict(sorted(dicc.items(), key=lambda item: item[1], reverse=True))
    for k in ne:
        print("Char", k, "appears", ne[k], "times in the book.")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_letter(text):
    dic = {}
    text = text.lower()
    for i in text:
        if i.isalpha():
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
    return dic
main()
