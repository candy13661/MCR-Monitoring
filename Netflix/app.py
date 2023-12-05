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
    driver.get("https://www.netflix.com/my-en/login");
    NetflixCookies = driver.get_cookies();
    time.sleep(5);

    ##-- Logic to check if login attempt required via cookies --##
    for cookieName in NetflixCookies:
        if cookieName["name"] == "NetflixId":
            if len(cookieName["value"]) > 700:
                ##-- login not required / Login cookies available --##
                #print(len(cookieName["value"]))
                print("Login Not required - Cookies Available")

                #-- Play Content --
                try:
                    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/span/div/div/div/div/div/div[2]/div/div/div[3]/a/button").click();
                except:
                    #-- Select Profile --
                    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[2]/div/a/div/div").click();
                    
                #-- Find player element --
                try:
                    find_status = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div").is_enabled(); 
                    print("Content playback success");
                    
                except:
                    callAPI("Netflix Service Down Alert","Netflix Playback Error")
                    print("Content not playable");

                time.sleep(10);
                print(find_status);
                print(driver.title);
                driver.quit();

            else:
                ##-- Login required / Login cookies not available --##
                print("Login Required - Cookies Not Available")

                ##-- Call secret readFile function to retrieve credential from JSON file
                try:
                    netflixSecret = secret("Netflix")
                except:
                    callAPI("Error reading JSON file","Please ensure file is exist and format is intact")
                    print("Error reading JSON file - Please ensure file is exist and format is intact")
                    break
        
                #-- Supply Credential --
                driver.find_element(By.ID, "id_userLoginId").send_keys(netflixSecret.appUsrnm);
                driver.find_element(By.ID, "id_password").send_keys(netflixSecret.appPass);

                #-- Click Login button --
                driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[1]/form/button").click();
                time.sleep(5);

                #-- Select Profile --
                driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[2]/div/a/div/div").click();
                time.sleep(5);

                #-- Play Content --
                driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/span/div/div/div/div/div/div[2]/div/div/div[3]/a/button").click();
                try:
                    find_status = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div").is_enabled();
                    print("Content playback success");
                except:
                    callAPI("Netflix Service Down Alert","Netflix Playback Error")
                    print("Content not playable");
    
                time.sleep(10);
                print(find_status);
                print(driver.title);
                driver.quit();

#-- Call function --
main_function();


