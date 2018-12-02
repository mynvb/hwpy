
# 1

geo_logs = [
{'visit1': ['Москва', 'Россия']},
{'visit2': ['Дели', 'Индия']},
{'visit3': ['Владимир', 'Россия']},
{'visit4': ['Лиссабон', 'Португалия']},
{'visit5': ['Париж', 'Франция']},
{'visit6': ['Лиссабон', 'Португалия']},
{'visit7': ['Тула', 'Россия']},
{'visit8': ['Тула', 'Россия']},
{'visit9': ['Курск', 'Россия']},
{'visit10': ['Архангельск', 'Россия']},
]

for i in range(len(geo_logs)):
    for key, value in geo_logs[i].items():
        if 'Россия' in value:
            print(key, value)


# 2

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

new=[]
for i in ids.values():
    new=new+i
print(list(set(new)))

# 3 (реализуется с помощью словарей, ключ - длина запроса в виде целого числа, значение - процент)
queries = [
'смотреть сериалы онлайн',
'новости спорта',
'афиша кино',
'курс доллара',
'сериалы этим летом',
'курс по питону',
'сериалы про спорт',
]

num=dict()
for i in range(len(queries)):
    lst = queries[i].split(' ')
    length_of_q = len(lst)
    if length_of_q not in num:
        num[length_of_q] = 1
    else:
        num[length_of_q] += 1
for i, j in num.items():
    j = round(j / len(queries) * 100)
    print('Запросов длиной в {} слова: {}%'.format(i, j))



# 4 предполагаем, что список влезает в память
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
result = sorted(stats.items(), key=lambda x: x[1], reverse=True)
print(result[0])

# 5
stream = [
'2018-01-01,user1,3',
'2018-01-07,user1,4',
'2018-03-29,user1,1',
'2018-04-04,user1,13',
'2018-01-05,user2,7',
'2018-06-14,user3,4',
'2018-07-02,user3,10',
'2018-03-21,user4,19',
'2018-03-22,user4,4',
'2018-04-22,user4,8',
'2018-05-03,user4,9',
'2018-05-11,user4,11',
]

watch = None
unique_users = list()
for line in stream:
    spl = line.split(',')
    if spl[1] not in unique_users:
       unique_users.append(spl[1])
    else:
        continue
    if watch is None:
        watch = int(spl[2])
    else:
        watch = watch + int(spl[2])
        
print(watch/len(unique_users))

#6

stats = [
['2018-01-01', 'google', 25],
['2018-01-01', 'yandex', 65],
['2018-01-01', 'market', 89],
['2018-01-02', 'google', 574],
['2018-01-02', 'yandex', 249],
['2018-01-02', 'market', 994],
['2018-01-03', 'google', 1843],
['2018-01-03', 'yandex', 1327],
['2018-01-03', 'market', 1764],
]

pairs=dict()
for line in stats:
    pairs[(line[0], line[1])] = line[2]
print(pairs)

#6*
pairs=dict()
for line in stats:
    *middle, last = line
    list_to_tuple = tuple(middle)
    pairs[list_to_tuple] = last
print(pairs)
