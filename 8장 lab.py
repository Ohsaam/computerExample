import random

def match(c,m):
    if c == m:
        return '비겼습니다.'

    elif match_table[c]==m:
        return '졌습니다.'

    else:
        return '이겼습니다.'


rps_dic = {1 : '가위', 2 : '바위' , 3:'보'}
match_table = 
