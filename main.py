#coding: utf-8
import sys
from time import sleep
from datetime import datetime
from pygame import mixer
mixer.pre_init(44100, 16, 2, 4096)
mixer.init()

sound = mixer.Sound("fx.mp3")
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
    for e in range(7):
        sound.play()

    if timer == 25:
        log = open('pymodore_log.txt', 'a')
        log.write('\n' + task)
        log.close()

        timer = 5
        message = "Start rest? ('N' to quit)"
    else:
        timer = 25
        message = "Start new task? ('N' to quit)"

    progress = input(message)

    if progress.lower() == 'n' or progress.lower() == 'no':
        return print('Remember to see your log')

    pomodoro()

pomodoro()
