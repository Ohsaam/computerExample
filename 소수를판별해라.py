import time

start = time.time()

n = int(input("n값을 입력하세요"))

count = 1

for a in range(2, n+1):
    if n % a == 0:
        count += 1


if(count == 2):
    print("소수입니다.")


else:
    print("소수가 아닙니다.")

print("time: ", time.time() -start)


##2가지 방법


for a in range(2, n+1):
    if n % 2 == 0:
        count += 3
        break


    elif n % a == 0:
        count += 1

        
##3가지 방법[입력한 수가 소수더라도 2부터 그 수까지 따질 필요 x]

b = (n+1) //2 #거르는 작업

for a in range(2,b):
    if n % 2 == 0:
        count += 3
        break

    elif n % a == 0:
        count += 1


#에라토스테네스의 채

n = 1000
number = [False, False] + [True] *(n-1)

primes = []

for i in range(2, n+1):
    if number[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            number[j] = False

print(primes)


        
