#coding: utf-8
import sys
from time import sleep
from datetime import datetime
from pygame import mixer
from termcolor import colored

mixer.init(44100)

sound = mixer.music
sound.load("fx.mp3")

# edit this for
cfg = {
    'task': 25,
    'rest': 5,
    'big_rest': 30,
    'max_rounds': 4
}

state = {
    'cur': 'task',
    'rounds': 0
}

def pomodoro():
    global sound
    global state
    global cfg

    task = "🍅 None"
    if state['cur'] == 'task':
        state['rounds'] += 1
        task = "🍅 Begin:"+ datetime.now().strftime("%d/%m/%Y %H:%M:%S") + ' | ' + input('What is the current task?')

    input('Press ENTER to start the timer. 🍅')
    print("Seconds are bad ヽ(ಠ_ಠ)ノ")

    for i in range(cfg[state['cur']]):
        time_left = '\rMinutes Left: ' + str(cfg[state['cur']] -i)

        sys.stdout.write(time_left) #escrevendo
        sys.stdout.flush() #atualizando
        sleep(1)

    # fim do timer
    for e in range(3):
        sound.play()
        sleep(1)

    if state['cur'] == 'task':
        log = open('pymodore_log.txt', 'a')
        log.write('\n' + task)
        log.close()
        if state['rounds'] == cfg['max_rounds']:
            state['cur'] = 'big_rest'
            message = "\nTime for a big rest! Press ENTER and take 30 mins! ('N' to quit)"

        else:
            state['cur'] = 'rest'
            message = "\nStart rest? ('N' to quit)"

    else:
        state['cur'] = 'task'
        message = "\nStart new task? ('N' to quit)"


    progress = input(message)
    if progress.lower() == 'n' or progress.lower() == 'no':
        return print('Remember to check your log')

    pomodoro()

pomodoro()
