from functools import wraps

import time

"""
Use `pytest -s` to print statements in the code
"""

def parameterised_time_int(verbose=False):
    def time_it(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            if verbose:
                print(f"Function {func.__name__} has started executing\n")
            ret = func(*args, **kwargs)
            if verbose:
                print(f"Function {func.__name__} has finished executing\n")
            end_time = time.perf_counter()
            diff = end_time - start_time
            print(f"Finished {func.__name__} in {diff:.4f} secs")
            return ret
        return wrapper
    return time_it


def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        ret = func(*args, **kwargs)
        end_time = time.perf_counter()
        diff = end_time - start_time
        print(f"Finished {func.__name__} in {diff:.4f} secs")
        return ret
    return wrapper

def recursive_sum(num: int, times: int):
    result = 0
    for _ in range(times):
        result += num
    return result

@time_it
def decorated_recursive_function(num: int, times: int):
    return recursive_sum(num=num, times=times)

@parameterised_time_int(verbose=True)
def decorated_parameterized_function(num: int, times: int):
    return recursive_sum(num=num, times=times)


def test_normal_function():
    assert recursive_sum(num=1, times=100) == 100, "Something went wrong"

def test_decorated_function():
    assert decorated_recursive_function(num=1, times=100_000_000), "Something went wrong"

def test_decorated_parameterised_function():
    assert decorated_parameterized_function(num=1, times=100_000_000), "Something went wrong"
