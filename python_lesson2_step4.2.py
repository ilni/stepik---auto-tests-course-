from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

 


    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

 
   
    button = browser.find_element_by_id("book")
    button.click()
    
    browser.execute_script("window.scrollBy(0, 100);")
    # Ваш код, который заполняет обязательные поля
    
 
    
    x_element = browser.find_element_by_id ("input_value")
    x = x_element.text
    y = calc(x)
    
    button1 = browser.find_element_by_id("answer")
    button1.send_keys(y)
    
    button2 = browser.find_element_by_id("solve")
    button2.click()
    

  

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()