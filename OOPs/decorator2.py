import time
def timer(func):
    def timer_test():
        start= time.time()
        result= func()
        print(result)
        end= time.time()
        print("Time required for the code to run is:")
        print(f"{end-start} sec")
    return timer_test

@timer
def test():
    return 90+50
test()