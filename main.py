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
        task = "🍅 Begin:"+ datetime.now().strftime("%d/%m/%Y %H:%M:%S") + ' | ' + input(colored('What is the current task?\n','green'))

    input('Press {0} to start the timer. {1}'.format(colored('ENTER','green'), colored('🍅', 'red')))
    print("Seconds are bad "+ colored('ヽ(ಠ_ಠ)ノ', 'red')) if state['cur'] == 'task'

    for i in range(cfg[state['cur']]):
        time_left = '\rMinutes Left: ' + colored(str(cfg[state['cur']] -i),'blue')

        sys.stdout.write(time_left) #escrevendo
        sys.stdout.flush() #atualizando
        sleep(1)

    # fim do timer
    for e in range(3):
        sound.play()
        sleep(60)

    if state['cur'] == 'task':
        log = open('pymodore_log.txt', 'a')
        # log.write('\n' + task)
        log.close()
        if state['rounds'] == cfg['max_rounds']:
            state['cur'] = 'big_rest'
            message = "\nTime for a big rest! Press {0} and take 30 mins! {1}".format(colored('ENTER','green'), colored("('N' to quit)",'magenta'))

        else:
            state['cur'] = 'rest'
            message = "\nStart rest? {0} to continue. {1}".format(colored('ENTER','green'), colored("('N' to quit)",'magenta'))

    else:
        state['cur'] = 'task'
        message = "\nStart new task? {0} to continue. {1}".format(colored('ENTER','green'), colored("('N' to quit)",'magenta'))

    progress = input(message)
    if progress.strip().lower()[0] == 'n':
        return print(colored('Remember to check your log', 'red'))

    pomodoro()

pomodoro()
