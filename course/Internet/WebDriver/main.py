from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Driver
path_to_chromedriver = "C:\python_practice\chromedriver-win64\chromedriver.exe"

service = Service(path_to_chromedriver)
driver = webdriver.Chrome(service=service)

driver.get("https://www.example.com")

# Установление значения в LocalStorage
driver.execute_script("localStorage.setItem('key', 'value');")

# Получение значения из LocalStorage
value = driver.execute_script("return localStorage.getItem('key');")
print(value)

# Удаление значения из LocalStorage
driver.execute_script("localStorage.removeItem('key');")

driver.refresh()

# Устанавление значения в Cookie
driver.add_cookie({"name": "key", "value": "myVal"})

# Получение значения из Cookie
cookies = driver.get_cookies()
for cookie in cookies:
    if cookie['name'] == 'key':
        value = cookie['value']
        print(value)

# Удаление Cookie
driver.delete_cookie("key")

driver.quit()