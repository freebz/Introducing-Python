# 4.4 반복하기: while

count = 1
while count <= 5:
    print(count)
    count += 1

# 1
# 2
# 3
# 4
# 5


# 4.4.1 중단한기: break

while True:
    stuff = input("String to capitalize [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())

# String to capitalize [type q to quit]: test
# Test
# String to capitalize [type q to quit]: hey, it works
# Hey, it works
# String to capitalize [type q to quit]: q


# 4.4.2 건너뛰기: continue

while True:
    value = input("Integer, please [q to quit]: ")
    if value == 'q':  # 종료
        break
    number = int(value)
    if number % 2 == 0:  # 짝수
        continue
    print(number, "squared is", number*number)

# Integer, please [q to quit]: 1
# 1 squared is 1
# Integer, please [q to quit]: 2
# Integer, please [q to quit]: 3
# 3 squared is 9
# Integer, please [q to quit]: 4
# Integer, please [q to quit]: 5
# 5 squared is 25
# Integer, please [q to quit]: q


# 4.4.3 break 확인하기: else

numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else:  # break가 호출되지 않았다.
    print('No even number found')

# No even number found
