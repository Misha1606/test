a=input('Введите жест для первого игрока ')
b=input('Введите жест для второго игрока ')
if a=='камень' and b=='бумага':
    print("a lost, b won")
elif a=='бумага' and b=='камень':
    print("a won, b lost")
elif a=='камень' and b=='ножницы':
    print("a won, b lost")
elif a=='ножницы'and b=='камень':
    print("a lost, b won")
elif a=='ножницы'and b=='бумага':
    print("a won, b lost")
elif a=='бумага' and b=='ножницы':
    print("a lost, b won")
elif a=='бумага' and b=='бумага':
    print("ничья")
elif a=='ножницы'and b=='ножницы':
    print("ничья")
elif a=='камень' and b=='камень':
    print("ничья")
else:
    print("ERROR")

