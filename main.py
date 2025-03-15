from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver.common.action_chains import ActionChains
import requests
import json
import os
import sys

WEBHOOK_URL = "DISCORD-WEBHOOK"

def send_to_discord(email, password):
    embed = {
        "embeds": [
            {
                "title": "CapCut Account Details",
                "description": f"**Details:**\n\n`{email}:{password}`",
                "color": 7506394,
                "thumbnail": {
                    "url": "https://media.discordapp.net/attachments/1154900995638313001/1350345704538640434/capcut-logo-on-transparent-white-background-free-vector.jpg?ex=67d666f0&is=67d51570&hm=b95e70d6ddb40c100c9fd348b42eba9c614eda78eec7325d228977337e5308d5&=&format=webp&width=648&height=648"
                },
                "image": {
                    "url": "https://media.discordapp.net/attachments/1154900995638313001/1350345825242316851/3f7c59f36d529f90-1200.png?ex=67d6670c&is=67d5158c&hm=837169ae3aadd7c972fe7e0da98a3085927663151f85c782ede60607f7b70abf&=&format=webp&quality=lossless&width=1088&height=544"
                }
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.post(WEBHOOK_URL, data=json.dumps(embed), headers=headers)
    
    if response.status_code == 204:
        print("Message successfully sent to Discord.")
    else:
        print(f"Error sending message: {response.status_code}")

def open_capcut_signup():
    options = Options()
    options.add_argument("--disable-webrtc")
    options.add_argument("--start-maximized")

    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    driver.get("https://www.capcut.com/signup")
    
    driver.execute_script("window.open('https://temp-mail.io/de', '_blank');")
    
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    
    email_element = driver.find_element(By.ID, "email")
    email_address = email_element.get_attribute("value")
    
    driver.switch_to.window(driver.window_handles[0])
    
    username_field = driver.find_element(By.NAME, "signUsername")
    username_field.send_keys(email_address)
    
    button = driver.find_element(By.CSS_SELECTOR, '.lv-btn.lv-btn-primary.lv-btn-size-default.lv-btn-shape-square.lv_sign_in_panel_wide-primary-button')
    button.click()
    
    time.sleep(1)
    
    password_field = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
    password = "BumBum11!"
    password_field.send_keys(password)
    
    sign_in_button = driver.find_element(By.CSS_SELECTOR, '.lv-btn.lv-btn-primary.lv-btn-size-large.lv-btn-shape-square.lv_sign_in_panel_wide-sign-in-button.lv_sign_in_panel_wide-primary-button')
    sign_in_button.click()
    
    time.sleep(1)

    try:
        year_field = driver.find_element(By.XPATH, '//*[contains(@placeholder, "Jahr")]')
        year_field.send_keys("2000")
        print("Year set to 2000.")

        actions = ActionChains(driver)
        (actions
         .send_keys(Keys.TAB)
         .send_keys(Keys.ENTER)
         .send_keys(Keys.ENTER)
         .send_keys(Keys.TAB)
         .send_keys(Keys.ENTER)
         .send_keys(Keys.ENTER)
         .perform())
        print("Automatically selected month and day")
    except Exception as e:
        print(f"Error while setting year: {e}")
    
    print("Please manually select the month and day.")

    while True:
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, '.lv-btn.lv-btn-primary.lv-btn-size-default.lv-btn-shape-square.lv_sign_in_panel_wide-birthday-next')
            
            if "lv-btn-disabled" not in next_button.get_attribute("class"):
                print("Button is enabled. Clicking the 'Next' button.")
                next_button.click()
                break
            else:
                print("Button is still disabled. Waiting for it to be enabled.")
        
        except Exception as e:
            print(f"Error: {e}. Retrying...")

        time.sleep(1)

    print("Waiting for email with verification code...")
    
    driver.switch_to.window(driver.window_handles[1])
    email_found = False
    
    while not email_found:
        try:
            email_subject_element = driver.find_element(By.CLASS_NAME, "message__subject")
            email_subject = email_subject_element.text
            
            match = re.search(r'(\d+)$', email_subject)
            if match:
                verification_code = match.group(1)
                print(f"Found verification code: {verification_code}")
                email_found = True
        except Exception as e:
            print("Email not yet received or could not find subject. Retrying...")
        
        time.sleep(2)
    
    driver.switch_to.window(driver.window_handles[0])

    try:
        verification_input = driver.find_element(By.CLASS_NAME, "verification_code_input-number")
        
        actions = ActionChains(driver)
        
        for digit in verification_code:
            actions.send_keys(digit)
        actions.perform()

        print("Verification code entered successfully.")
    except Exception as e:
        print(f"Error while entering verification code: {e}")

    send_to_discord(email_address, password)

    print("Browser will be closed now.")
    driver.quit()

def clear_screen():
    if os.name == 'nt':
        os.system('cls')

def main():
    print("\033[34m░█████╗░░█████╗░░█████╗░██████╗░░█████╗░██╗░░░██╗████████╗")
    print("██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝")
    print("██║░░╚═╝███████║██║░░╚═╝██████╔╝██║░░╚═╝██║░░░██║░░░██║░░░")
    print("██║░░██╗██╔══██║██║░░██╗██╔═══╝░██║░░██╗██║░░░██║░░░██║░░░")
    print("╚█████╔╝██║░░██║╚█████╔╝██║░░░░░╚█████╔╝╚██████╔╝░░░██║░░░")
    print("░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░░╚════╝░░╚═════╝░░░░╚═╝░░░" + " Made by DasoFabe\033[0m")
    
    repeat_count = int(input("How many times do you want to repeat the process? "))
    
    for _ in range(repeat_count):
        clear_screen()
        open_capcut_signup()
        print("\033[32m░██████╗██╗░░░██╗░█████╗░░█████╗░███████╗░██████╗")
        print("██╔════╝██║░░░██║██╔══██╗██╔══██╗██╔════╝██╔════╝")
        print("╚█████╗░██║░░░██║██║░░╚═╝██║░░╚═╝█████╗░░╚█████╗░")
        print("░╚═══██╗██║░░░██║██║░░██╗██║░░██╗██╔══╝░░░╚═══██╗")
        print("██████╔╝╚██████╔╝╚█████╔╝╚█████╔╝███████╗██████╔╝")
        print("╚═════╝░░╚═════╝░░╚════╝░░╚════╝░╚══════╝╚═════╝░\033[0m")
        time.sleep(5)

if __name__ == "__main__":
    main()
