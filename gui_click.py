from random import choice

import PySimpleGUI as sg

from super_click import go_click
from threading import Timer, Thread, Event

themes = sg.theme_list()
# Безумие!! Выбор случайной темы!
sg.theme(choice(themes))
# Добавляем компоненты на форму
layout = [
    [sg.Text('Запуск кликера!!!!', key='work_textbox')],
    [sg.Text('Задержка в сек.'), sg.InputText(key='delay')],
    [sg.Button('Запустить', key='start_key'), sg.Button('Стоп', key='stop_key'), sg.Button('Выйти')]
]

# Создание окна
window = sg.Window('Мега Кликер', layout)


def start_clicks(delay):
    ticker = Event()
    while not ticker.wait(delay):
        go_click()
        global stop_thread
        if stop_thread:
            break


thread = None
stop_thread = False

# Цикл событий для обработки эвентов и значений элементов на форме
while True:
    event, values = window.read()
    # Выход из программы
    if event == sg.WIN_CLOSED or event == 'Выйти':
        break

    if event == 'start_key':
        print('Запуск...')
        window.Element('work_textbox').update(value='Запущено!!')
        delay = int(values["delay"]) if values["delay"].isdigit() else 1
        if thread is None:
            thread = Thread(target=start_clicks, args=(delay,))
            stop_thread = False
            thread.start()

    if event == 'stop_key':
        print('Остановка...')
        window.Element('work_textbox').update(value='Остановлено!!')
        stop_thread = True
        thread = None


window.close()
