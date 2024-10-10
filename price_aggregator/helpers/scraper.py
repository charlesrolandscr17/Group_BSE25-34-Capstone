import traceback
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, requests, selenium
from bs4 import BeautifulSoup
import os

from selenium.webdriver.common.action_chains import ActionChains

print("Starting...")

os.environ["MOZ_HEADLESS"] = "1"

driver = webdriver.Firefox()


def amazon_list(search):
    driver.get("https://www.amazon.com/")

    # search_bar = driver.find_element(By.ID, "twotabsearchtextbox")

    try:
        search_bar = driver.find_element(By.ID, "twotabsearchtextbox")

    except:
        search_bar = driver.find_element(By.ID, "nav-bb-search")

    search_bar.send_keys(search)

    search_bar.send_keys(Keys.ENTER)

    time.sleep(3)

    results = driver.find_elements(By.CLASS_NAME, "s-result-item")

    data = check_all_results(results, search_term=search)

    print(data)
    print(len(data))



def check_all_results(web_elements, search_term):
    print("start")
    data = []

    for web_element in web_elements:
        try:
            image_element = web_element.find_element(By.CLASS_NAME, "s-image")
            image_link = image_element.get_attribute("src")
            price = web_element.find_element(By.CLASS_NAME, "a-price-whole")
        except :
            print("error")
            # traceback.print_exc()
            continue

        el = web_element.find_element(
            By.TAG_NAME,
            "a",
        )

        link = el.get_attribute("href")

        response = requests.get(link)

        soup = BeautifulSoup(response.text, 'html.parser')

        try:

            title = soup.find("span", id = "productTitle").getText()

        except AttributeError:
            print("Title not found")
            continue

        # if search_term.lower() in title.lower():
        #     print("found product")
            

        links_dict = {"image": image_link, "link": link, "price": price.text, "title": title}

        data.append(links_dict)
        
        
    data.pop(0)
    return data
        
    


amazon_list("Samsung galaxy S23 phone")
