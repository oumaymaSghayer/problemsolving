from time import sleep
# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.


def dosomething():
    print("doing something")


def schedule(f, delay_in_ms):
    delay_in_s = delay_in_ms/1000
    sleep(delay_in_s)
    f()


schedule(dosomething, 10000)  # in 10 sec
