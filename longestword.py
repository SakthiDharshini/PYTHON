IP = input()
length = 0
for word in IP.split():
    if(len(word)>length):
        length = len(word);
print(length)

