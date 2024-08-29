# importa bibliotecas
import pyautogui as auto
import time

# Input de dados
repo = input('Informe o link do seu repositorio: ')
commit = input('Escreva seu commit: ')

auto.PAUSE = 1

auto.press('win')
auto.write('vscode')
auto.press('enter')

time.sleep(4)

auto.hotkey('ctrl', 'j')
time.sleep(4)

auto.write('git init')
auto.press('enter')
auto.write('git add .')
auto.press('enter')
auto.write(f'git commit -m "{commit}"')
auto.press('enter')

time.sleep(4)

auto.write('git branch -M main')
auto.press('enter')
auto.write(f'git remote add origin {repo}')
auto.press('enter')

auto.write('git push -u origin main')
auto.press('enter')
