#coding: utf-8
import sys
from time import sleep
from datetime import datetime
from pygame import mixer
from os import getcwd

mixer.init(44100)

sound = mixer.music
sound.load("fx.mp3")
timer = 25

def pomodoro():

    global timer
    task = "🍅 None"
    if timer == 25:
        task = "🍅 Begin:"+ datetime.now().strftime("%d/%m/%Y %H:%M:%S") + ' | ' + input('What is the current task?')

    input('Press ENTER to start the timer. 🍅')

    print("Seconds are bad ヽ(ಠ_ಠ)ノ")
    for i in range(timer):
        time_left = '\rMinutes Left: ' + str(timer -i)

        sys.stdout.write(time_left) #escrevendo
        sys.stdout.flush() #atualizando
        sleep(60)

    global sound
    for e in range(3):
        sound.play()
        sleep(1)

    if timer == 25:
        log = open('pymodore_log.txt', 'a')
        log.write('\n' + task)
        log.close()

        timer = 5
        message = "\nStart rest? ('N' to quit)"
    else:
        timer = 25
        message = "\nStart new task? ('N' to quit)"

    progress = input(message)

    if progress.lower() == 'n' or progress.lower() == 'no':
        return print('Remember to check your log')

    pomodoro()

pomodoro()
