import time
import datetime
import random
import sched
import threading

from person import Person

SPEED = .25
POPULATION = 50
 
current_time = datetime.datetime(1,1,1)
week_day = 1 #start on Monday
occupants = []

def populate_building():
    # for _ in range(POPULATION):
        # print('hey')
    None

def print_datetime():
    print(f"Day: {week_day} {current_time.time()}")

def add_time():
    global current_time
    global week_day
    if(current_time.time() == datetime.time(23,45)):
        if(week_day == 7):
            week_day = 1
        else:
            week_day += 1 
    current_time = current_time + datetime.timedelta(minutes = 15)

def periodic(scheduler, interval, action, actionargs=()):
    scheduler.enter(interval, 1, periodic, 
                    (scheduler, interval, action, actionargs))
    action(*actionargs)
    print_datetime()

def clock_thread():
    scheduler = sched.scheduler(time.time, time.sleep)
    time.sleep(SPEED)
    periodic(scheduler, SPEED, add_time)
    scheduler.run()

def demand_proc():
    # set number of people, pick someone from the dictionary and have them come into the building
    print("demand")
        
def main():
    populate_building()
    clock = threading.Thread(target=clock_thread)
    clock.start()
    while(True):
        if(current_time.time() == datetime.time(7,00)):
            print("Good morning")
            time.sleep(1)
        if(current_time.time() == datetime.time(12,00)):
            print("Good afternoon")
            time.sleep(1)
        if(current_time.time() == datetime.time(18,00)):
            print("Good evening")    
            time.sleep(1)

if __name__ == "__main__":
    main()
    
