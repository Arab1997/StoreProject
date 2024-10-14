import requests



s_city = "Minsk,BY"
city_id = 625144
appid = "bf92102ecd82d3994af53c403681fbd1"


def Weather_3_hours():
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast/",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        result = []
        for i in data['list'][:2]:
            date = i['dt_txt'][10:16]
            result.append(date)
        return result
    except Exception as e:
        print("Exception (forecast):", e)
        pass


def Weather_3_temp():
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast/",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        result = []
        for i in data['list'][:2]:
            date = i['main']['temp']
            result.append(round(date))
        return result
    except Exception as e:
        print("Exception (forecast):", e)
        pass


def Weather_day():
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast/",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        result1 = []
        for i in data['list'][:9]:
            date = i['dt_txt'][10:16]
            result1.append(date)
        return result1
    except Exception as e:
        print("Exception (forecast):", e)
        pass


def Weather_temp():
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast/",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        result2 = []
        for i in data['list'][:9]:
            date = i['main']['temp']
            result2.append(round(date))
        return result2
    except Exception as e:
        print("Exception (forecast):", e)
        pass

