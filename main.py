def main():
    bookp = "books/frankenstein.txt"
    with open(bookp) as f:
        file_c = f.read()
        words = len(file_c.split())
        b = countc(file_c)
        docu(bookp, words, b)

def countc(din):
    di = din.lower()
    d = {}
    for x in di:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    return d

def docu(bookp, wrd, dic):
    print(f"--- Begin report of {bookp} ---")
    print(f"{wrd} words foud in the document")
    y = sorto(dic)
    for i in y:
        print(f"The {i[0]} character was found {i[1]} times")
    print(f"--- End report ---")

def sorto(dic):
    sor = []
    for i, j in dic.items():
        if i.isalpha():
            sor.append([i, j])
    sor.sort(key= lambda x: x[1], reverse=True)
    return sor

if __name__ == "__main__":
    main()
