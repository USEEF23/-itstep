class Soda:
    print("1-лимон\n"
          "2-чай\n"
          "3-клубника\n"
          "4-персик\n"
          "5-груша\n"
          "6-ничего\n")
    n=int(input("Выберите добавку из меню (только номер)"))
    if n==1:
        print("Лимонад с лимоном")
    elif n==2:
        print("Айс ти")
    elif n==3:
        print("Клубничный лимонад")
    elif n==4:
        print("Лимонад с персиком")
    elif n==5:
        print("Дюшес")
    elif n==6:
        print("Простой лимонад")
Soda()