import pyautogui
import click

from pynput.keyboard import Key, Listener, KeyCode


RESUME_KEY = 'z'
PAUSE_KEY = 'x'
EXIT_KEY = 'c'

STATES = {
    RESUME_KEY: (True, False, 'Resumed'),
    PAUSE_KEY: (True, True, 'Paused'),
    EXIT_KEY: (False, False, 'Exit'),

}


def change_state(state: str) -> None:
    """
    Меняет состояние программы в зависимости от нажатой клавиши
    :param state: Нажатая кнопка в виде строки
    """
    global running, pause

    running, pause, info_aaa = STATES[state]
    print(info_aaa)


pause = True
running = True


def on_press(key: KeyCode):
    """
    Обработка нажатий
    :param key:
    :return:
    """
    lower_key = key.char.lower()
    if lower_key in STATES:
        change_state(lower_key)


def display_controls(delay):
    """
    Отображает сообщение о запуске программы и краткую справку
    :param delay:
    :return:
    """

    print("*** Settings: ***")
    print(f"\t delay = {delay} sec")
    print("*** Controls: ***")
    for key, (_, _, info) in STATES.items():
        print(f"{key} = {info}")


def start_click(delay, run_immediately=False):
    """
    Запускает и останавливает кликер
    :param run_immediately: запускает кликер сразу
    :param delay: задержка между кликами
    """
    global running, pause
    lis = Listener(on_press=on_press)
    lis.start()
    if run_immediately:
        running = True
        pause = False

    display_controls(delay)
    while running:
        if not pause:
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
    lis.stop()


def go_click():
    pyautogui.click(pyautogui.position())


@click.command()
@click.option('-delay', '-d', default=1, type=click.INT, help='Задержка между нажатиями в секундах')
def main(delay):
    start_click(delay)


if __name__ == "__main__":
    main()
