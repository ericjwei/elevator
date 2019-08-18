import time
# import datetime
import sched
import threading
import queue

from random import randint
from person import Person

SPEED = .25
RATIO = 300
DAY_SECONDS = 86400 / RATIO
POPULATION = 50
MAX_FLOOR = 10
YEAR = 1

def new_day(scheduler, base_time, demand_queue):
    scheduler.enterabs(DAY_SECONDS + base_time, 1,
                    new_day, (scheduler, base_time + DAY_SECONDS, demand_queue))
    for _ in range(POPULATION):
        person = Person(randint(2, MAX_FLOOR))
        person.set_begin()
        person.set_end()
        scheduler.enterabs(person.begin / RATIO + base_time, 2, demand_queue.put, (person,))
        scheduler.enterabs(person.end / RATIO + base_time, 2, demand_queue.put, (person,))

def demand_thread(demand_queue, start_time):
    scheduler = sched.scheduler(time.time, time.sleep)
    new_day(scheduler, start_time, demand_queue)    
    scheduler.run()

def print_time(start_time):
    t = time.strftime("%b-%d %H:%M:%S", time.gmtime((time.time() - start_time) * RATIO))
    print(f"Year {YEAR} {t}")

def main():
    start_time = time.time()
    demand_queue = queue.Queue()
    demand = threading.Thread(target=demand_thread, args=(demand_queue, start_time))
    demand.start()

    while(True):
        if(not demand_queue.empty()):
            p = demand_queue.get()
            print_time(start_time)
            p.print_info()

if __name__ == "__main__":
    main()
    

