import threading
import time

def clean_house():
    time.sleep(2)
    print('Cleaning the house')

def walk_dog():
    time.sleep(2)
    print('Walking the dog')

def take_out_the_trash():
    time.sleep(2)
    print('Taking out the trash')


clean_house()
walk_dog()
take_out_the_trash()



