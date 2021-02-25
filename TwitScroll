from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time

"""
A function that uses selenium and chromedriver to scroll through the tweets of a Twitter account.
"""

def seeTweets(uname,pword):
 
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("https://twitter.com/home") #open the browser and visit the url
    time.sleep(2) #if the connection is slow alter this


    driver.find_element_by_name("session[username_or_email]").send_keys(uname)
    print('\nName succesfully entered')
    time.sleep(2)
 
    driver.find_element_by_name("session[password]").send_keys(pword)
    print('Password succesfully entered')
    time.sleep(2)

    driver.find_element_by_xpath("//div[@class='css-1dbjc4n']/div[@role='button']").click()
    print('Button pressed')

    print('Getting homepage\n')
    
    #driver.maximize_window() 

    while(1):
        driver.execute_script("window.scrollBy(0,30);") 
        time.sleep(0.5)
    print('done')

print("\nWith twitter scroller you can watch your twitter feeds scroll down by themselves!\n")
u = input("Enter username or email: ")
p = input("Enter password for (%s):"%u)
seeTweets(u,p)
