
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
browser.get("https://fbref.com/en/comps/Big5/2023-2024/stats/players/2023-2024-Big-5-European-Leagues-Stats")
time.sleep(10)

# Списки для сбора данных
goals_list=[]
assist_list=[]
non_penalty_goals_list=[]
yelow_cards_list=[]
red_cards_list=[]
penalty_made_list=[]
exp_goals_list=[]
exp_ass_list=[]
prog_car_list=[]
prog_pas_list=[]
prog_pas_done_list=[]
name_list=[]



for i in range(1, 2580):
        if i % 26 ==0:
            continue
        xpath_goals=f"/html/body/div[4]/div[6]/div[3]/div[3]/table/tbody/tr[1]/td[12]"
        xpath_ass=f"/html/body/div[4]/div[6]/div[3]/div[3]/table/tbody/tr[{i}]/td[13]"
        xpath_non_penalty=f"/html/body/div[4]/div[6]/div[3]/div[3]/table/tbody/tr[{i}]/td[15]"
        xpath_yelow_cards=f"/html/body/div[4]/div[6]/div[3]/div[3]/table/tbody/tr[{i}]/td[18]"
        xpath_red_cards=f"/html/body/div[4]/div[6]/div[3]/div[3]/table/tbody/tr[{i}]/td[19]"
        xpath_exp_goals=f"/html/body/div[4]/div[6]/div[3]/div[3]/table/tbody/tr[{i}]/td[20]"
        xpath_exp_ass=f"/html/body/div[4]/div[6]/div[3]/div[3]/table/tbody/tr[{i}]/td[22]"
        xpath_prog_car=f"/html/body/div[4]/div[6]/div[3]/div[3]/table/tbody/tr[{i}]/td[24]"
        xpath_prog_pass=f"/html/body/div[4]/div[6]/div[3]/div[3]/table/tbody/tr[{i}]/td[25]"
        xpath_prog_pass_done=f"/html/body/div[4]/div[6]/div[3]/div[3]/table/tbody/tr[{i}]/td[26]"
        xpath_penalty_made=f"/html/body/div[4]/div[6]/div[3]/div[3]/table/tbody/tr[{i}]/td[16]"
        xpath_name=f"/html/body/div[4]/div[6]/div[3]/div[3]/table/tbody/tr[{i}]/td[1]/a"



        goals = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, xpath_goals))).text
        assistance = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH,xpath_ass ))).text
        non_penalty = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH,xpath_non_penalty))).text
        yelow_cards = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, xpath_yelow_cards))).text
        red_cards= WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, xpath_red_cards))).text
        exp_goals = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, xpath_exp_goals))).text
        exp_ass=WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, xpath_exp_ass))).text
        prog_car=WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, xpath_prog_car))).text
        prog_pass = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, xpath_prog_pass))).text
        prog_pass_done = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, xpath_prog_pass_done))).text
        penalty_made = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, xpath_penalty_made))).text
        name=WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, xpath_name))).text


        goals_list.append(goals)
        assist_list.append(assistance)
        non_penalty_goals_list.append(non_penalty)
        yelow_cards_list.append(yelow_cards)
        red_cards_list.append(red_cards)
        penalty_made_list.append(penalty_made)
        exp_goals_list.append(exp_goals)
        exp_ass_list.append(exp_ass)
        prog_car_list.append(prog_car)
        prog_pas_list.append(prog_pass)
        prog_pas_done_list.append(prog_pass_done)
        name_list.append(name)

data_parser = pd.DataFrame({
    "Фамилия Имя": name_list,
    "Голы":goals_list,
    "Ассисты":assist_list,
    "Голы с игры":non_penalty_goals_list,
    "Желтые карточки":yelow_cards_list,
    "красные карточки":red_cards_list,
    "заработанные пенальти":penalty_made_list,
    "Ожидаемые голы":exp_goals_list,
    "Ожидаемые ассисты":exp_ass_list,
    "Прогрессивные переводы ":prog_car_list,
    "Прогрессивные пасы":prog_pas_list,
    "Прогрессивные успешные пасы":prog_pas_done_list
})
excel_filename = 'Таблица_с_данными_о_действиях.xlsx'
data_parser.to_excel(excel_filename, index=False)



