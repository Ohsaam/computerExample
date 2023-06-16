#딕셔너리 예제1 
phone_book = {}
phone_book[홍길동] = "010-1234-5678"
print(phone_book)

#딕셔너리 예제2

phone_book = {"홍길동" : "010-2222-1111"}
print(phone_book)

#자료를 이와 같이 추가 할 수 있다.

phone_book["강감찬"]="010-1111-2222"
phone_book["허승"]="010-1321-2222"


dict = {'Name' : '홍길동', 'Age':7, 'Class' : '초급'}
print(dict['Name'])
print(dict['Age'])


phone_book = {'홍길동':'010-2222-4444', '강감찬' : '010-4444-3333', '이순신' : '1231231'}

print(phone_book['홍길동'])
#사전처럼 홍길동 단어를 찾고 -> 해당 매핑되는 내용에 드러가서 입력한다.


###몰랐던 부분 - 딕셔너리 선언 -> 키값설정하려면 ~~~.keys()) 선언하면 된다.

phone_book = {'홍길동' : '010-2131-2321', '이순신': '010-1231-2131'}

print(phone_book.keys())

#딕셔너리 키값을 설정한다. 

phone_book = { '홍길동': '010-1212-2311', '강감찬' : '010-1212-2445', '홍길동' : '010-2213-1323'}

for key in sorted(phone_book.keyss()):
    print(key,phone_book[key])



#딕셔너리 values()
phone_book = { '홍길동': '010-1212-2311', '강감찬' : '010-1212-2445', '홍길동' : '010-2213-1323'}

print(phone_book.values())#내용을 알고 싶으면 value로 해서 사용하면 된다.



#딕셔너리 del, pop 사용
phone_book = { '홍길동': '010-1212-2311', '강감찬' : '010-1212-2445', '허승' : '010-2213-1323'}

del phone_book['홍길동']
print(phone_book)

print(phone_book.pop('강감찬'))
print(phone_book)
#출력될 때, 그대로 출력된다.


#항목 모두 삭제

phone_book = { '홍길동': '010-1212-2311', '강감찬' : '010-1212-2445', '허승' : '010-2213-1323'}

phone_book.clear()
print(phone_book)


###딕셔너리 영한사전 만들기 

english_dict = {}
english_dict['one'] = '하나'
english_dict['two'] = '둘'
english_dict['three'] = '셋'

word = input("단어를 입력하세요 : ")

print(english_dict[word])


### 편의점 재고 관리 프로그램 #활용하기 좋은 문제 

items = {'커피' : 7, '펜': 3, '종이컵' : 10, '우유' : 5, '콜라' : 4, '라면' : 11}

print("판매 전 재고", items)


sell = input("판매한 물건을 입력하세요:")


if sell in items:
    items[sell] -= 1

else:
    print("판매 제품이 아닙니다")

print("판매 후 재고", items)


#딕셔너리 반복문

phone_book = { '홍길동': '010-1212-2311', '강감찬' : '010-1212-2445', '허승' : '010-2213-1323'}

for i in phone_book.keys():#홍길동, 강감찬 etc... 키 값을 출
    print(i)


for i in phone_book.values(): # 키값에 매핑되는 values 값들 출력한다. 
    print(i)


#key, values 동시 출력하는 방법
phone_book = { '홍길동': '010-1212-2311', '강감찬' : '010-1212-2445', '허승' : '010-2213-1323'}

for k,v in phone_book.items():
    print('{}의 전화번호는 {}입니다.'. format(k,v))

#format은 {} {} << 여기에 저장된 값을 넣어준다. 


#집합  

s = set()
s.add(10)
s.add(3)
print(s)

s.discard(5) #집합 항목 삭제
s.remove(2)
s.clear() #초기화 한다.

