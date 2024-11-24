# MIRACLE SORT
import threading
import time


class Test:
    ARRAY = [3, 2, 1]


def miracle_sort():
    sort = False
    while not sort:
        sort = True
        for index in range(1, len(Test.ARRAY)):
            if Test.ARRAY[index] < Test.ARRAY[index -1]:
                sort = False
                continue
    return True


def sort_array():
    time.sleep(5)
    Test.ARRAY = [1, 2, 3]

thread = threading.Thread(target=sort_array)
thread.start()

print(miracle_sort())