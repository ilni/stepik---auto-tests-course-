from selenium import webdriver
import time 
import os 



try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
       element.send_keys("answer")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    el=browser.find_element_by_name("file")
    el.send_keys(file_path)
    
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла