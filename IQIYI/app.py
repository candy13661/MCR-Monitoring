#import selenium;
from selenium.webdriver.chrome.options import Options
import time;
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By
from teamsApi import *
from readSecretFile import *

#PATH = "C:\ChromeDriver\chromedriver.exe";

def main_function():
    chrome_options = Options()
    chrome_options.add_argument(r"--user-data-dir=C:\Netflix\Cookies")
    
    driver = webdriver.Chrome(options=chrome_options);
    driver.maximize_window();
    driver.get("https://tv.iq.com");
    time.sleep(5);

    #-- Click content from Coming Soon rail --
    driver.find_element(By.XPATH, "/html").send_keys(Keys.ARROW_DOWN)
    time.sleep(2);
    driver.find_element(By.XPATH, "/html").send_keys(Keys.ARROW_DOWN)
    time.sleep(2);
    driver.find_element(By.XPATH, "/html").send_keys(Keys.ARROW_DOWN)
    time.sleep(2);
    driver.find_element(By.XPATH, "/html").send_keys(Keys.ARROW_DOWN)
    time.sleep(2);
    driver.find_element(By.XPATH, "/html").send_keys(Keys.ENTER)

    time.sleep(10);
    print(driver.title);
    print('Playback Success')
    driver.quit();
    
main_function();
#-- Call function --
# try:
#     main_function();
# except:
#     #callAPI("Disney Hotstar site is unreachable","Please check service monitoring application or Disney Hotstar site")
#     print("Disney Hotstar down");

