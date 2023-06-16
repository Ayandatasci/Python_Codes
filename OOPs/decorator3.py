import time
def timer(func):
    def timer_test():
        start= time.time()
        result= func()
        print(result)
        end= time.time()
        print(f"{end-start} sec")
    return timer_test

@timer
def test():
    for i in range(100000):
        pass
    return "Loop Completed"
test()