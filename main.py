# test.txt - тестовые данные из задания 301_26 - данный файл
f = open('test.txt', 'r', encoding='UTF-8')
n = int(f.readline())

a = [[int(y) for y in x.split()] for x in f]

# сортировка по возрастанию
a.sort(key=lambda x: x[1])

# инициализация переменных
min_start, finish, max_break, count = 0, 0, 0, 0

for i in a:
    if finish <= i[0]:  # если время окончания одного мероприятия меньше либо равна времени начала другого - подходит
        count += 1
        min_start = finish
        finish = i[1]
        max_break = i[0] - min_start

    if min_start <= i[0]:
        max_break = max(max_break, i[0] - min_start)
print(count, max_break)
