import random


infile = open("D:\\hangman.txt","r")
lines = infile.readline()
word = random.choice(lines).rstrip()


solution = list(word)
result = list('_' * len(word))


print("turtle")
print(list("turtle"))
print(list("_"*len("turtle")))

turns = 10

while turns > 0:
    guess = input("단어를 추측하세요:")
    turns -= 1
    i = 0

    for c in word:
        if c == guess:
            result[i] = c
        i +=1

    if result == solution:
        print("성공입니다.")
        break

    if turns <= 0:
        print("실패하였습니다.")
        break
    

infile.close()

