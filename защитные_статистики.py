
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchWindowException
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
browser.get("https://fbref.com/en/comps/Big5/2023-2024/defense/players/2023-2024-Big-5-European-Leagues-Stats")
time.sleep(10)
name_list=[]
Tkl=[]
TklW=[]
Att=[]
Lost=[]
Sh=[]
Pass=[]
Int=[]
Clr=[]
Err=[]
Matches=[]
for i in range(1, 2850):
    if i %26 == 0 :
        continue
    xpath_name = f'/html/body/div[4]/div[6]/div[3]/div[2]/table/tbody/tr[{i}]/td[1]/a'
    xpath_tackles=f"/html/body/div[4]/div[6]/div[3]/div[2]/table/tbody/tr[{i}]/td[9]"
    xpath_tackles_won=f"/html/body/div[4]/div[6]/div[3]/div[2]/table/tbody/tr[{i}]/td[10]"
    xpath_att=f"/html/body/div[4]/div[6]/div[3]/div[2]/table/tbody/tr[{i}]/td[15]"
    xpath_lost=f"/html/body/div[4]/div[6]/div[3]/div[2]/table/tbody/tr[{i}]/td[17]"
    xpath_blocs_shoots=f"/html/body/div[4]/div[6]/div[3]/div[2]/table/tbody/tr[{i}]/td[19]"
    xpath_blocs_passes=f"/html/body/div[4]/div[6]/div[3]/div[2]/table/tbody/tr[{i}]/td[20]"
    xpath_intercaptions=f"/html/body/div[4]/div[6]/div[3]/div[2]/table/tbody/tr[{i}]/td[21]"
    xpath_clearense=f"/html/body/div[4]/div[6]/div[3]/div[2]/table/tbody/tr[{i}]/td[23]"
    xpath_errors=f"/html/body/div[4]/div[6]/div[3]/div[2]/table/tbody/tr[{i}]/td[24]"
    xpath_matches=f"/html/body/div[4]/div[6]/div[3]/div[2]/table/tbody/tr[{i}]/td[8]"



    name = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, xpath_name))).text
    tackles=WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH,xpath_tackles ))).text
    tackles_won=WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH,xpath_tackles_won ))).text
    tackles_att=WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH,xpath_att))).text
    tackles_lost=WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH,xpath_lost))).text
    shoots_blocs=WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH,xpath_blocs_shoots))).text
    passes_blocs = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, xpath_blocs_passes))).text
    intercaprion = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, xpath_intercaptions))).text
    clearance = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, xpath_clearense))).text
    errrors = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, xpath_errors))).text
    matches_played=WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, xpath_matches))).text


    name_list.append(name)
    Tkl.append(tackles)
    TklW.append(tackles_won)
    Att.append(tackles_att)
    Lost.append(tackles_lost)
    Err.append(errrors)
    Clr.append(clearance)
    Int.append(intercaprion)
    Pass.append(passes_blocs)
    Sh.append(shoots_blocs)
    Matches.append(matches_played)



data_frame=pd.DataFrame({
    'Фамилия Имя':name_list,
    "Попытки отбора":Tkl,
    "успешные попытки отбора":TklW,
    "количество остановок дриблинга+неудачных попыток остановаить дриблинг":Att,
    "неудачные попытки остновки дриблинга":Lost,
    "Ошибки преведщие к ударам по воротам ":Err,
    "Выносы из штрафной":Clr,
    "Прерванные пасы":Pass,
    "Прерванные удары":Sh,
    "колво матчей (колво сыгранных минут/90)":Matches,
    "Прочитанных передач":Int
})
excel_filename = 'Таблица_с_данными_о_защитных_действиях.xlsx'
data_frame.to_excel(excel_filename, index=False)




