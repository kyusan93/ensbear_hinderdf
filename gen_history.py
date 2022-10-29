from googlesearch import search
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Jonathan\\AppData\\Local\\Google\\Chrome\\User Data") #Path to your chrome profile
driver = webdriver.Chrome(executable_path="C:\\Tools\\chromedriver.exe",chrome_options=options)

search_terms = []
file1 = open(r'C:\Tools\searches.txt', 'r')
Lines = file1.readlines()

for line in Lines:
    line = line.strip()
    search_terms.append(line)

for term in search_terms:
    url = "https://www.google.com.tr/search?q={}".format(term)
    driver.get(url)
    for term_url in search(term, tld="com", num=1, stop=1, pause=5):
        driver.get(term_url)
driver.quit()
