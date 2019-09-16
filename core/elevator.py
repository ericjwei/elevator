import time
import sched
import threading
import queue

from random import randint
from person import Person
from control_system import control_system
from constants import RATIO, DAY_SECONDS, POPULATION, MAX_FLOOR, YEAR

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

    control_system(demand_queue)

if __name__ == "__main__":
    main()
    

