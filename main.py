from platform import python_branch
import random
import pyautogui
import time

if (pyautogui.confirm('Clique em OK para iniciar o processo, lembre-se de não mexer em nada até o processo finalizar e de estar logado na conta da Deeply no Tiktok previamente.') == 'Cancel'):
    exit()

pyautogui.PAUSE = 0.5

# VARIÁVEIS EDITÁVEIS

likemin = 1 # Número mínimo de videos assistidos para deixar like
likemax = 10 # Número máximo de videos assistidos para deixar like
secondsmin = 5 # Número mínimo de segundos para deixar rolando o vídeo
secondsmax = 45 # Número máximo de segundos para deixar rolando vídeo
videos = 1 # Número de vídeos que deseja assistir
search = '#sneakers' # Texto a ser procurado no Tiktok para filtrar os vídeos

# FIM VARIÁVEIS EDITÁVEIS

like = random.randrange(likemin, likemax) # Número de vídeos passados até 1 like, número aleatório entre 1 e 10, troca toda vez que é deixado um like - Linha 37
seconds = random.randrange(secondsmin, secondsmax) # Segundos pra deixar rolando o vídeo, número aleatório entre 5 e 45 segundos, troca toda vez que termina de assistir um vídeo - Linha 34

pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('https://tiktok.com')
pyautogui.press('enter')

time.sleep(5)

pyautogui.moveTo(835, 100, duration=1)
pyautogui.click()
pyautogui.write(search)
pyautogui.press('enter')

pyautogui.moveTo(880, 365, duration=1)
pyautogui.click()

while videos > 0:
    time.sleep(seconds)
    seconds = random.randrange(secondsmin, secondsmax)
    if (videos % like == 0):
        pyautogui.press('l')
        like = random.randrange(likemin, likemax)

    pyautogui.press('down')
    videos = videos - 1

pyautogui.hotkey('ctrl', 'w')