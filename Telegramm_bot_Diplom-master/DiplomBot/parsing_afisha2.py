import requests
from bs4 import BeautifulSoup

url = 'https://afisha.tut.by/film/?crnd=49574'
r = requests.get(url).text
soup = BeautifulSoup(r, "html.parser")
link = soup.find('div', id='events-block')
links = link.find_all('li', class_='lists__li')

spisok_text = []
spisok_img = []
spisok_link = []


############## парсим первый фильм ################

def main_afisha0():
    for lk in links:
        luk = lk.find('a', class_='name').text
        spisok_text.append(luk)
    return spisok_text[0]


def img0():
    for im in links:
        image = im.find('a', class_='media')
        images = image.find('img').get('src')
        spisok_img.append(images)
    return spisok_img[0]


def link0():
    for ln in links:
        linkus = ln.find('a', class_='media').get('href')
        spisok_link.append(linkus)
    return spisok_link[0]


############## парсим второй фильм ################
def main_afisha1():
    for lk in links:
        luk = lk.find('a', class_='name').text
        spisok_text.append(luk)
    return spisok_text[1]


def img1():
    for im in links:
        image = im.find('a', class_='media')
        images = image.find('img').get('src')
        spisok_img.append(images)
    return spisok_img[1]


def link1():
    for ln in links:
        linkus = ln.find('a', class_='media').get('href')
        spisok_link.append(linkus)
    return spisok_link[1]


############## парсим третий фильм ################
def main_afisha2():
    for lk in links:
        luk = lk.find('a', class_='name').text
        spisok_text.append(luk)
    return spisok_text[2]


def img2():
    for im in links:
        image = im.find('a', class_='media')
        images = image.find('img').get('src')
        spisok_img.append(images)
    return spisok_img[2]


def link2():
    for ln in links:
        linkus = ln.find('a', class_='media').get('href')
        spisok_link.append(linkus)
    return spisok_link[2]


############## парсим четвертый фильм ################
def main_afisha3():
    for lk in links:
        luk = lk.find('a', class_='name').text
        spisok_text.append(luk)
    return spisok_text[3]


def img3():
    for im in links:
        image = im.find('a', class_='media')
        images = image.find('img').get('src')
        spisok_img.append(images)
    return spisok_img[3]


def link3():
    for ln in links:
        linkus = ln.find('a', class_='media').get('href')
        spisok_link.append(linkus)
    return spisok_link[3]


############## парсим пятый фильм ################
def main_afisha4():
    for lk in links:
        luk = lk.find('a', class_='name').text
        spisok_text.append(luk)
    return spisok_text[4]


def img4():
    for im in links:
        image = im.find('a', class_='media')
        images = image.find('img').get('src')
        spisok_img.append(images)
    return spisok_img[4]


def link4():
    for ln in links:
        linkus = ln.find('a', class_='media').get('href')
        spisok_link.append(linkus)
    return spisok_link[4]


############## парсим шестой фильм ################
def main_afisha5():
    for lk in links:
        luk = lk.find('a', class_='name').text
        spisok_text.append(luk)
    return spisok_text[5]


def img5():
    for im in links:
        image = im.find('a', class_='media')
        images = image.find('img').get('src')
        spisok_img.append(images)
    return spisok_img[5]


def link5():
    for ln in links:
        linkus = ln.find('a', class_='media').get('href')
        spisok_link.append(linkus)
    return spisok_link[5]


############## парсим седьмой фильм ################
def main_afisha6():
    for lk in links:
        luk = lk.find('a', class_='name').text
        spisok_text.append(luk)
    return spisok_text[6]


def img6():
    for im in links:
        image = im.find('a', class_='media')
        images = image.find('img').get('src')
        spisok_img.append(images)
    return spisok_img[6]


def link6():
    for ln in links:
        linkus = ln.find('a', class_='media').get('href')
        spisok_link.append(linkus)
    return spisok_link[6]


############## парсим восьмой фильм ################
def main_afisha7():
    for lk in links:
        luk = lk.find('a', class_='name').text
        spisok_text.append(luk)
    return spisok_text[7]


def img7():
    for im in links:
        image = im.find('a', class_='media')
        images = image.find('img').get('src')
        spisok_img.append(images)
    return spisok_img[7]


def link7():
    for ln in links:
        linkus = ln.find('a', class_='media').get('href')
        spisok_link.append(linkus)
    return spisok_link[7]


############## парсим девятый фильм ################
def main_afisha8():
    for lk in links:
        luk = lk.find('a', class_='name').text
        spisok_text.append(luk)
    return spisok_text[8]


def img8():
    for im in links:
        image = im.find('a', class_='media')
        images = image.find('img').get('src')
        spisok_img.append(images)
    return spisok_img[8]


def link8():
    for ln in links:
        linkus = ln.find('a', class_='media').get('href')
        spisok_link.append(linkus)
    return spisok_link[8]


############## парсим десятый фильм ################
def main_afisha9():
    for lk in links:
        luk = lk.find('a', class_='name').text
        spisok_text.append(luk)
    return spisok_text[9]


def img9():
    for im in links:
        image = im.find('a', class_='media')
        images = image.find('img').get('src')
        spisok_img.append(images)
    return spisok_img[9]


def link9():
    for ln in links:
        linkus = ln.find('a', class_='media').get('href')
        spisok_link.append(linkus)
    return spisok_link[9]


############## парсим 11 фильм ################
def main_afisha10():
    for lk in links:
        luk = lk.find('a', class_='name').text
        spisok_text.append(luk)
    return spisok_text[10]


def img10():
    for im in links:
        image = im.find('a', class_='media')
        images = image.find('img').get('src')
        spisok_img.append(images)
    return spisok_img[10]


def link10():
    for ln in links:
        linkus = ln.find('a', class_='media').get('href')
        spisok_link.append(linkus)
    return spisok_link[10]


############## парсим 12 фильм ################
def main_afisha11():
    for lk in links:
        luk = lk.find('a', class_='name').text
        spisok_text.append(luk)
    return spisok_text[11]


def img11():
    for im in links:
        image = im.find('a', class_='media')
        images = image.find('img').get('src')
        spisok_img.append(images)
    return spisok_img[11]


def link11():
    for ln in links:
        linkus = ln.find('a', class_='media').get('href')
        spisok_link.append(linkus)
    return spisok_link[11]


print(spisok_text)