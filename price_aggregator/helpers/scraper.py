from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import os

print("Starting...")

options = Options()
os.environ["MOZ_HEADLESS"] = "1"
geckodriver_binary = "/snap/bin/geckodriver"
service = Service(geckodriver_binary)

driver = webdriver.Firefox(service=service, options=options)


def amazon_list(search):
    driver.get("https://www.amazon.com/")

    # search_bar = driver.find_element(By.ID, "twotabsearchtextbox")

    try:
        search_bar = driver.find_element(By.ID, "twotabsearchtextbox")

    except BaseException:
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
            image_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(web_element.find_element(
                    By.CLASS_NAME, ".s-image")))
            image_link = image_element.get_attribute("src")
            price = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(web_element.find_element(
                    By.CLASS_NAME, ".a-price-whole")))
        except Exception as e:
            print(f"Error retrieving image or price: {e}")
            # traceback.print_exc()
            continue

        el = web_element.find_element(
            By.TAG_NAME,
            "a",
        )

        link = el.get_attribute("href")

        try:
            response = requests.get(link)
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find("span", id="productTitle").getText()

        except AttributeError:
            print("Title not found")
            continue

        except Exception as e:
            print(f"Error fetching product page: {e}")
            continue

        # if search_term.lower() in title.lower():
        #     print("found product")

        links_dict = {"image": image_link,
                      "link": link,
                      "price": price.text,
                      "title": title
                      }

        data.append(links_dict)

    if data:
        data.pop(0)
    else:
        print("Warning: 'data' is empty; nothing to pop.")
    return data


# amazon_list("Samsung galaxy S23 phone")
