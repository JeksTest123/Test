import pandas as pd
import sqlite3 as sqlt
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# Для отображения всех записей в Dataframe:
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Скачивание данных

# Подключаем webdriver Chrome
# Предварительно необходимо скачать сhromedriver с https://chromedriver.chromium.org/downloads
# и положить в необходимый каталог, указав его путь в переменной driver.
driver = webdriver.Chrome('/bin/chromedriver')

# Осуществляем переход по ссылке для скачивания данных с Мангистауской области
driver.get('http://mng.kgd.gov.kz')
trigger = driver.find_element_by_xpath('//a[@href="/ru/depsection/yuridicheskim-licam"]')
trigger.click()
trigger1 = driver.find_element_by_xpath('//a[@href="/ru/depsection/reabilitaciya-i-bankrotstvo"]')
trigger1.click()
trigger2 = driver.find_element_by_xpath('//a[@href="/ru/depsection/2018-god"]')
trigger2.click()
driver.maximize_window()
driver.execute_script("window.scrollTo(703, 38)")
trigger3 = driver.find_element_by_id('node-23124')
trigger3.click()
trigger4 = driver.find_element_by_xpath('//header[//h3[@class="title"]]').find_element_by_xpath('//a[@href="/ru/content/informacionnye-soobshcheniya-14-2"]')
trigger4.click()
trigger5 = driver.find_element_by_xpath('//a[@href="http://mng.kgd.gov.kz/sites/default/files/u63182/4_2018_vozbuzhdenii_dela_o_bankrotstve_i_poryadke_zayavleniya_trebovaniy_kreditorami_vremennomu_upravlyayushchemu_5.xlsx"]')
trigger5.click()
# Путь сохранения xlsx файла идет по умолчанию с настройками браузера

# Функция для осуществления перехода по ссылке для скачивания данных
# Загруженные excel-файлы лежат в каталоге "Загрузки" по умолчанию с настройками браузера Chrome
# При считывании excel-файлов pandas'ом нужно будет указать путь хранения excel-файлов через переменную path.
def driver_get(url, first_href, second_href, third_href, fourth_href, fifth_href):
    driver.get('{}'.format(url))
    trigger1 = driver.find_element_by_xpath('//a[@href="{}"]'.format(first_href))
    trigger1.click()
    trigger2 = driver.find_element_by_xpath('//a[@href="{}"]'.format(second_href))
    trigger2.click()
    trigger3 = driver.find_element_by_xpath('//a[@href="{}"]'.format(third_href))
    trigger3.click()
    driver.implicitly_wait(1000)
    trigger4 = driver.find_element_by_xpath('//a[@href="{}"]'.format(fourth_href))
    trigger4.click()
    driver.implicitly_wait(1000)
    trigger5 = driver.find_element_by_xpath('//a[@href="{}"]'.format(fifth_href))
    trigger5.click()

# Вызываем функцию для скачивания данных с Нур-Султана
driver_get('http://nursultan.kgd.gov.kz/ru', '/ru/depsection/yuridicheskim-licam', \
           '/ru/depsection/reabilitaciya-i-bankrotstvo', '/ru/depsection/2018-god', \
          '/ru/content/informacionnoe-soobshchenie-2', \
           'http://astana.kgd.gov.kz/sites/default/files/u1323/kopiya_kopiya_4_rus_263_67_58.xlsx')

# Вызываем функцию для скачивания данных с Алматы
driver_get('http://almaty.kgd.gov.kz/', '/ru/depsection/yuridicheskim-licam', \
           '/ru/depsection/reabilitaciya-i-bankrotstvo', '/ru/depsection/2018-god', \
          '/ru/content/informacionnye-soobshcheniya-3-2', \
           'http://almaty.kgd.gov.kz/sites/default/files/u1353/o_vozbuzhdenii_rus_29.12.2018_ispr.xlsx')

# Вызываем функцию для скачивания данных с Шымкента
driver_get('http://shymkent.kgd.gov.kz', '/ru/depsection/yuridicheskim-licam', \
           '/ru/depsection/reabilitaciya-i-bankrotstvo', '/ru/depsection/2018-god', \
          '/ru/content/informacionnye-soobshcheniya-18', \
           'http://shymkent.kgd.gov.kz/sites/default/files/obyavleniya_o_vozbuzhdenii_dela_o_bankrotstve_i_poryadke_zayavleniya_trebovaniy_kreditorami_vremennomu_upravlyayushchemu_03.01.2019.xlsx')

# Вызываем функцию для скачивания данных с Акмолинской области
driver_get('http://akm.kgd.gov.kz', '/ru/depsection/yuridicheskim-licam', \
           '/ru/depsection/reabilitaciya-i-bankrotstvo', '/ru/depsection/2018-god', \
          '/ru/content/informacionnye-soobshcheniya-4-2', \
           'http://akm.kgd.gov.kz/sites/default/files/u1354/obyavlenie_o_vozbuzhdenii_dela_o_bankrotstve_i_poyadka_zayavlennyh_trebovaniy_kreditorov_vremennomu_upravlyayushchemu_117.xlsx')

# Вызываем функцию для скачивания данных с Актюбинской области
driver_get('http://akb.kgd.gov.kz', '/ru/depsection/yuridicheskim-licam', \
           '/ru/depsection/reabilitaciya-i-bankrotstvo', '/ru/depsection/2018-god', \
          '/ru/content/informacionnye-soobshcheniya-5-1', \
           'http://akb.kgd.gov.kz/sites/default/files/u63278/is_o_vozbuzh_bankr_rus_8.xlsx')

# Вызываем функцию для скачивания данных с Алматинской области
driver_get('http://alm.kgd.gov.kz', '/ru/depsection/yuridicheskim-licam', \
           '/ru/depsection/reabilitaciya-i-bankrotstvo', '/ru/depsection/2018-god', \
          '/ru/content/informacionnye-soobshcheniya-6-2', \
           'http://alm.kgd.gov.kz/sites/default/files/u1356/4_vozb._dela_o_bankr_rus_360_67.xlsx')

# Вызываем функцию для скачивания данных с Атырауской области
driver_get('http://atr.kgd.gov.kz', '/ru/depsection/yuridicheskim-licam', \
           '/ru/depsection/reabilitaciya-i-bankrotstvo', '/ru/depsection/2018-god', \
          '/ru/content/informacionnye-soobshcheniya-7-2', \
           'http://atr.kgd.gov.kz/sites/default/files/u1357/obyavleniya_o_vozbuzhdenii_dela_o_bankrotstve_i_poryadke_zayavleniya_trebovaniy_kreditorami_vremennomu_upravlyayushchemu_244.xlsx')

# Вызываем функцию для скачивания данных с ВКО
driver_get('http://vko.kgd.gov.kz', '/ru/depsection/yuridicheskim-licam', \
           '/ru/depsection/reabilitaciya-i-bankrotstvo', '/ru/depsection/2018-god', \
          '/ru/content/informacionnye-soobshcheniya-1-4', \
           'http://vko.kgd.gov.kz/sites/default/files/u1358/o_vozbuzhd.rus_29.12.18.xlsx')

# Вызываем функцию для скачивания данных с Жамбыльской области
driver_get('http://zhmb.kgd.gov.kz/', '/ru/depsection/yuridicheskim-licam', \
           '/ru/depsection/reabilitaciya-i-bankrotstvo', '/ru/depsection/2018-god', \
          '/ru/content/informacionnye-soobshcheniya-9-1', \
           'http://zhmb.kgd.gov.kz/sites/default/files/u1359/rus_16_0.xls')

# Вызываем функцию для скачивания данных с ЗКО
driver_get('http://zko.kgd.gov.kz', '/ru/depsection/yuridicheskim-licam', \
           '/ru/depsection/reabilitaciya-i-bankrotstvo', '/ru/depsection/2018-god', \
          '/ru/content/informacionnye-soobshcheniya-10-0', \
           'http://zko.kgd.gov.kz/sites/default/files/u1360/o_vozbuzhdenii_dela_o_bankrotstve_rus_2018_13.xlsx')

# Осуществляем переход по ссылке для скачивания данных с Карагандинской области
driver.get('http://krg.kgd.gov.kz')
trigger = driver.find_element_by_xpath('//a[@href="/ru/depsection/yuridicheskim-licam"]')
trigger.click()
trigger1 = driver.find_element_by_xpath('//a[@href="/ru/depsection/reabilitaciya-i-bankrotstvo"]')
trigger1.click()
trigger2 = driver.find_element_by_xpath('//a[@href="/ru/depsection/2018-god"]')
trigger2.click()
driver.implicitly_wait(1000)
trigger3 = driver.find_element_by_id('node-23105')
trigger3.click()
driver.implicitly_wait(1000)
trigger4 = driver.find_element_by_xpath('//a[@href="/ru/content/informacionnye-soobshcheniya-11-4"]')
trigger4.click()
trigger5 = driver.find_element_by_xpath('//a[@href="http://krg.kgd.gov.kz/sites/default/files/u1361/russ_74.xls"]')
trigger5.click()
# Путь сохранения xlsx файла идет по умолчанию с настройками браузера

# Вызываем функцию для скачивания данных с Костанайской области
driver_get('http://kst.kgd.gov.kz', '/ru/depsection/yuridicheskim-licam', \
           '/ru/depsection/reabilitaciya-i-bankrotstvo', '/ru/depsection/2018-god', \
          '/ru/content/informacionnye-soobshcheniya-12-2', \
           'http://kst.kgd.gov.kz/sites/default/files/prilozhenie_4_rus_149_3.xls')

# Вызываем функцию для скачивания данных с Кызылординской области
driver_get('http://kzl.kgd.gov.kz', '/ru/depsection/yuridicheskim-licam', \
           '/ru/depsection/reabilitaciya-i-bankrotstvo', '/ru/depsection/2018-god', \
          '/ru/content/informacionnye-soobshcheniya-13-2', \
           'http://kzl.kgd.gov.kz/sites/default/files/u1363/kopiya_obyav.vozb.bank.rus1_0_0.xlsx')

# Вызываем функцию для скачивания данных с Павладорской области
driver_get('http://pvl.kgd.gov.kz/ru', '/ru/depsection/yuridicheskim-licam', \
           '/ru/depsection/reabilitaciya-i-bankrotstvo', '/ru/depsection/2018-god', \
          '/ru/content/informacionnye-soobshcheniya-15-1', \
           'http://pvl.kgd.gov.kz/sites/default/files/u1365/o_vozb_dela_o_bankr_i_por_zayav_treb_kred_vrem_79.xlsx')

# Вызываем функцию для скачивания данных с СКО
driver_get('http://sko.kgd.gov.kz', '/ru/depsection/yuridicheskim-licam', \
           '/ru/depsection/reabilitaciya-i-bankrotstvo', '/ru/depsection/2018-god', \
          '/ru/content/informacionnye-soobshcheniya-16-1', \
           'http://sko.kgd.gov.kz/sites/default/files/u1366/o_vozbuzhdenii_149_0.xls')

# Вызываем функцию для скачивания данных с Туркестанской области
driver_get('http://trk.kgd.gov.kz', '/ru/depsection/yuridicheskim-licam', \
           '/ru/depsection/reabilitaciya-i-bankrotstvo', '/ru/depsection/2018-god', \
          '/ru/content/informacionnye-soobshcheniya-17-2', \
           'http://trk.kgd.gov.kz/sites/default/files/u6814/kazobyavleniya_o_vozbuzhdenii_dela_o_bankrotstve_i_poryadke_zayavleniya_trebovaniy_kreditorami_vremennomu_upravlyayushchemu.xlsx')

# Входные данные

# Считываем все ексел файлы и чистим от ненужных нам колонок и пустых строк
# Загруженные excel-файлы лежат в каталоге "Загрузки" по умолчанию с настройками браузера Chrome
# При считывании excel-файлов pandas'ом нужно будет указать путь хранения excel-файлов через переменную path.

path = '/home/pc-user/Загрузки/'

data_alm_obl_2018 = pd.read_excel(path + '4_vozb._dela_o_bankr_rus_360_67.xlsx', sheet_name='рус', header=5, dtype=str)
data_alm_obl_2018.drop(data_alm_obl_2018.columns[[14, 15]], axis = 1, inplace = True)

data_akt_olb_2018 = pd.read_excel(path + 'is_o_vozbuzh_bankr_rus_8.xlsx', sheet_name='рус', header=9, dtype=str)

data_mng_obl_2018 = pd.read_excel(path + '4_2018_vozbuzhdenii_dela_o_bankrotstve_i_poryadke_zayavleniya_trebovaniy_kreditorami_vremennomu_upravlyayushchemu_5.xlsx', \
                                  sheet_name='Лист1', header=5, dtype=str)

data_turk_obl_2018 = pd.read_excel(path + 'kazobyavleniya_o_vozbuzhdenii_dela_o_bankrotstve_i_poryadke_zayavleniya_trebovaniy_kreditorami_vremennomu_upravlyayushchemu.xlsx', \
                    sheet_name='рус', header=4, dtype=str)

data_ast_2018 = pd.read_excel(path + 'kopiya_kopiya_4_rus_263_67_58.xlsx', sheet_name='Лист1', header=4, dtype=str)

data_kzl_obl_2018 = pd.read_excel(path + 'kopiya_obyav.vozb.bank.rus1_0_0.xlsx', sheet_name='Лист2', header=5, dtype=str)

data_akm_obl_2018 = pd.read_excel(path + 'obyavlenie_o_vozbuzhdenii_dela_o_bankrotstve_i_poyadka_zayavlennyh_trebovaniy_kreditorov_vremennomu_upravlyayushchemu_117.xlsx', \
                                 sheet_name='рус.', header=6, dtype=str)

data_shmk_2018 = pd.read_excel(path + 'obyavleniya_o_vozbuzhdenii_dela_o_bankrotstve_i_poryadke_zayavleniya_trebovaniy_kreditorami_vremennomu_upravlyayushchemu_03.01.2019.xlsx', \
                              sheet_name='рус', header=4, dtype=str)
data_shmk_2018.drop(data_shmk_2018.columns[[14,15,16]], axis=1, inplace=True)

data_atr_obl_2018 = pd.read_excel(path + 'obyavleniya_o_vozbuzhdenii_dela_o_bankrotstve_i_poryadke_zayavleniya_trebovaniy_kreditorami_vremennomu_upravlyayushchemu_244.xlsx', \
                     sheet_name='Лист1', header=3, dtype=str)

data_pvl_obl_2018 = pd.read_excel(path + 'o_vozb_dela_o_bankr_i_por_zayav_treb_kred_vrem_79.xlsx', \
                                  sheet_name='объявление о банкротстве', header=5, dtype=str)

data_vko_2018 = pd.read_excel(path + 'o_vozbuzhd.rus_29.12.18.xlsx', sheet_name='Рус.яз.', header=4, dtype=str)
data_vko_2018.drop(data_vko_2018.columns[[1]], axis=1, inplace=True)

data_sko_2018 = pd.read_excel(path + 'o_vozbuzhdenii_149_0.xls', sheet_name='Лист1', header=6, dtype=str)

data_zko_2018 = pd.read_excel(path + 'o_vozbuzhdenii_dela_o_bankrotstve_rus_2018_13.xlsx', \
                              sheet_name='о возб дела о банкр и предяв ВУ', header=9, dtype=str)

data_alm_2018 = pd.read_excel(path + 'o_vozbuzhdenii_rus_29.12.2018_ispr.xlsx', sheet_name='Лист1', header=3, dtype=str)

data_kst_obl_2018 = pd.read_excel(path + 'prilozhenie_4_rus_149_3.xls', sheet_name='рус', header=5, dtype=str)

data_zhmbl_obl_2018 = pd.read_excel(path + 'rus_16_0.xls', sheet_name='Лист1', header=5, dtype=str)

data_krgn_obl_2018 = pd.read_excel(path + 'russ_74.xls', sheet_name='о возб дела о банкр и предяв ВУ', header=8, dtype=str)

# Задаем наименование колонок всем Dataframe

lst = [data_alm_obl_2018, data_akt_olb_2018, data_mng_obl_2018, data_turk_obl_2018, \
      data_ast_2018, data_kzl_obl_2018, data_akm_obl_2018, data_shmk_2018, \
      data_atr_obl_2018, data_pvl_obl_2018, data_vko_2018, data_sko_2018, \
      data_zko_2018, data_alm_2018, data_kst_obl_2018, data_zhmbl_obl_2018, \
      data_krgn_obl_2018]

col = ['№ п/п', 'БИН/ИИН должника', 'Наименование /Ф.И.О.должника', 'Номер государственной регистрации должника', \
       'Адрес местонахождения должника', 'Наименование суда', \
       'Дата вынесения определения о возбуждении дела о банкротстве', 'Дата назначения временного управляющего', \
       'Ф.И.О. Временного управляющего', 'Начальный срок принятия требований кредиторов временным управляющим', \
       'Конечный срок принятия требований кредиторов временным управляющим', 'Адрес приема требований', \
       'Контактные данные (телефон, электронный адрес) временного управляющего', \
       'Дата размещения объявления']

for i in lst:
    i.columns = col

# Объединяем все Dataframe в один и устанавливаем индекс
data = pd.concat(lst)
emp_lst = []
for i in range(1, len(data['№ п/п'])+1):
    emp_lst.append(i)
data['№ п/п'] = emp_lst
data.set_index('№ п/п', inplace=True)
# data

# Устанавливаем соединение с БД sqlite3
con = sqlt.connect("test_db.db")

# Осуществляем запись Dataframe в БД sqlite3
data.to_sql("defaulter", con=con, if_exists="replace", index=True)

# Проверяем успешность записи с БД sqlite3 сделав запрос
sql_data = pd.read_sql_query('SELECT * FROM defaulter;', con=con)
# sql_data

# В терминале ОС Linux прописываем команду на создание БД и в ее терминале создаем БД.
# sqlite3 test_db.db
# .database
# .quit

