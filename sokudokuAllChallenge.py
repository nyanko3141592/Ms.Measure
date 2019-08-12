import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import random

def main():
    for i in range(25):
        #chromeを開く
        driver = webdriver.Chrome('./chromedriver')
        driver.get("https://www.sokunousokudoku.net/measuresan/")

        element = driver.find_element_by_css_selector('#select')
        Select(element).select_by_value("5")  # valueの値

        driver.find_element_by_css_selector("#button2").click()
        time.sleep(3)

        time.sleep(0.5)
        driver.find_element_by_css_selector("#done_btn > span").click()

        answer = [random.randint(1, 3) for i in range(3)]
        print(answer)

        for i in range(3):
            driver.find_element_by_css_selector("#q" + str(i+1) + " > ul > li:nth-child(" + str(answer[i]) + ") > p > span").click()
            time.sleep(1)

        driver.find_element_by_css_selector("#question > p").click()
        time.sleep(3)
        print("result page")

        try:
            result = driver.find_element_by_css_selector("#result > div.wrapper > div > div > div.result-hd.class1 > div > div.block > div > div.comment > dl > dd:nth-child(3) > p > em").text
            # print(result)
            correctAnswer = int(result[0])
            print(correctAnswer)
            time.sleep(3)
        except:
            correctAnswer = 0
            print("Error")
            time.sleep(3)

        if correctAnswer == 3:
            print("Perfect!")
            input()
            driver.quit()
            break
        else:
            driver.quit()

if __name__ == "__main__":
    main()

