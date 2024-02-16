def outer():
    val = 1
    def inner():
        v = val * 2
        print("Inner {}".format(v))
    val += 10
    print("Outer {}".format(val))
    return inner
