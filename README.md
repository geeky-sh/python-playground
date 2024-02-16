### This is the place where I have written:

- Concepts about the language. You can find this under `learn` folder
- Leetcode problems under `leetcode` folder
- Advent of Code 2023 Solutions under `aoc-2023` folder
- If there is any other folder, maybe it is temporary and not relevant.

## Observations


## Notes
- A function can contain `*args` and `**kwargs`. When a function is invoked by passing arguments, it divides the arugments in the list of normal and keyword arguments. `args` is a list which contains the list of normal arguments. `kwargs` is a dict containing the dict of keyword arguments. For eg. `Greet("Hola", name="Aash")`. If we had `Greet(*args, **kwargs)`, then `args` would have `["Hola"]` and `kwargs` would have `{name: "Aash"}`
- For sorting we have we `list.sort()` and `sorted`. `sorted` returns a new object and `sort` does in-place sort. Both the functions have two keyword arguments `key` and `reverse`. `key` accepts a lambda or callable which would help in sorting and `reverse` is boolean which would determine whether to sort in asc or desc order. [ref](https://docs.python.org/3/howto/sorting.html)
- Python supports multiple inheritance.
- Method resolution order. Since Python 3 and onwards, method resolution has been done using linearization algorithm. So if `DerivedClass` inherits from both `BaseClass1` and `BaseClass2` and if the derived instance calls `base_method` which is defined in both the base classes, the method resolution is done from left to right i.e. if the derived class is defined as `class DerivedClass(BaseClass1, BaseClass2):` the method defined in `BaseClass1` is invoked
- Python supports adding the `else` clause for both `for` and `while` loops. `else` is invoked only when no `break` is encountered in the loop. This is generally used in patterns where we are searching for a value in the loop (using `break`) and the value is not found.
- `__init__` method is an initializer used to initialize the attributes of the object while `__new__` is used to create the object. When an object is initlialised, order of execution is `__new__(cls, *args, **kwargs) -> __init__(self, init_val)`. `__new__` is generally used to create singleton class.
- `__repr__` vs `__str__`. `__repr__` is generally used for debugging or by developer and `__str__` is used by users. In python console, the object that we call is represented via `__repr__` and all the print statements use `__str__`
- Defining the `__call__` function in a class makes that class's instance a callable function.
- `dir` is used to list down all the methods and attributes of an object. `__mro__` gives us the list of classes which determine the order of method resolution
- Every class is an object as well. And each user-defined class's class is `type`. We can use metaclasses to create a class which can manipulate the behaviour of a class creation. [ref](https://sentry.io/answers/what-are-Python-metaclasses/#creating-and-using-a-metaclass)
- Single underscore vs Double underscore -
    - `_name` is a convention to tell someone that the name is intended as a private variable. When doing `from module import *`, `_variables` are not imported
    - `__name` is a more private variable. When instantiated it is replaced in the `__dict__` as `_MyClass__name` to prevent conflicts with subclasses
    - `__name__` is another convention used by Python to prevent name conclicts


```python
try:
    # code
except Exception1 as e:
    # handle exception 1
except Exception2 as e:
    # handle exception 2
else:
    # executed when exception is not raised. Can be used to invoke code for successful execution
finally:
    # executed irrespective of whether exception is raised or not. Can be used for certain operations like closing a file, or cleaning up etc.


"""
# usage of else block in loops
"""
def find_num(n):
    is_found = False
    seq = [1, 2, 4, 5, 6]
    for x in seq:
        if x == n:
            print("Found the no.")
            is_found = True
            break
    else:
        print("Didn't find the no.")
        is_found = False
    return is_found

"""
shallow copy vs deep copy
"""
from copy import copy, deepcopy
obj = [{"name": "aash", "surname": "dhariya"}, {"name": "raj", "surname": "patel"}]
sh = copy(obj)
sh[0]["name"] = "vinod"
print(obj[0]["name"]) # This will be vinod as the sh's objects refer to obj's objects

dc = deepcopy(obj)
dc[0]["name"] = "ashish"
print(obj[0]["name"]) # This will still be vinod as dc's objects are different from obj's objects

"""
This can also be checked by other means
"""
id(obj[0])
id(sh[0])
# both of the above statements give the same value

id(dc[0])
# the value returned above is different from the original objects

"""
Use of `__new__`
"""
class Singleton:
    __ins = None

    def __new__(cls, *args, **kwargs):
        if cls.__ins is None:
            cls.__ins = super().__new__(cls, *args, **kwargs)
        return cls.__ins

s1 = Singleton()
s2 = Singleton()

s1 is s2

"""
Use of callable function
"""
class A:
    def __init__(self, number):
        print("__init__() call")
        self.data = number
    def __str__(self):
        print("__str__() call")
        print("Number is {}".format(self.data))
    def __call__(self):
       num = 0
       print("__call__() call")
       print("Adding 10 to the value of data")
       num = self.data + 10
       return num

a = A(23)
a() # returns 33
callable(a) # returns true

class MyClass():
     def __init__(self):
        self.__superprivate = "Hello"
        self._semiprivate = ", world!"

mc = MyClass()
mc.__dict__
# {'_MyClass__superprivate': 'Hello', '_semiprivate': ', world!'}
```

## Concepts
- **Decorators** - A decorator is a design pattern that allows you to modify a function's behavior by wrapping it in another function. The outer function is called the decorator which takes the actual function as an argument and returns the modified version of it. Function parameters are passed as arguments to the inner function.
- **Iterators** - These are objects that iterate as `list`, `tuples`. With this pattern and method definition, it is possible to loop through objects. An iterator object must implement two methods `__iter__` and `__next__`, which is collectively called as the     iterator protocol. `StopIteration` Exception should be raised by `__next__` method to end the iteration.
- **Generator** - A generator is a function that returns an iterator. It uses `yield` expression to do the same. `yield` statement in a function pauses the function execution at that point and returns the value beside the `yield` statement. They are useful when we need a large sequence of values.
- **Closures** - A Python closure is a nested function that allows us to access variables of the outer function even after the outer function is closed. One caveat is that the closure variable's value is what it was at the end of the outer function and not what it was when the inner function was defined. Another caveat is that closure variables can't be modified by the inner function otherwise it will return an `UnboundLocal` error. You need to create another variable to store the modified value instead.
- **Packages and Modules** - These are used to divide code, have proper separation of concerns in the code and improve readability. Modules are files and packages are folders in Python. A folder must contain a file name `__init__.py` for Python to consider it as a package.


### Collections
#### Counter
Counter is a `dict` class for counting hashable objects
```python
a = Counter()
a["first"] # 0
a["first"] += 1
a["first"] += 1
a["first"] += 1
a["first"] # 3
a["second"] += 1
a.most_common() # [{"first": 3}]
a.elements() # ["first", "first", "first", "second"]
a.clear() # clears everything
```

## Garbage Collection
- Python employs automatic garbage collection to do memory management. Memory Management is needed in any application so that you don't overuse the memory that you get and you don't access memory that is not present. There are two types of garbage collectors:
- Reference counting garbage collector - This works by keep track of reference counts for each of the object. If the reference count becomes zero, `gc` removes that variable from the memory
- Generational garbage collector - Ref counting does not help in cyclical references. Here Ggc helps. It keeps track of 3 generation of objects. Whenever the object is created, it initially goes to 1st gen, In the next gc run, if the object survives, it goes to 2nd gen and then 3rd.
- You can disable the main garbage collection in python which is reference counting. You can however disable generational garbage collector. Instagram once disabled their generation garbage collector and their application efficiency increased by 10%. But generally it is not a good idea to disable garbage collectors
- Deallocating memory objects doesn't return memory back to the operating system.

#### ref:
- https://stackify.com/python-garbage-collection/


```python
import sys
a = 1
sys.getrefcount(a) # retuns the ref count for the object

import gc
gc.get_threshold() # returns the threshold kept for each generations
gc.collect() # runs gc manually
```

## GIL (Global Interpreter Lock)
- GIL is a lock that allows only one thread to execute Python bytecode in a multi-threaded environment
- Python threading is not useful for CPU-bound tasks because of GIL. IO-bound tasks however can benefit from it. Thus true parallelism can't be achieved in python
- It is there to reduce the complexity that comes with memory management and object access patterns in shared environment.
- We can, however, use `multiprocessing` module to achieve true parallelism since it creates separate processes instead of threads.

#### Ref:
- https://realpython.com/python-memory-management/#the-global-interpreter-lock-gil
