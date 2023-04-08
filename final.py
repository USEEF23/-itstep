day=10
k=0
names=["Elon Tusk","Melon Musk","Bill Fames","Jack Morton","Jamshut Yakubovich"]
import random
class human():
    students_choose=input("Enter your name and surname: ")
    age=int(input("Enter your age: "))
    vib=input("Choose your rang: (s/t)")
for i in range(50):
    if human.vib=="s":
        class student():
            print("Congratulations you are......")
            print("Student")
            print(f"{human.students_choose}'s day number {day}")
    if day%10==0:
        if human.vib=="s":
            class tests_s():
                r=random.randint(1,2)

                student_answer = []
                result = 0
                if r == 1:
                    students_choose = input("Enter your name and surname: ")
                    age = int(input("Enter your age: "))
                    answers1 = [10, 343, 1, 54, 21, 1, 3, 2, 4, 1024]
                    print(f"------TEST{int(day / 10)}-------")
                    student_answer.append(int(input("1)2+8=")))
                    student_answer.append(int(input("2) 7^3=")))
                    student_answer.append(int(input("3) 3^0=")))
                    student_answer.append(int(input("4) 6*9=")))
                    student_answer.append(int(input("5) 7*3=")))
                    student_answer.append(int(input("6) 7/7=")))
                    student_answer.append(int(input("7) 9/3=")))
                    student_answer.append(int(input("8) 8/4=")))
                    student_answer.append(int(input("9) (8^2)/(4^2)=")))
                    student_answer.append(int(input("10) 2^10=")))
                    for i in range(len(answers1)):
                        if answers1[i] == student_answer[i]:
                            result += 10
                            i += 1
                    student_answer = []
                    with open("results.txt", "w") as fileHandler:
                        fileHandler.write(f"{human.students_choose} | {result} points | Age : {human.age}")
                    k += result
                    y=input("Do you want to see your results? (y/n): ")
                    if y == "y":
                        print(result)
                    result = 0
                    i = 0
                elif r == 2:
                    students_choose = input("Enter your name and surname: ")
                    age = int(input("Enter your age: "))
                    answers2 = [11, 36, 6561, 63, 5, 5, 1, 4, 2, 512]
                    print(f"------TEST{int(day / 10)}-------")
                    student_answer.append(int(input("1)2+9=")))
                    student_answer.append(int(input("2) 6^2=")))
                    student_answer.append(int(input("3) 3^8=")))
                    student_answer.append(int(input("4) 9*7=")))
                    student_answer.append(int(input("5) 5*1=")))
                    student_answer.append(int(input("6) 1*5=")))
                    student_answer.append(int(input("7) 1^2023=")))
                    student_answer.append(int(input("8) 8/2=")))
                    student_answer.append(int(input("9) (8^1)/(4^1)=")))
                    student_answer.append(int(input("10) 2^9=")))
                    for i in range(len(answers2)):
                        if answers2[i] == student_answer[i]:
                            result += 10
                            i += 1
                    with open("results.txt", "w") as fileHandler:
                        fileHandler.write(f"{human.students_choose} | {result} points | Age: {human.age}")
                    y=input("Do you want to see your results? (y/n): ")
                    k+=result
                    if y == "y":
                        print(result)
                    result = 0
                    i = 0

print("-----Graduation day-----")
print("Your graduation grade:",k/5)
for z in range(50):
    if human.vib=="t":
        class teacher():
            print(human.vib)
            print(f"{human.students_choose}'s day number {day}")
            rand_grade=random.randint(0,100)

            print("Graduate students performance")