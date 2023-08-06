# Created to send a message to a WhatsApp group when a notification arrives, but Windows 11 notifications prevent completing the idea.
# Made by Guilherme Romano in 2023
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui
import keyboard

def notification_action(message):
    print("Notification received! Performing action...")
    time.sleep(1)
    pyautogui.moveTo(-1066, 810)
    pyautogui.click()
    pyautogui.typewrite(message, interval=0.1)
    pyautogui.press("enter")
    print("Success")

def wait_for_key_combination(keys):
    print("Press the key combination:", keys)
    while not keyboard.is_pressed(keys):
        pass

# Create a ChromeDriver instance using Webdriver-Manager and open WhatsApp.
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
time.sleep(2)

# Drag to the other window.
pyautogui.moveTo(498, 27)
pyautogui.dragTo(-600, 0, 1)

print("Waiting")
wait_for_key_combination("ctrl+alt")

# Update WhatsApp.
pyautogui.moveTo(-1731, 349)
pyautogui.click()

print("Waiting")
wait_for_key_combination("ctrl+alt")

# Clear notifications, click on the group, then the chat - ready to write.
pyautogui.moveTo(-1476, 336)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(-1650, 369)
pyautogui.click()


# Click on the chat, write the text, send, and it's ready.
pyautogui.moveTo(-1066, 810)
pyautogui.click()
message = "AnonDesk Online!"
pyautogui.typewrite(message, interval=0.05)
pyautogui.press("enter")
print("Sent")

print("listening")
wait_for_key_combination("ctrl+alt")

#while True:
    # the idea is to listen to the win notifications an send a message on whatsapp