class CubeIterator:
    def __init__(self, value) -> None:
        self.value = value
        self.cur_value = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur_value is None:
            self.cur_value = self.value
        elif self.cur_value > 100_000:
            raise StopIteration
        else:
            self.cur_value = self.cur_value ** 3
        return self.cur_value

def cube_iterator(val: int):
    actual_val = val
    while actual_val < 100_1000:
        yield actual_val
        actual_val = actual_val ** 3

def test_iterator():
    val = 2
    for v in CubeIterator(2):
        print(f"Value returned is {v}")
        assert v == val
        val = val ** 3

def test_generator():
    val = 2
    for v in cube_iterator(2):
        print(f"Value returned is {v}")
        assert v == val
        val = val ** 3
