import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import chromedriver_binary
import schedule
from time import sleep

from selenium.webdriver.chrome.service import Service

num = 0  # カウンタ数


def start_chrome():

    # Chrome起動
    service = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()  # 画面サイズ最大化

    # GoogleログインURL
    args = sys.argv
    url='URLを入れてください'+args[1]
    print(url)

    return driver,args[1]


def login_google(driver,n):

    # ログイン情報
    with open("database.txt", "r", encoding="utf-8") as file:
        for line in file:
            if n in line:
                mylist = line.split(",") # lineをカンマで分割
                login_id = mylist[1]
                login_pw = mylist[2]
            
    # 最大待機時間（秒）
    wait_time = 30

    # IDを入力
    login_id_xpath = '//*[@id="identifierNext"]'
    # xpathの要素が見つかるまで待機。
    WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.XPATH, login_id_xpath)))
    driver.find_element(By.NAME, "identifier").send_keys(login_id)
    driver.find_element(By.XPATH, login_id_xpath).click()

    # パスワードを入力
    login_pw_xpath = '//*[@id="passwordNext"]'
    # xpathの要素が見つかるまで待機。
    WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.XPATH, login_pw_xpath)))
    time.sleep(1)
    driver.find_element(By.NAME, "password").send_keys(login_pw)
    time.sleep(1)  # クリックされずに処理が終わるのを防ぐために追加。
    driver.find_element(By.XPATH, login_pw_xpath).click()

    # xpathの要素が見つかるまで待機。
    WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="check_table"]')),
    message="ページが読み込まれませんでした。")

    # チェックボタン入力
    check_box_1 = driver.find_element(
        By.XPATH, '//*[@id="check_table"]/tbody/tr[3]/th/span/input')
    check_box_1.click()
    check_box_2 = driver.find_element(
        By.XPATH, '//*[@id="check_table"]/tbody/tr[17]/th/span/input')
    check_box_2.click()
    check_box_3 = driver.find_element(
        By.XPATH, '//*[@id="check_table"]/tbody/tr[28]/th/span/input')
    check_box_3.click()
    check_box_4 = driver.find_element(
        By.XPATH, '//*[@id="check_table"]/tbody/tr[41]/th/span/input')
    check_box_4.click()
    check_box_5 = driver.find_element(
        By.XPATH, '//*[@id="check_table"]/tbody/tr[45]/th/span/input')
    check_box_5.click()
    check_box_6 = driver.find_element(
        By.XPATH, '//*[@id="check_table"]/tbody/tr[65]/th/span/input')
    check_box_6.click()
    check_box_7 = driver.find_element(By.XPATH, '//*[@id="postbtn"]')
    check_box_7.click()
    time.sleep(1)  # クリックされずに処理が終わるのを防ぐために追加。




def clicK_disinfection():
    # Chromeを起動
    driver, n = start_chrome()

    # Googleにログイン
    login_google(driver, n)

    # ブラウザー閉じる
    driver.quit()





clicK_disinfection()
   # トリガー設定する
   # スケジュール登録
schedule.every(5).seconds.do(clicK_disinfection)

   # イベント実行
while True:

    schedule.run_pending()
    time.sleep(3600)
    num = num+1
    print(num)
    if num > 17:  # 繰り返したい数N-1の値を代入する
        sys.exit()
