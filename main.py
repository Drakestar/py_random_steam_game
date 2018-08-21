import pyautogui
import time

file = open("games.txt", "r")
#time.sleep(5)
# Switch to browser
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt')
# For every line write the game title
for game in file.readlines():
    for character in game:
        pyautogui.press(character)
    #pyautogui.press('enter')
file.close()

