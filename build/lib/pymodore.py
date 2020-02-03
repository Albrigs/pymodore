#coding: utf-8
from sys import stdout, stdin
from select import select
from time import sleep, time
from datetime import datetime
from termcolor import colored
import click
from os import getenv, system, name
from vlc import MediaPlayer


@click.command()

#montagem de opções
@click.option('--task', default=25, help='Time for tasks')
@click.option('--rest', default=5, help='Time for small rests.')
@click.option('--bigrest', default=30, help='Time for big rest.')
@click.option('--maxrounds', default=4, help='Number of tasks before a big rest.')


def pomodoro(task, rest, bigrest, maxrounds):
    system('cls' if name == 'nt' else 'clear')
    sound = MediaPlayer("fx.mp3")
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

        #chamada ao fim do loop
        def selection_screen(isnt_timeout):
            nonlocal state
            nonlocal task
            nonlocal cfg

            system('cls' if name == 'nt' else 'clear')

            log_folder = getenv('HOME')

            # task block
            if state['cur'] == 'task':

                #inserindo tempo decorrido para que a tarefa seja concluída
                if isnt_timeout:
                    task += ' | TIME: {0} minutes'.format(isnt_timeout)
                else:
                    task += ' | TIME: {0} minutes'.format(cfg['task'])

                # criando log no log_folder
                log = open('{0}/pymodore_log.txt'.format(log_folder), 'a')
                log.write('\n' + task)
                log.close()

                #big rest block
                if state['rounds'] == cfg['max_rounds']:
                    state['cur'] = 'big_rest'
                    log = open('{0}/pymodore_log.txt'.format(log_folder), 'a')
                    log.write('\n' + '|-🍅-🍅- REST -🍅-🍅-|')
                    log.close()
                    message = "\nTime for a big rest! Press {0} and take {1} mins! {2}".format(colored('ENTER','green'), colored(cfg['big_rest'], 'red') , colored("('N' to quit)",'magenta'))

                #rest block
                else:
                    state['cur'] = 'rest'
                    message = "\nStart rest? {0} to continue. {1}".format(colored('ENTER','green'), colored("('N' to quit)",'magenta'))

            #iniciando nova tarefa
            else:
                state['cur'] = 'task'
                message = "\nStart new task? {0} to continue. {1}".format(colored('ENTER','green'), colored("('N' to quit)",'magenta'))

            #saindo ou processeguindo no loop
            willcontinue = input(message)
            if willcontinue:
                if willcontinue.strip().lower()[0] == 'n':
                    return print(colored('Remember to check your log in {0}'.format(log_folder), 'red'))
            loopomodore()

        input('Press {0} to start the timer. {1}'.format(colored('ENTER','green'), colored('🍅', 'red')))
        if state['cur'] == 'task':
            print("Seconds are bad "+ colored('ヽ(ಠ_ಠ)ノ', 'red') + colored('\nTo finish current task press F and ENTER', 'magenta' ))


        #loop de atividade
        for i in range(cfg[state['cur']]):
            CICLE_SIZE = 0.1
            time_left = '\rMinutes Left: ' + colored(str(cfg[state['cur']] -i),'blue')

            stdout.write(time_left) #escrevendo


            #finalizador de tarefas
            if state['cur'] == 'task':
                s_i, s_o, s_e = select([stdin], [], [], CICLE_SIZE)

                #se for digitada qualquer coisa no input
                if s_i:
                    return selection_screen(i+1)

            stdout.flush() #atualizando

            if state['cur'] != 'task':
                sleep(CICLE_SIZE)

        # fim do timer
        for e in range(5):
            sound.play()
            sleep(0.5)
            sound.stop()


        selection_screen(0)

    #inicio do loop
    loopomodore()

if __name__ == '__main__':
    pomodoro()
