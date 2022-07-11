import time


class CyclicIterator:
    def __init__(self, list_el):
        self.list_el = list(list_el)
        self.obj = 0

    def __iter__(self):
        self.i = self.list_el[self.obj]
        return self

    def __next__(self):
        each_el = self.i
        if self.obj < len(self.list_el) - 1:
            self.obj += 1
            self.i = self.list_el[self.obj]
        elif self.obj == len(self.list_el) - 1:
            self.obj = 0
            self.i = self.list_el[self.obj]
        return each_el


if __name__ == "__main__":
    list_cycle = [1, 2, 3]
    tuple_cycle = (4, 5, 6)
    set_cycle = {7, 8, 9}
    range_cycle = range(10, 13)
    cyclic_iterator = CyclicIterator([list_cycle, tuple_cycle, set_cycle, range_cycle])
    for el in cyclic_iterator:
        for j in el:
            time.sleep(0.5)
            print(j)
