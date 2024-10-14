import requests


def get_money_euro():
    url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
    response = requests.get(url).json()
    key = "EUR"
    for i in response:
        if key in i['Cur_Abbreviation']:
            # result.append(i['Cur_OfficialRate'])
            return i['Cur_OfficialRate']


def get_money_usd():
    url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
    response = requests.get(url).json()
    key = "USD"
    for i in response:
        if key in i['Cur_Abbreviation']:
            return i['Cur_OfficialRate']


def get_money_rus():
    url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
    response = requests.get(url).json()
    key = "RUB"
    for i in response:
        if key in i['Cur_Abbreviation']:
            return '{}'.format(i['Cur_OfficialRate'])


def get_money_aud():
    url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
    response = requests.get(url).json()
    key = "AUD"
    for i in response:
        if key in i['Cur_Abbreviation']:
            return '{}'.format(i['Cur_OfficialRate'])


def get_money_bgn():
    url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
    response = requests.get(url).json()
    key = "BGN"
    for i in response:
        if key in i['Cur_Abbreviation']:
            return '{}'.format(i['Cur_OfficialRate'])


def get_money_uah():
    url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
    response = requests.get(url).json()
    key = "UAH"
    for i in response:
        if key in i['Cur_Abbreviation']:
            return '{}'.format(i['Cur_OfficialRate'])


def get_money_dkk():
    url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
    response = requests.get(url).json()
    key = "DKK"
    for i in response:
        if key in i['Cur_Abbreviation']:
            return '{}'.format(i['Cur_OfficialRate'])


def get_money_pln():
    url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
    response = requests.get(url).json()
    key = "PLN"
    for i in response:
        if key in i['Cur_Abbreviation']:
            return '{}'.format(i['Cur_OfficialRate'])


def get_money_irr():
    url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
    response = requests.get(url).json()
    key = "IRR"
    for i in response:
        if key in i['Cur_Abbreviation']:
            return '{}'.format(i['Cur_OfficialRate'])


def get_money_isk():
    url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
    response = requests.get(url).json()
    key = "ISK"
    for i in response:
        if key in i['Cur_Abbreviation']:
            return '{}'.format(i['Cur_OfficialRate'])