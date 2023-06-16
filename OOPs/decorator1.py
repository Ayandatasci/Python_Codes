def upper_deco(func):
    def ori_deco():
        result= func() #calling original func
        return result.upper()
    return ori_deco

@upper_deco
def test():
    return "hello, i am ayan"

print(test())
