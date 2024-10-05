from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar o navegador Edge com o WebDriver
driver = webdriver.Edge()  # Não é necessário fornecer o caminho se o WebDriver estiver no PATH

# 1. Acessar o Google
driver.get("https://www.google.com")

# 2. Buscar por "ge.globo"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("ge.globo")
search_box.send_keys(Keys.RETURN)

# 3. Aguardar e clicar no primeiro resultado que leva ao ge.globo
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//h3)[1]'))
).click()

# 4. Aguardar o carregamento da página do ge.globo
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'body'))
)

# 5. Clicar na primeira notícia
first_news = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//a[contains(@class, "feed-post-link")])[1]'))
)
first_news.click()

# Aguardar a página da notícia ser carregada
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'body'))
)

# Fechar o navegador (opcional)
driver.quit()

