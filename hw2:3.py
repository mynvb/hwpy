import requests

# 1
data1 = [
    [13, 25, 23, 34],
    [45, 32, 44, 47],
    [12, 33, 23, 95],
    [13, 53, 34, 35],]

def count(inp):
    sum1 = 0
    for i in range(len(inp)):
        if len(inp) != len(inp[i]):
            print('Check matrix dimension')
        sum1 = sum1 + inp[i][i]
    print(sum1)
count(data)

# 2
data2 = [1, '5', 'abc', 20, '2']
def sum_int(inp):
    sum2 = 0
    for i in inp:
        try: sum2 = sum2 + int(i)
        except: continue
    print(sum2)
sum_int(data2)

# 3 

def find_max_FErate():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    cur = response.json()['Valute']
    max_value = None
    name = None
    for key, value in cur.items():
        if max_value is None:
            max_value = value['Value']
        if max_value < value['Value']:
            max_value = value['Value']
            name = value['Name']
    print(name)
find_max_FErate()

# 4 
class Rate:
    def __init__(self, format='value', diff=False):
        self.format = format
        self.diff = diff
    
    def exchange_rates(self):
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']
    
    def make_format(self, currency):
        response = self.exchange_rates()
        
        if currency in response:
            if self.format == 'full':
                if self.diff is True:
                    return response[currency]['Value'] - response[currency]['Previous']
                return response[currency]
            
            if self.format == 'value':
                return response[currency]['Value']
            
            if self.format == 'name':
                return response[currency]['Name']
            
            if self.diff is True:
                return response[currency]['Value'] - response[currency]['Previous']
        
        return 'Error'
    
    def eur(self):
        """Возвращает курс евро на сегодня в формате self.format"""
        return self.make_format('EUR')
    
    def usd(self):
        """Возвращает курс доллара на сегодня в формате self.format"""
        return self.make_format('USD')
print(Rate(format='full', diff=True).usd())

# 5
def first_n(n):
    a = [0,1]
    while len(a) < n:
        next_num = a[len(a)-1] + a[len(a)-2]
        a.append(next_num)
    return sum(a)
print(first_n(6))


        
