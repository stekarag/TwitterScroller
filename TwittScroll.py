from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import getpass

"""
A function that uses selenium and chromedriver to scroll through the tweets of a Twitter account.
"""

def seeTweets(uname,pword,speed):
 
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("https://twitter.com/home")
    time.sleep(2)


    driver.find_element_by_name("session[username_or_email]").send_keys(uname)
    time.sleep(2)
 
    driver.find_element_by_name("session[password]").send_keys(pword)
    time.sleep(2)

    driver.find_element_by_xpath("//div[@class='css-1dbjc4n']/div[@role='button']").click()
    time.sleep(2)
    #driver.maximize_window() 

    while(1):
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        no = str(0.01*speed)
        cmd = "window.scrollBy(%s);"%no
        driver.execute_script(cmd) 
        time.sleep(0.01)
    print('done')

print("\nWith twitter scroller you can watch your twitter feeds scroll down by themselves!")
u = input("Enter username or email: ")
p = getpass.getpass("Enter password for %s: "%u)
j = 1
while j:
    try:
        s = int(input("Enter speed (1, 2, 3 etc): "))
        j = 0
    except ValueError:
        print("Please reenter an integer for speed.")

seeTweets(u,p,s)

#augment letter size twice
