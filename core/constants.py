from datetime import timedelta

RATIO = 60 #simulation seconds per one real second
SHIFT_START = timedelta(hours=1)
SHIFT_END = timedelta(hours=16)
DAY_SECONDS = 86400 / RATIO
POPULATION = 50
MAX_FLOOR = 10
YEAR = 1
FLOOR_HEIGHT = 4.5