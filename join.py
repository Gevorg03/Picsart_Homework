def join(data, sep):
    line = str(data[0])
    for i in range(1, len(data)):
        line += sep + data[i]
    return line    
data = input("Input a sentence: ")
sep = input("Input the word: ")
data = data.split(' ')
print(join(data, sep))
