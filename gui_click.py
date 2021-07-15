from random import choice

import PySimpleGUI as sg

from super_click import go_click
from threading import Timer

themes = sg.theme_list()
# Безумие!! Выбор случайной темы!
sg.theme(choice(themes))
# Добавляем компоненты на форму
layout = [
    [sg.Text('Запуск кликера!!!!')],
    [sg.Text('Задержка в сек.'), sg.InputText(key='delay')],
    [sg.Button('Запустить', key='start_key'), sg.Button('Выйти')]
]

# Создание окна
window = sg.Window('Мега Кликер', layout)



def timer_tick():
    go_click()


timer = Timer(1, timer_tick)

# Цикл событий для обработки эвентов и значений элементов на форме
while True:
    event, values = window.read()
    # Выход из программы
    if event == sg.WIN_CLOSED or event == 'Выйти':
        break

    if event == 'start_key':
        print('Запуск...')
        delay = int(values["delay"]) if values["delay"].isdigit() else 1
        timer = Timer(delay, timer_tick)
        timer.start()


window.close()
