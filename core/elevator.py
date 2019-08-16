import time
import datetime
import sched
import threading
import queue

from random import randint
from person import Person

SPEED = .25
DAY_SECONDS = 86400
POPULATION = 50
MAX_FLOOR = 10
YEAR = 1
#BASE_TIME = None
START_TIME = None

current_time = datetime.datetime(1,1,1)
week_day = 1 #start on Monday

# occupants = []

# def print_datetime():
#     print(f"Day: {week_day} {current_time.time()}")

# def add_time():
#     global current_time
#     global week_day
#     if(current_time.time() == time(23,45)):
#         if(week_day == 7):
#             week_day = 1
#         else:
#             week_day += 1 
#     current_time = current_time + timedelta(minutes = 15)

# def periodic(scheduler, interval, action, actionargs=()):
#     scheduler.enter(interval, 1, periodic, 
#                     (scheduler, interval, action, actionargs))
#     action(*actionargs)
#     print_datetime()

# def clock_thread():
#     scheduler = sched.scheduler(time.time, time.sleep)
#     time.sleep(SPEED)
#     periodic(scheduler, SPEED, add_time)
#     scheduler.run()

# def populate_building():
#     for _ in range(POPULATION):
#         person = Person(randint(2, MAX_FLOOR))
#         person.set_begin()
#         person.set_end()
#         occupants.append(person)    

def new_day(scheduler, baseTime, demand_queue):
    scheduler.enter(DAY_SECONDS - (time.time() - baseTime), 1,
                    new_day, (scheduler, baseTime + DAY_SECONDS, demand_queue))
    occupants = []
    for _ in range(POPULATION):
        person = Person(randint(2, MAX_FLOOR))
        person.set_begin()
        person.set_end()
        occupants.append(person)  
    occupants.sort(key=lambda x: x.begin)
    demand_queue.put(occupants)
    # for p in occupants:
    #     p.print_info()
    print(baseTime)
    print_time()

def demand_thread(demand_queue):
    #populate_building()
    baseTime = START_TIME
    scheduler = sched.scheduler(time.time, time.sleep)
    new_day(scheduler, baseTime, demand_queue)    
    scheduler.run()

def print_time():
    t = time.strftime("%b-%d %H:%M:%S", time.gmtime(time.time() - START_TIME))
    print(f"Year {YEAR} {t}")

def main():
    global START_TIME
    START_TIME = time.time()
    # print(START_TIME)
    # print_time()
    demand_queue = queue.Queue()
    demand = threading.Thread(target=demand_thread, args=(demand_queue,))
    demand.start()

    while(True):
        occupants = demand_queue.get()
        print_time()
        for p in occupants:
            p.print_info()
        
    
    # clock = threading.Thread(target=clock_thread)
    # clock.start()
    # while(True):
    #     if(current_time.time() == datetime.time(7,00)):
    #         print("Good morning")
    #         time.sleep(1)
    #     if(current_time.time() == datetime.time(12,00)):
    #         print("Good afternoon")
    #         time.sleep(1)
    #     if(current_time.time() == datetime.time(18,00)):
    #         print("Good evening")    
    #         time.sleep(1)

if __name__ == "__main__":
    main()
    

