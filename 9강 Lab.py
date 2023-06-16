import random

def match(c,m):
    if c == m:
        return '비겼습니다.'
    elif match_table[c] == m:
        return '졌습니다.'

    else:
        return '이겼습니다.'

rps_dic = {1:'가위', 2:'바위', 3:'보'}
match_table = {'가위' :'보' , '바위': '가위', '보' : '바위' }

computer = rps_dic[random.randint(1,3)]
mine = input('가위, 바위, 보 입력: ')
result = match(computer, mine)


print(result)



#행맨

import random

#infile = open() 
lines = infile.realines()
word = random.choice(lines).rstrip()

solution = list(word)
result = list('_' + len(word))
turns = 10

while turns > 0:
    guess = input("단어를 추측하세요 : ")
    turns -= 1

    i = 0

    for c in word:
        if c == guess:
            result[i] = c
        i += 1


    print(result)


    if result == solution:
        print("성공입니다.")
        break

    if turns <= 0:
        print("실패했습니다")
        break

