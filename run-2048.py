from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import random
import time
import sys

def run():
    try :
        driver = webdriver.Firefox()
        driver.get('https://play2048.co/')

        key_strokes = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]

        game_state_elm = driver.find_element_by_css_selector('.game-container p')
        htmlElem = driver.find_element_by_css_selector('html')
        

        while game_state_elm.text != 'Game over!':
            
            htmlElem.send_keys(key_strokes[random.randint(0, 3)])
            game_state_elm = driver.find_element_by_css_selector('.game-container p')

        score = driver.find_element_by_css_selector('.score-container').text

        print(f'Your score is: {score}')
        time.sleep(5)
        driver.quit()

    except :
        sys.exit("Invalid url")



if __name__ == '__main__':
    run()
