day=0
k=[]
l=0
grades=[]
names=["Elon Tusk","Melon Musk","Bill Fames","Jack Morton","Jamshut Yakubovich"]
import random
class human():
    students_choose=input("Enter your name and surname: ")
    age=int(input("Enter your age: "))
    vib=input("Choose your rang: (s/t)")
if human.vib=="s":
    print("Congratulations you are......")
    print("Student")
    for m in range(50):
        day+=1
        if human.vib=="s":
            class student():
                print(f"{human.students_choose}'s day number {day}")
        if day%10==0:
            if human.vib=="s":
                class tests_s():
                    r=random.randint(1,2)
                    student_answer = []
                    result = 0
                    if r == 1:
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
                        y=input("Do you want to see your results? (y/n): ")
                        if y == "y":
                            print(result)
                        k.append(result)
                        result = 0
                        i = 0
                    elif r == 2:
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
                        y=input("Do you want to see your results? (y/n): ")
                        if y == "y":
                            print(result)
                        k.append(int(result))
                        result = 0
                        i = 0
        if m==49:
            for h in k:
                l+=h
            print(l)
            print("-----Graduation Day-----")
            print("Your graduation grade:",l/2)
            with open("grad.txt","w") as FileHandler:
                FileHandler.write(f"Name: {human.students_choose} | Average point: {l/2}")
elif human.vib=="t":
    print("Congratulations you are......")
    print("Teacher")
    for z in range(50):
        day+=1
        if human.vib=="t":
            class teacher():
                print(f"{human.students_choose}'s day number {day}")
                if day%10==0:
                    randname=random.randint(0,4)
                    rand_grade=random.randint(0,100)
                    print("Graduate students performance")
                    print(f"Name: {names[randname]} | {rand_grade} points")
                    grades.append(names[randname])
                    grades.append(rand_grade)
                    grad=input(f"Graduate student (Test {day//10}) A/B/C/D/E: ")
                    grades.append(grad)
    print("------Graduation Day-------")
    print("Thank you for your job :), now you will receive the file with students grades")
    with open("results.txt","w") as filehandler:
        filehandler.write(f"{grades}")