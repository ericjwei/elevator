import time
import sched
import threading
import queue
import multiprocessing

#import datetime

from random import randint
from person import Person
#from control_system import control_system
from constants import RATIO, DAY_SECONDS, POPULATION, YEAR, FLOOR_HEIGHT, MAX_FLOOR

# def new_day(scheduler, base_time, demand_queue):
#     scheduler.enterabs(DAY_SECONDS + base_time, 1,
#                     new_day, (scheduler, base_time + DAY_SECONDS, demand_queue))
#     for _ in range(POPULATION):
#         person = Person(randint(2, MAX_FLOOR))
#         scheduler.enterabs(person.begin / RATIO + base_time, 2, demand_queue.put, (person,))
#         scheduler.enterabs(person.end / RATIO + base_time, 2, demand_queue.put, (person,))

def new_day(scheduler, base_time, demand_list):
    scheduler.enterabs(DAY_SECONDS + base_time, 1,
                    new_day, (scheduler, base_time + DAY_SECONDS, demand_list))
    for _ in range(POPULATION):
        person = Person()
        scheduler.enterabs(person.begin / RATIO + base_time, 2, demand_list[1].put, (person,))
        scheduler.enterabs(person.end / RATIO + base_time, 2, demand_list[person.floor * 2].put, (person,))

def demand_thread(demand_list, start_time):
    scheduler = sched.scheduler(time.time, time.sleep)
    new_day(scheduler, start_time, demand_list)    
    scheduler.run()

def print_time(start_time):
    t = time.strftime("%b-%d %H:%M:%S", time.gmtime((time.time() - start_time) * RATIO))
    print(f"Year {YEAR} {t}")

def main():
    start_time = time.time()
    demand_list = [ multiprocessing.Queue() for _ in range(MAX_FLOOR * 2 + 1) ]
    
    # demand_queue = queue.Queue()
    demand = threading.Thread(target=demand_thread, args=(demand_list, start_time))
    demand.start()

    # for i in demand_list:
    #     print(i.qsize())

    #control_system(demand_queue)

if __name__ == "__main__":
    main()
    

