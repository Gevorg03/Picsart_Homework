def replace(source, old, new, count):
    source = source.split(' ')
    for i in range(count):
        if source[i] == old:
            source[i] = new
    source = ' '.join(source)
    return source
source = input("Input a sentence: ")
old = input("Input the word, that must be changed: ")
new = input("Input the word, that must be replaced: ")
count = len(source.split(' '))
print(replace(source, old, new, count))
