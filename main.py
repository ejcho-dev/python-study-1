# print("Hello Python!")

# 문자열
# x = "파이썬은 재미있어요."
# print(x)

# y = '프로그래밍'
# print(y)

# 문자열 내에 따옴표가 있는 경우
# print ("그는 \"파이썬을 배우세요.\"라고 말했다.")

# 정수와 실수
# x = 30.2
# print(x)
# print(x + 10.4)

# 참거짓
# x = False
# print(x)

# 타입 출력
# print(type("10"))
# print(type(10))
# print(type(10.0))
# print(type(True))

# 예약어 출력
# import keyword
# print(keyword.kwlist)

# import = "예약어"
# print(import) # 예약어이므로 오류 발생

# 주석
# var = "문자열입니다."
# print(var) # 변수의 값을 출력합니다.
'''
여러 줄의 주석을
작성할 수 있습니다
'''
from mouseinfo import screenshot

# 입출력
# name = input("Name: ")
# contact = input("Contact: ")
# print("이름: " + name)
# print("연락처: " + contact)

# 연산
# x = 7
# y1 = x + 5
# y2 = x - 5
# y3 = x * 5
# y4 = x / 5
# print(y1)
# print(y2)
# print(y3)
# print(y4)

# 산술 연산자
# a = 25
# b = 13
# print(a // b)
# print(a % b)

# 비교 연산자
# a = 25
# b = 13
# print(a > b)
# print(a == b)
# print(a < b)

# 논리 연산자
# print(not True)
# print(True and True)
# print(True and False)
# print(True or False)

# 축약 연산자
# a = 0
# a = a + 7
# a += 7
# print(a) # 14
# a *= 3
# print(a) # 42

# 조건문
# weather = "맑음"
# if weather == "비":
#     print("비가 많이 옵니다.")
#     print("우산을 챙겨 나가세요.")
# elif weather == "눈":
#     print("눈이 옵니다.")
#     print("눈이 오니 우산을 챙기세요")
# elif weather == "흐림":
#     print("날씨가 흐립니다.")
#     print("강수 확률을 확인하세요.")
# else:
#     print("비가 오지 않습니다.")
#     print("우산을 챙기지 않아도 괜찮습니다.")

# 문자열 인덱싱
# string = "Hello World"
# print(string[0])
# print(len(string))

# 문자열 슬라이싱
# string = "Hello World"
# print(string[0:5])
# print(string[0:5:2])
# print(string[0::2])
# print(string[6:])
# print(string[6:-2])
# print(string[4::-1])

# 문자열 자르기
# string = "Hello World Python!"
# print(string.split(' '))
# print(string.split(' ')[1])

# 이스케이프
# print('[ 공지글 ]\n오늘 새롭게 서비스가 \'런칭\'되었습니다.')
# print('파일 경로: C:\\Temp\\Project')

# 리스트
# score_list = [98, 87]
# print(score_list)
#
# mixed_list = ['홍길동', 98, '임꺽정', 93]
# print(mixed_list)

# 리스트 인덱스
# score_list = [98, 78, 83, 94, 100]
# print(score_list)
# score_list[3] = 68
# print(score_list)
# print(score_list[-3])

# 리스트 슬라이싱
# score_list = [98, 78, 83, 94, 100, 97, 85]
# score_list= score_list[0:5]
# print(score_list)
# print(score_list[0:3])
# print(score_list[0:-2])
# print(score_list[4:1:-1])

# 리스트 삽입
# score_list = []
# score_list.append(88)
# score_list.append(93)
# score_list.append(97)
# print(score_list)

# score_list = [98, 95, 100]
# score_list.insert(1, 97)
# score_list.insert(4, 98)
# print(score_list)

# 리스트 원소 삭제
# score_list = [98, 95, 100]
# del score_list[0]
# print(score_list)
# del score_list[-1]
# print(score_list)

# 튜플
# tuple_var = ('홍길동', '이순신', '신립')
# print(tuple_var)
# print(tuple_var[0])
# print(tuple_var[0:2])
# tuple_var[0] = '임꺽정' #오류 발생

# 시퀀스 자료형 --> 문자열, 리스트, 튜플

# 시퀀스 자료형 연산
# tuple_var = (1, 2, 3)
# tuple_var2 = (4, 5, 6)
# list_var = [1, 2, 3]
# print(tuple_var + tuple_var2)
# print(list_var + tuple_var) # 오류 발생

# 원소 확인
# list_var = [1, 2, 3, 4, 5, 6]
# print(3 in list_var) # True
# print(7 in list_var) # False

# 반복문
# todo_list = ['이메일 확인하기', '거래처 미팅하기', '보고서 작성하기',
#              'cs 응대하기', '비품 정리하기', '택배 출고하기']
# print(f"오늘 업무: {todo_list[0]}")
# print(f"오늘 업무: {todo_list[1]}")
# print(f"오늘 업무: {todo_list[2]}")
# print(f"오늘 업무: {todo_list[3]}")
# print(f"오늘 업무: {todo_list[4]}")
# print(f"오늘 업무: {todo_list[5]}")
'''
 for todo in todo_list:
     print(f"오늘 업무: {todo}")
'''
# 반복문과 조건문 함께 사용하기
# forecast = ['맑음', '맑음', '비', '맑음', '눈',
#             '맑음', '비', '눈', '눈', '눈']
# 
# rain_snow_days = 0
# 
# for condition in forecast:
#     if condition == '비' or condition == '눈':
#         rain_snow_days += 1
# 
# print(f"{len(forecast)}일 간 비나 눈이 온 날짜는 {rain_snow_days}일입니다.")

# continue 건너뛰기
# number_list = [1, 2, 3, 4, 5, 6]
#
# for number in number_list:
#     if number % 2 == 0:
#         continue # 짝수 건너뛰기
#     print(number)
#
# print("홀수만 찾았습니다.")

# range
# months = ['1월', '2월', '3월', '4월', '5월', '6월',
#           '7월', '8월', '9월', '10월', '11월', '12월']
# rainfall = [20, 50, 5, 10, 20, 80, 100, 40, 15, 10, 20, 10]
# 
# for i in range(12):
#     if rainfall[i] > 50:
#         print(f"{months[i]}은 강수량이 많았던 달입니다. 강수량: {rainfall[i]}mm")

# while문
# i = 0
#
# while i < 10:
#     i = i + 1
#     print(f"{i}번째 반복 중")

# 딕셔너리 자료형
# english_dict = {}
# english_dict['사과'] = 'Apple'
# print(english_dict['사과'])

# user = {
#     "id": "gildong",
#     "pw": "1234"
# }
#
# print(user["id"])
# print(user["pw"])

# book_stock = {
#     "알라딘": 4,
#     "신데렐라": 2,
#     "비전공자를 위한 이해할 수 있는 파이썬": 8,
#     "백설공주": 3
# }

# for key in book_stock.keys():
#     print(f"key: {key}, value: {book_stock[key]}")

# for book, stock in book_stock.items():
#     if stock < 5:
#         print(f"{book}의 재고: {stock}권")

# score_dict = {}
# score_dict['홍길동'] = 85
# score_dict['임꺽정'] = 98
# print(score_dict['홍길동'])
# del score_dict['홍길동']
# print(score_dict['홍길동']) # 오류 발생

# score_dict = {
#     "사과": "Apple",
#     "바나나": "Banana",
#     "당근": "Carrot"
# }
# key_list = list(score_dict.keys())
# value_list = list(score_dict.values())
# print(key_list)
# print(value_list)

# import pyautogui
# # 스크린샷 찍기
# screenshot = pyautogui.screenshot()
#
# # 스크린샷 저장하기 (파일명은 원하는대로 지정)
# screenshot.save("screenshot.png")

# 함수
# def avg_of_three(a, b, c):
#     total = (a + b + c) / 3
#     return total
#
# print(avg_of_three(10, 20, 30))
# print(avg_of_three(12, 24, 30))
# print(avg_of_three(100, 120, 300))

# def add(a, b):
#     print(a + b)
#
# add(10, 20)

# def operator(a, b):
#     add_var = a + b
#     subtract_var = a - b
#     multiply_var = a * b
#     divide_var = a / b
#     return add_var, subtract_var, multiply_var, divide_var
#
# a, b, c, d = operator(7, 3)
# print(a, b, c, d)

# import math
# print(math.floor(3.5))
# print(math.sqrt(4))
# print(math.pow(3,2))

# import lib
# from lib import add_num
# import lib as l
# sum = l.add_num(2, 5)
# print(sum)

# class MyClass:
#     var = '클래스 멤버'
#     def func(self):
#         print('클래스 메소드')
#
# obj = MyClass() # 객체 초기화
# print(obj.var)
# obj.func()

# class Student:
#     def set_id(self, id):
#         self.id = id
#     def set_name(self, name):
#         self.name = name
#     def set_age(self, age):
#         self.age = age
#     def show(self):
#         print(self.id, self.name, self.age)
#
# student = Student()
# student.set_id('20153157')
# student.set_name('홍길동')
# student.set_age(24)
# student.show()
#
# student2 = Student()
# student2.set_id('20153156')
# student2.set_name('이순신')
# student2.set_age(27)
# student2.show()
# Student.show(student) #클래스 이름으로 메소드 호출

# class Student:
#     def __init__(self, id, name, age):
#         self.id = id
#         self.name = name
#         self.age = age
#     def show(self):
#         print(self.id, self.name, self.age)
# 
# student = Student('20153157', '홍길동', 24)
# student.show()

# class Human:
#     race = '인간' # 클래스 멤버
#     count = 0 # 클레스 멤버
#     def __init__(self):
#         Human.count += 1
#     def set_job(self, job):
#         self.job = job # 인스턴스 멤버
#     def show(self):
#         print(self.count, self.race, self.job)
#
# human1 = Human()
# human1.set_job('프로그래머')
# human1.show()
# human2 = Human()
# human2.set_job('농구선수')
# human2.show()

# class Student:
#     count = 0
#     def __init__(self, id, name, age): # 생성자
#         self.id = id
#         self.name = name
#         self.age = age
#         Student.count += 1
#     def show(self):
#         print(self.id, self.name, self.age)
#     def __del__(self): # 소멸자
#         Student.count -= 1
#
# student1 = Student('20153157', '홍길동', 24)
# student2 = Student('20153158', '이순신', 25)
# print(Student.count)
# del student1
# print(Student.count)

class Unit:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(self.name, "이(가) 공격을 수행합니다. [공격력:", self.power, "]")

class Monster(Unit):
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type
    def show_info(self):
        print("몬스터 이름:", self.name, "/ 몬스터 종류:", self.type)

monster = Monster("슬라임",10, "초급")
monster.show_info()
monster.attack()