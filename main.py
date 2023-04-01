from sys import platform
from platform import python_branch
import pyautogui
import os
import random
import time

if (pyautogui.confirm('Clique em OK para iniciar o processo, lembre-se de não mexer em nada até o processo finalizar e de estar logado na conta da Deeply no Tiktok previamente.') == 'Cancel'):
    exit()

# VARIÁVEIS EDITÁVEIS
pyautogui.PAUSE = 1
likemin = 1 # Número mínimo de videos assistidos para deixar like
likemax = 2 # Número máximo de videos assistidos para deixar like
secondsmin = 5 # Número mínimo de segundos para deixar rolando o vídeo
secondsmax = 10 # Número máximo de segundos para deixar rolando vídeo
videos = 3 # Número de vídeos que deseja assistir

# FIM VARIÁVEIS EDITÁVEIS

browserPath = '/Applications/Google\ Chrome.app'
like = random.randrange(likemin, likemax) # Número de vídeos passados até 1 like, número aleatório entre 1 e 10, troca toda vez que é deixado um like - Linha 37
seconds = random.randrange(secondsmin, secondsmax) # Segundos pra deixar rolando o vídeo, número aleatório entre 5 e 45 segundos, troca toda vez que termina de assistir um vídeo - Linha 34

if (platform == 'darwin') :
    os.system(f"open {browserPath}")
else : 
    pyautogui.press('winleft')
    pyautogui.write('chrome')
    pyautogui.press('enter')

time.sleep(2)

pyautogui.write('https://tiktok.com')
pyautogui.press('enter')

time.sleep(10)

pyautogui.moveTo(362, 250, duration=1)
pyautogui.click()

while videos > 0:
    time.sleep(seconds)
    seconds = random.randrange(secondsmin, secondsmax)
    if (videos % like == 0):
        pyautogui.press('l')
        like = random.randrange(likemin, likemax)

    pyautogui.press('down')
    videos = videos - 1

pyautogui.hotkey('command', 'w')