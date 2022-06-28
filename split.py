def split(source, sep, count):
    lst = []
    new_lst = []
    word_size = len(sep)
    start = 0
    n = 0
    for i in range(count):
        lst.append(source.index(sep, start))
        start = source.index(sep, start) + 1
    lst.append(len(source))
    for i in range(count + 1):
        line = ""
        for j in range(n, lst[i]):
            line += source[j]
        new_lst.append(line)
        n = lst[i] + word_size
    return new_lst
source = input("Input a sentence: ")
sep = input("Input the substring, that must divided according that: ")
count = source.count(sep)
print(split(source, sep, count))
