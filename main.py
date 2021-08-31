import pandas as pd
import numpy as np

data = pd.read_excel("Страны и территории.xlsx")


while 1:
    numbers = np.random.randint(0, len(data.iloc[::]), 3)

    countrys = list(data['Страна или территория'].iloc[numbers])

    capitals = list(data['Столица'].iloc[numbers])
    areas = list(data['Площадь, км^2'].iloc[numbers])

    num_of_people = list(data['Население, чел.'].iloc[numbers])
    continent = list(data['Континент'].iloc[numbers])


    ind = np.random.randint(0, 2)
    print(f"Страна - {countrys[ind]}\
            Столицы - {capitals}")

    inp = input("Введите правильную столицу: ")

    if inp == capitals[ind]:
        print("Верно!!!")
        print(f"В этом госуд-ве проживают {num_of_people[ind]} людей.\
            Площадь госуд-ва - {areas[ind]} км^2.\
            Также эта страна находиться на континенте - {continent[ind]}")
    else:
        print("Не верно :((")
        print(f"Страна - {countrys[ind]}, Столица - {capitals[ind]}")
        print(f"В этом госуд-ве проживают {num_of_people[ind]} людей.\
            Площадь госуд-ва - {areas[ind]} км^2.\
            Также эта страна находиться на континенте - {continent[ind]}")
