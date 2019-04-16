words = open("common words.txt").readlines()

score = int()

def quality(x):
    text = words
    print(x[0:3])
    for word in text:
        for part in word.split():
            if x[0:3] in part:
                print(word,'its here')
quality("zzzzzorange")