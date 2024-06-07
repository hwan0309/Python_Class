
#programming_dictionary 변수에 값 입력
programming_dictionary = {
    123: "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",

 }
#출력시 변수 안에 배열 이름 그대로 입력
print(programming_dictionary[123])

#변수안에 새로운 배열 추가
programming_dictionary ["Loop"] = "The action of doing something over and over againg"
print(programming_dictionary)

#변수 값 초기화
# programming_dictionary = []
# print(programming_dictionary)

#배열 값 수정
programming_dictionary [123] = "The new commit"
print(programming_dictionary[123])

#변수 값 중 key값 불러오기
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#----------------------------------------------------
    student_scores = {
        "Harry": 81,
        "Ron": 78,
        "Hermione": 99,
        "Draco": 74,
        "Neville": 62,
    }

    student_grades = {}

    for student in student_scores:
        score = student_scores[student]
        if score > 90:
            student_grades[student] = "Outstanding"
        elif score > 80:
            student_grades[student] = "Exceeds Expectations"
        elif score > 70:
            student_grades[student] = "Acceptable"
        else:
            student_grades[student] = "Fail"

    print(student_grades)
