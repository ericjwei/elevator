import time
import datetime
import sched
import threading

from random import randint
from person import Person

SPEED = .25
DAY_SECONDS = 5 #86400
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

def new_day(scheduler, populate_building, baseTime):
    scheduler.enter(DAY_SECONDS - (time.time() - baseTime), 1,
                    new_day, (scheduler, populate_building, baseTime + DAY_SECONDS))
    for _ in range(POPULATION):
        person = Person(randint(2, MAX_FLOOR))
        person.set_begin()
        person.set_end()
        occupants.append(person)  
    occupants.sort(key=lambda x: x.begin)
    print(baseTime)
    print_time()

def demand_thread():
    #populate_building()
    baseTime = START_TIME
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(DAY_SECONDS - (time.time() - baseTime), 1,
                    new_day, (scheduler, populate_building, baseTime + DAY_SECONDS))
    #for p in occupants:
    #    p.print_info()
        #scheduler.enter(p.get_begin - time.time(), 1, demand_proc())
    scheduler.run()
    
def print_time():
    t = time.strftime("%b-%d %H:%M:%S", time.gmtime(time.time() - START_TIME))
    print(f"Year {YEAR} {t}")

def main():
    global START_TIME
    START_TIME = time.time()
    print_time()
    demand = threading.Thread(target=demand_thread)
    demand.start()
    
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
    

