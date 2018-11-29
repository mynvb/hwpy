import math

# 1
long_phrase = 'Насколько проще было бы писать программы, если бы не заказчики'
short_phrase = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
def compare (long, short):
	print(len(long)>len(short))

compare(long_phrase, short_phrase)

# 2.1
text = 'Если программист в 9-00 утра на работе, значит, он там и ночевал'
d=dict()
for letter in text:
        if letter not in d:
                d[letter]=1
        if letter in d:
                d[letter]+=1
result='В строке text {} букв "а" и {} букв "и"'.format(d['а'], d['и'])
print(result)

# 2.2

if len(text.replace('и','')) < len(text.replace('а','')):
        print('В строке больше букв "и"')
else:
        print('В строке больше букв "а"')

# 3
byte=213680000
megabyte=byte/(10**6)
print('Объем файла равен {}Mb'.format(megabyte))

# 4
sin=math.sin(math.pi/6)
print(sin)

''' 5 дробные числа не могут быть представлены в точности в бинарном виде,
поэтому значения округляются, и такие операции,
как 0.1+0.2, дают неточный результат  '''


# 5
def exchange (a, b):
        b=b-a
        a=a+b
        b=a-b
        print('a=',a,'b=',b)
exchange(120,1)

# 6
# разбиваем число на элементы, получаем спискок
num=10011
st=str(num)
st.split()
l=len(st)-1
print(l)
# создаем новый список куда добавим вычисляемые значения
new_num=list()
# вычисляем каждый элемент (умножение на 2 в степени номера эл-та)
k=-1
for i in st:
        k=k+1
        i=int(i)*(2**(l-k))
        print(i)
        new_num.append(i)
result=sum(new_num)
print(result)
