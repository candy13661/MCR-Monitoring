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
    driver.get("https://www.hotstar.com/my");
    time.sleep(5);

    #-- Click content from Coming Soon rail --
    driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[2]/div/div/div/div/div/div/div/article/a/div[4]").click();
    time.sleep(5);
    #-- Detect player object --
    find_status = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div/div[1]/div[8]/div/div[2]/div/div").is_enabled(); 
    #-- Call alert function
    if find_status == True:
        #-- Playback Success
        print("Playback success")
    else:
        #-- Playback fail
        callAPI("Disney Hotstar content playback is failed","Please check Disney Hotstar site")
        print("Playback Fail")

    time.sleep(5);
    print(find_status);
    print(driver.title);
    driver.quit();

#-- Call function --
try:
    main_function();
except:
    callAPI("Disney Hotstar site is unreachable","Please check service monitoring application or Disney Hotstar site")
    print("Disney Hotstar down");

