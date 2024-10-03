import pyautogui
import keyboard
from threading import Thread


# Funções para cada verificação de cor e ação correspondente
def check_color_a():
    if pyautogui.pixelMatchesColor(1279, 981, (0, 152, 0)):
        pyautogui.press("a")


def check_color_s():
    if pyautogui.pixelMatchesColor(1368, 981, (255, 0, 0)):
        pyautogui.press("s")


def check_color_j():
    if pyautogui.pixelMatchesColor(1459, 982, (244, 244, 2)):
        pyautogui.press("j")


def check_color_k():
    if pyautogui.pixelMatchesColor(1549, 979, (0, 152, 255)):
        pyautogui.press("k")


def check_color_l():
    if pyautogui.pixelMatchesColor(1644, 981, (255, 101, 0)):
        pyautogui.press("l")


# Loop principal que roda até que a tecla "1" seja pressionada
while not keyboard.is_pressed("1"):
    # Cria threads para cada verificação de cor
    thread_a = Thread(target=check_color_a)
    thread_s = Thread(target=check_color_s)
    thread_j = Thread(target=check_color_j)
    thread_k = Thread(target=check_color_k)
    thread_l = Thread(target=check_color_l)

    # Inicia todas as threads
    thread_a.start()
    thread_s.start()
    thread_j.start()
    thread_k.start()
    thread_l.start()

    # Espera que todas as threads terminem antes de continuar o loop
    thread_a.join()
    thread_s.join()
    thread_j.join()
    thread_k.join()
    thread_l.join()
