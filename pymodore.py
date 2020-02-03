#coding: utf-8
from sys import stdout
from time import sleep
from datetime import datetime
from pygame import mixer
from termcolor import colored
import click

@click.command()
@click.option('--task', default=25, help='Time for tasks')
@click.option('--rest', default=5, help='Time for small rests.')
@click.option('--bigrest', default=30, help='Time for big rest.')
@click.option('--maxrounds', default=4, help='Number of tasks before a big rest.')


def pomodoro(task, rest, bigrest, maxrounds):
    mixer.init(44100)

    sound = mixer.music
    sound.load("fx.mp3")

    state = {
        'cur': 'task',
        'rounds': 0
    }

    cfg = {
        'task': task,
        'rest': rest,
        'big_rest': bigrest,
        'max_rounds': maxrounds
    }

    def loopomodore():
        nonlocal state
        nonlocal cfg
        nonlocal sound

        task = "🍅 None"
        if state['cur'] == 'task':
            state['rounds'] += 1
            task = "🍅 Begin:"+ datetime.now().strftime("%d/%m/%Y %H:%M:%S") + ' | ' + input(colored('What is the current task?\n','green'))

        input('Press {0} to start the timer. {1}'.format(colored('ENTER','green'), colored('🍅', 'red')))

        if state['cur'] == 'task':
            print("Seconds are bad "+ colored('ヽ(ಠ_ಠ)ノ', 'red'))

        for i in range(cfg[state['cur']]):
            time_left = '\rMinutes Left: ' + colored(str(cfg[state['cur']] -i),'blue')

            stdout.write(time_left) #escrevendo
            stdout.flush() #atualizando
            sleep(1)

        # fim do timer
        for e in range(3):
            sound.play()
            sleep(1)

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
        if progress:
            if progress.strip().lower()[0] == 'n':
                return print(colored('Remember to check your log', 'red'))
        loopomodore()

    loopomodore()

if __name__ == '__main__':
    pomodoro()
