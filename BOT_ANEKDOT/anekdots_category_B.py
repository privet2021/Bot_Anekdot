import requests
import random
from bs4 import BeautifulSoup as b

URL = 'https://baneks.ru/{}'


# функция для парсинга анекдотов в виде списка
def parser(url):
    anekdots_b = []
    for i in range(50):
        r = requests.get(url.format(random.randint(1,999)))  # далем запрос к сайту
        soup = b(r.text, 'html.parser')# собираем все данные с сайта в виде текста'
        anekdot = soup.find('p')  # обращаемся по классу текст, так как там лежат все анекдоты
        anekdot = anekdot.get_text()
        anekdots_b.append(anekdot)
    return anekdots_b


anekdots_B = parser(URL)
random.shuffle(anekdots_B)
print(f'Анекдоты категории Б собраны. Было собрано: {len(anekdots_B)}')

