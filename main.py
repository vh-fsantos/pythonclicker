import pyautogui
import time

pyautogui.alert("Clique em OK para iniciar o processo, lembre-se de não mexer em nada até o processo finalizar")
pyautogui.PAUSE = 0.5
count = 0


pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('https://tiktok.com')
pyautogui.press('enter')

time.sleep(5)

pyautogui.moveTo(1061,561,duration=1)
pyautogui.click()

while count < 5:
    time.sleep(5)

    # if (count % 2 == 0):
    #     pyautogui.press('l')

    pyautogui.press('down')
    count = count + 1