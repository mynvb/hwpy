from datetime import datetime
# 1, 2


start_date = '07.08.2018'
end_date = '10.08.2018'
def days(start_date, end_date):
    final = []
    try:
        start_date_format = datetime.strptime(start_date, '%d.%m.%Y')
        end_date_format = datetime.strptime(end_date, '%d.%m.%Y')
        current_date = start_date_format
        if end_date_format > start_date_format:
            while current_date < end_date_format:
                current_date = current_date + timedelta(days=1)
                current = current_date.strftime('%Y-%m-%d')
                final.append(current)
            return final
        else: 
            return []
    except:
        return 'invalid data, check your input'
    
days(start_date, end_date)


# 3 
stream = ['2018-04-02', '2018-02-29', '2018-19-02']

def check_stream(stream):
    #В качестве аргумента принимает список
    for i in stream:
        try:
            date = datetime.strptime(i, '%Y-%m-%d')
            print(i, True)
        except:
            print (i, False)

check_stream(stream)

# 4 
def days_of_month():
    from datetime import datetime
    current = datetime.now()
    if current.day == 1:
        prev = current
        mon = current.month-1
        while prev.month == mon:
            prev = prev - timedelta(days=1)
            if prev.day == 1: 
                print(prev)
                break
            print(prev)
    else:
        date_output = current 
        while date_output.month == current.month:
            date_output = date_output - timedelta(days=1)
            if date_output.day == 1: 
                print(date_output)
                break
            print(date_output)
# 5

def find_day():
    inp = input('Enter "today" or "last monday" or "last day"')
    today = datetime.today()
    if inp == "today":
        return today.strftime('%Y-%m-%d')
    if inp == "last monday":
        if today.strftime('%A') == 'Monday': return today
        else:
            prev_date = today
            while not prev_date.strftime('%A') == 'Monday':
                prev_date = prev_date - timedelta(days = 1)
            return prev_date.strftime('%Y-%m-%d')
    if inp == "last day":
        last_day = today
        while last_day.month == today.month:
            last_day = last_day + timedelta(days=1)
        last_day = last_day - timedelta(days=1)
        return last_day.strftime('%Y-%m-%d')
find_day()

#6

start = '2018-12-07'
end = '2018-12-26'
def weeks(start, end):
    week_list = []
    start_format = datetime.strptime(start, '%Y-%m-%d')
    end_format = datetime.strptime(end, '%Y-%m-%d')

    middle = start_format
    while middle != end_format:
        week = []
        while middle != end_format:
            if middle == start_format:
                week.append(middle.strftime('%Y-%m-%d'))
            middle = middle + timedelta(days = 1)
            if middle.strftime('%A') == 'Sunday':
                week.append(middle.strftime('%Y-%m-%d'))

                if len(week) == 7:
                    week_list.append(week)
                break
            week.append(middle.strftime('%Y-%m-%d'))

    return week_list

weeks(start, end)
