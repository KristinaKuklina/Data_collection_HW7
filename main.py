from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from bs4 import BeautifulSoup
import re
import csv

# Функция перехода на новую страницу с ожиданием загрузки
def loading_new_page(buttom):
    old_url = driver.current_url
    buttom.click()
    wait = WebDriverWait(driver, timeout=10)
    wait.until(lambda driver: driver.current_url != old_url)

# Добавление опции развертывания браузера во весь экран
options = Options()
options.add_argument('--start-maximized')

# Установка web-драйвера и переход на сайт
driver = webdriver.Chrome(options)
driver.get("https://shop.tastycoffee.ru/?ysclid=lv1fnhl3fe445267367")

# Переход к выпадающему меню "Купить"
wait = WebDriverWait(driver, timeout=10)
menu_buy = wait.until(Ec.element_to_be_clickable((By.XPATH, "/html/body/div[1]/header/div[1]/div/div[8]/div[1]/a")))
menu_buy.click()

# Выбор категории "Кофе"
category_coffee = driver.find_element(By.XPATH, value="/html/body/div[1]/header/div[1]/div/div[8]/div[1]/ul/li[1]/a")
category_coffee.click()

# Выбор параметров кофе
# Переход к меню "степень прожарки"
menu_roasting = driver.find_element(By.XPATH, value="/html/body/div[3]/div[3]/div/div/div/div[1]/form/div[1]/div[2]/div[2]/button/div/div/div")
menu_roasting.click()
# Выбор степени прожарки (средняя)
degree_of_roasting = driver.find_element(By.XPATH, value="/html/body/div[3]/div[3]/div/div/div/div[1]/form/div[1]/div[2]/div[2]/div/div/ul/li[2]/a/span[2]")
degree_of_roasting.click()
menu_roasting.click() # свернуть окно со степенью прожарки

# Выбор помола (в зернах)
grinding = driver.find_element(By.XPATH, '//a[contains(@href, "coffee/v-zernah")]')
loading_new_page(grinding)

# Загрузка всех результатов, отвечающих заданным фильтрам
while True:
    try:
        buttom = driver.find_element(By.XPATH, "//a[@class='loadLink']") # кнопка "загрузить еще"
        loading_new_page(buttom)
    except: break

# Импорт страницы в  BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Поиск всех карточек
regex = re.compile('.*cardBox noteBox-for.*')
cards = soup.find_all("div", {"class": regex})

data =[]

# Парсинг данных с помощью BeautifulSoup
for card in cards:
    name = card.find('div', {"class": "nameTovar"}).find('a').text.strip()
    description = card.find('div', {'class': "textTovar text-hide"}).text.strip()
    price_per_250g = float(card.find('a', {'class': "priceCb"}).text.strip().split()[0])
    try:
        price_per_kg = float(card.find_all('a', {'class': "priceCb"})[1].text.strip().split()[0])
    except:
        price_per_kg = 'отсутствует'
    data.append({
                "Название": name,
                "Описание": description,
                "Цена за 250 г, руб": price_per_250g,
                "Цена за кг, руб": price_per_kg
            })
    
# Запись результатов в файл
with open('tasty_coffee.csv', 'w', newline='', encoding='utf-8') as f:
    dict_writer = csv.DictWriter(f, data[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(data)
