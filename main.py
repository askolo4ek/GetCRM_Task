#Словарь (хэш-таблица), где ключом является приоритет посещения места, а значением - время на его посещение
sights_dict = {
    1: 6,
    2: 4,
    3: 4,
    4: 3.5,
    5: 1.5,
    6: 5.5,
    7: 10,
    8: 5,
    9: 2,
    10: 5,
    11: 8,
    12: 7,
    13: 2,
    14: 1,
    15: 9,
    16: 7,
    17: 1,
    18: 3,
    19: 2,
    20: 12
}
#Словарь соответствий приоритета (ключ) и названия места (значение)
sights_names = {
    1: 'Всероссийский музей А.С. Пушкина и филиалы',
    2: 'Литературно-мемориальный музей Ф.М.Достоевского',
    3: 'Казанский собор',
    4: 'Кунсткамера',
    5: 'Екатерининский дворец',
    6: 'Зоологический музей',
    7: 'Петропавловская крепость',
    8: 'Русский музей',
    9: 'Спас на Крови',
    10: 'Исаакиевский собор',
    11: 'Эрмитаж',
    12: 'Зимний дворец Петра I',
    13: 'Музей восковых фигур',
    14: 'Петербургский музей кукол',
    15: 'Ленинградский зоопарк',
    16: 'Музей современного искусства Эрарта',
    17: 'Медный всадник',
    18: 'Музей микроминиатюры «Русский Левша»',
    19: 'Музей обороны и блокады Ленинграда',
    20: 'Навестить друзей'
}

flag = True
all_time = 32  #Время, которое у нас есть (48-16)
current_time = 0  #В этой переменной будет суммироваться время, когда мы посещаем определённое место (свободное время)
visited = []  #Здесь будет итоговый список посещённых мест


#Цикл будет работать пока мы не истратим всё свободное время
while flag and len(sights_dict) != 0:
    avg_time = round(sum(sights_dict.values()) / len(sights_dict), 0)  #Среднее время на посещение одного места, округлённое до целого
    #Проходимся по словарю, посещаем только места, на которое потратим не более среднего
    for key in sights_dict.copy():
        if sights_dict[key] <= avg_time:   #Проверка, что текущая достопримечательность не займёт много времени
            current_time += sights_dict[key]
            if current_time > all_time:  #Если уже не остаётся времени, то прерываем цикл и уезжаем домой
                current_time -= sights_dict[key]
                flag = False
                break
            sights_dict.pop(key)  #Удаляем посещённое место из словаря
            visited.append(sights_names[key])   #Добавляем посещённое место

#Красивый вывод
print('Посещённые места: ')
print(*visited, sep='\n')
print('-------------------------')
print("Потраченное время: ")
print(current_time)
print('-------------------------')
print('Количество мест: ')
print(len(visited))