import requests
import random
from bs4 import BeautifulSoup as b

# сайт с анекдотами
URL = 'https://www.anekdot.ru/release/anekdot/day/'


# функция для парсинга анекдотов в виде списка
def parser(url):
    r = requests.get(url)  # далем запрос к сайту
    soup = b(r.text, 'html.parser')  # собираем все данные с сайта в виде текста
    for br in soup('br'):  # находим в супе все элементы br, которые означают перенос строки
        br.replace_with('\n')  # заменяем их на стандартный перенос строки в питоне
    anekdots = soup.find_all('div', class_='text')  # обращаемся по классу текст, так как там лежат все анекдоты
    clear_anekdots = []  # заводим отдельный список с анекдотами без лишних элементами супа
    for anekdot in anekdots:
        clear_anekdots.append(anekdot.get_text())  # из списка супа забираем только текст, отсекая все html-элементы
    return clear_anekdots


anekdots_A = parser(URL)
random.shuffle(anekdots_A)
print(f'Анекдоты категории А собраны. Было собрано:{len(anekdots_A)}')



