happiness = 0
class chelovek:
    class name:
        name=input("Введите ФИО: ")
    class age:
        age=int(input("Введите год рождения: "))
    class rassa:
        r=input("Введите рассу (экватор\север\юг): ")
    class continent:
        c=input("Введите континент (европа\азия\южная америка\северная америка\австралия\африка): ")
    class color:
        co=input("Введите цвет кожи (чёрный\белый): ")
    class educ:
        e=input("образование есть? (д\н): ")
        if e=="д":
            ea="есть"
        elif e=="н":
            ea="нету"

print("ФИО"+"-"+chelovek.name.name)
print("Год рождения"+"-",chelovek.age.age)
print("Расса"+"-"+ chelovek.rassa.r)
print("Материк"+"-"+chelovek.continent.c)
print("Цвет кожи"+"-"+chelovek.color.co)
print("Образование"+"-"+chelovek.educ.ea)