import time
import sched
import threading
import multiprocessing

from person import Person
#from control_system import control_system
from constants import RATIO, DAY_SECONDS, POPULATION, YEAR, FLOOR_HEIGHT, MAX_FLOOR

from leetCode import Solution
from listNode import ListNode 

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
#    start_time = time.time()
#    demand_list = [ multiprocessing.Queue() for _ in range(MAX_FLOOR * 2 + 1) ]
    
    # demand_queue = queue.Queue()
    # demand = threading.Thread(target=demand_thread, args=(demand_list, start_time))
    # demand.start()

    # for i in demand_list:
    #     print(i.qsize())

    # control_system(demand_list)

    solution = Solution()

#Two Sum
    # nums = [1, 2, 3, 4, 5, 6]
    # s = solution.twoSum(nums, 7)
    # for i in s:
    #     print(i)

#Add Two Numbers
    # l1 = ListNode(9)
    # l2 = ListNode(9)
    # l2.next = ListNode(9)
    # summation = solution.addTwoNumbers(l1, l2)
    # while(summation is not None):
    #     print(summation.value)
    #     summation = summation.next

#Length of Longest Substring
    s = "hello world"
    int length = solution.lengthOfLongestSubstring(s)
    


# Baseline o(n^2), s(1)
    # previous = s[0]
    # m = 1
    # count = 1
    # for c in s[1:]:
    #   if(c is not previous):
    #     count = count + 1
    #   else:
    #     count = 1
    #   if(count > m):
    #     m = count
    #   previous = c
    #   # needs to check for duplicate in the already passed area
    # return(m)
'''
  # Using a map for constant lookup for a sliding window
  # o(n), s(m, n) where m is size of string and n is size of charset
    previous = {s[0]: 0}
    m = 1
    count = 1
    i = 0 # left window, j = right window
    for j, c in enumerate(s[1:], 1):
      if(c in previous):
        for char in s[i:(previous[c] + 1)]:
          previous.pop(char)
          count = count - 1 
          #print(char)  
          i = i + 1
      previous[c] = j
      count = count + 1
      #print(count)
      if(count > m):
        m = count
    return(m)

    # s = "abcdebag"
    # print(solution.lengthOfLongestSubstring(s))
'''
if __name__ == "__main__":
    main()
    

