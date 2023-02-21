from undetected_chromedriver import Chrome
import time 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def get_movie_link(movieName):
    driver = Chrome()

    movieLink = "https://soap2day.to/search/keyword/" + movieName.replace(" ","%20")
    #Opens webpage
    driver.get(movieLink)

    #Finds continue button and presses it
    home = driver.find_element("xpath", '//a')
    home.click()

    #Waits for browser to load and find the first movie search result
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-info']")))
    movieSearch = driver.find_elements("xpath", "//a")[28]
    #Opens webpage linked to first search result
    driver.get(movieSearch.get_attribute('href'))

    #Waits for browser to load and gets the video WebElement
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//video[@class='jw-video jw-reset']")))
    video = driver.find_element("xpath", "//video")
    #Gets video mp4 link from 
    return video.get_attribute('src')

def get_watchpubs_link(movieName):
    driver = Chrome()

    videoLink = get_movie_link(movieName)

    #Opens WatchPubs and waits for load
    driver.get("https://app.watchpubs.com")
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//span[@class='MuiButton-label']")))
    #Clicks on button to start new Private party
    privateButton = driver.find_elements("xpath", "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-text jss18']")[1]
    privateButton.click()

    #Waits for site to load and clicks menu option (bottom right)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search Youtube or paste a link...']")))
    menuButton = driver.find_element("xpath", "//button[@id='room_playlist']")
    menuButton.click()
    
    #Waits for options menu to appear and clicks on edit button next to name field
    time.sleep(0.5)
    nameButton = driver.find_elements("xpath", "//button")[8]
    nameButton.click()

    #Waits for name input field to appear and double clicks on name field, changing the name to 'Rishi Movie Bot'
    time.sleep(0.5)
    nameInput = driver.find_element("xpath", "//input[@placeholder='Enter nickname...']")
    ActionChains(driver).double_click(nameInput).perform()
    nameInput.send_keys("Rishi Movie Bot" + Keys.RETURN)

    #Waits for name to change and enters movie mp4 link into input underneath the video player
    time.sleep(0.5)
    videoInput = driver.find_element("xpath", "//input[@placeholder='Search Youtube or paste a link...']")
    videoInput.send_keys(videoLink + Keys.RETURN)

    #Waits for movie link to load into video available for selection; Then clicks on the video selection to play it
    WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.XPATH, "//*[local-name() = 'svg'][@title='Add to playlist']")))
    try:
        videoRep = driver.find_element("xpath", "//div[@class='jss267']")
    except:
        videoRep = driver.find_element("xpath", "//div[@class='jss264']")
    videoRep.click()

    #Gets link for WebPubs party
    partyLink = driver.current_url

    #Returns [0] WebPubs link and [1] mp4 movie video link
    return partyLink

    #Stops browser from closing
    #time.sleep(10000) 