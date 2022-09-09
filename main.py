import pyautogui
import time

pyautogui.alert("Clique em OK para iniciar o processo, lembre-se de não mexer em nada até o processo finalizar")
pyautogui.PAUSE = 0.5

like = 3 # Numero de vídeos passados até 1 like
seconds = 5 # Segundos pra deixar rolando o vídeo
count = 0 # Número de vídeos que deseja assistir


pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('https://tiktok.com')
pyautogui.press('enter')

time.sleep(5)

pyautogui.moveTo(1061,561)
pyautogui.click()

while count > 0:
    time.sleep(seconds)

    if (count % like == 0):
        pyautogui.press('l')

    pyautogui.press('down')
    count = count - 1