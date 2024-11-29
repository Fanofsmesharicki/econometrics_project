
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchWindowException

# Настройки браузера для загрузки страницы
option = webdriver.FirefoxOptions()
option.set_preference("dom.webdriver.enabled", False)
option.set_preference("media.volume_scale", "0.0")
option.set_preference("general.useragent.override", "Robert bobert")
option.set_preference("profile.default_content_setting_values.notifications", 2)
option.set_preference("profile.managed_default_content_settings.images", 2)
option.set_preference("permissions.default.image", 2)
option.set_preference("dom.webnotifications.enabled", False)
pd.set_option('display.max_columns', None)

browser = webdriver.Firefox(options=option)
browser.get("https://www.transfermarkt.world/spieler-statistik/wertvollstespieler/marktwertetop")
time.sleep(10)

# Списки для сбора данных
age_list = []
nation_list = []
position_list = []
name_list = []
club_list = []
cost_list = []
liga_list = []
clubs_APl = [
    'Арсенал', 'Астон Вилла', 'Бирмингем Сити', 'Блэкберн Роверс',
    'Болтон Уондерерс', 'Борнмут', 'Брайтон энд Хоув Альбион', 'Бернли', 'Челси',
    'Кристал Пэлас', 'Эвертон', 'Фулхэм', 'Халл Сити', 'Лидс Юнайтед', 'Лестер Сити',
    'Ливерпуль', 'Манчестер Сити', 'Манчестер Юнайтед', 'Мидлсбро', 'Ньюкасл Юнайтед',
    'Норвич Сити', 'Квинз Парк Рейнджерс', 'Реддинг', 'Саутгемптон', 'Сток Сити',
    'Сандерленд', 'Суонси Сити', 'Тоттенхэм Хотспур', 'Уиган Атлетик', 'Уотфорд',
    'Уэст Бромвич Альбион', 'Уэст Хэм Юнайтед', 'Уулверхэмптон Уондерерс'
]
clubs_LA_liga = [
    'Алавес', 'Атлетико Мадрид', 'Атлетик Бильбао', 'Барселона', 'Сельта', 'Эйбар',
    'Эльче', 'Хетафе', 'Гранада', 'Осасуна', 'Реал Бетис', 'Реал Вальядолид',
    'Реал Мадрид', 'Реал Сосьедад', 'Валенсия', 'Вильярреал', 'Леванте', 'Мальорка',
    'Райо Вальекано', 'Реал Сарагоса'
]
clubs_bundesliga = [
    "Бавария Мюнхен", "Боруссия Дортмунд", "РБ Лейпциг", "Байер 04 Леверкузен",
    "Унион Берлин", "Фрайбург", "Вольфсбург", "Айнтрахт Франкфурт", "Майнц 05",
    "Боруссия Мёнхенгладбах", "Кёльн", "Хоффенхайм", "Вердер Бремен", "Аугсбург",
    "Штутгарт", "Бохум", "Хайденхайм", "Дармштадт 98"
]
clubs_seria_a = [
    "АС Рома", "Аталанта Бергамо", "Болонья", "Кальяри", "Верона", "Интер Милан",
    "Ювентус", "Лацио", "Милан", "Наполи", "Парма", "Фиорентина", "Дженоа",
    "Сампдория", "Сассуоло", "Торино", "Удинезе", "Верона"
]
clubs_liga_1 = [
    "Пари Сен-Жермен", "Лилль", "Лион", "Монако", "Марсель", "Страсбург", "Нант",
    "Ренн", "Бордо", "Ницца", "Сент-Этьен", "Монпелье", "Анже", "Ланс", "Реймс",
    "Мец", "Брест", "Лорьян", "Ним", "Дижон"
]

for j in range(1, 20):
    for i in range(1, 26):
        xpath_age = f'/html/body/div/main/div[1]/div[1]/div/div[3]/div/table/tbody/tr[{i}]/td[3]'
        xpath_nation = f'/html/body/div/main/div[1]/div[1]/div/div[3]/div/table/tbody/tr[{i}]/td[4]/img[1]'
        xpath_position = f'/html/body/div/main/div[1]/div[1]/div/div[3]/div/table/tbody/tr[{i}]/td[2]/table/tbody/tr[2]/td'
        xpath_name = f'/html/body/div/main/div[1]/div[1]/div/div[3]/div/table/tbody/tr[{i}]/td[2]/table/tbody/tr[1]/td[2]/a'
        xpath_club = f'/html/body/div/main/div[1]/div[1]/div/div[3]/div/table/tbody/tr[{i}]/td[5]/a/img'
        xpath_cost = f'/html/body/div/main/div[1]/div[1]/div/div[3]/div/table/tbody/tr[{i}]/td[6]/a'

        age = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, xpath_age))).text
        nation = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, xpath_nation))).get_attribute("title")
        position = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, xpath_position))).text
        name = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, xpath_name))).get_attribute("title")
        club = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, xpath_club))).get_attribute("title")
        cost = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, xpath_cost))).text[:-6]
        cost = float(cost.replace(",", "."))

        if club in clubs_bundesliga:
            liga_list.append("Бундеслига")
        elif club in clubs_LA_liga:
            liga_list.append("Ла лига")
        elif club in clubs_seria_a:
            liga_list.append("Серия А")
        elif club in clubs_APl:
            liga_list.append("АПЛ")
        elif club in clubs_liga_1:
            liga_list.append("Лига 1")
        else:
            liga_list.append("another league")

        nation_list.append(nation)
        age_list.append(age)
        position_list.append(position)
        name_list.append(name)
        club_list.append(club)
        cost_list.append(cost)

    if j == 1:
        xpath_button = '/html/body/div/main/div[1]/div[1]/div/div[3]/div/div[2]/ul/li[11]/a'
    else:
        xpath_button = '/html/body/div/main/div[1]/div[1]/div/div[3]/div/div[2]/ul/li[13]/a'

    button = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, xpath_button))).click()
    time.sleep(3)

data_parser = pd.DataFrame({
    "Фамилия Имя": name_list,
    "Возраст игрока": age_list,
    "Национальность": nation_list,
    "Позиция на поле": position_list,
    "Лига": liga_list,
    "Клуб": club_list,
    "Стоимость": cost_list

})
excel_filename = 'Таблица_с_данными_о_стоимости.xlsx'
data_parser.to_excel(excel_filename, index=False)





