from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from data import get_student, get_list, write_output

source_2 = 'http://evaluare.edu.ro/2022/rezultate/B/index.html'

if __name__ == '__main__':
    # deprecated driver = webdriver.Edge(executable_path=r"C:\things\Python\webdrivers\NewEdge\msedgedriver.exe")
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

driver.get(source_2)
time.sleep(3)
element = driver.find_element(By.XPATH, "//*[@id='dynatable-pagination-links-candidate-list']/li[7]/a").get_attribute("data-dynatable-page")
last_page = int(element)
soup = BeautifulSoup(driver.page_source, features='html.parser')
datas = []
page = 1
for i in range(1, last_page+1):
    if i==1:
        write_output(get_list(get_student(soup)))
    else:
        source_1 = f'http://evaluare.edu.ro/2022/rezultate/B/index.html?page={i}&offset=25'
        driver.get(source_1)
        time.sleep(1)
        soup_3 = BeautifulSoup(driver.page_source, features='html.parser')
        write_output(get_list(get_student(soup_3)))

driver.close()
