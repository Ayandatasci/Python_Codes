def deco(func):
    def inner_deco():
        print("Start")
        result = func()
        print(result)
        print("End")
    return inner_deco

@deco
def test():
    return 6+7

test()
