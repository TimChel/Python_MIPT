#Доработать связный список из предыдущих занятий, снабдив его
#возможностью сохранять данные в бинарный файл и восстанавливать из сохранения.
import pickle


class ListIterator:
    def __init__(self, list):
        self._curr_pointer = list._start_pointer

    def __next__(self):
        if self._curr_pointer is None:
            raise StopIteration()
        curr_pointer = self._curr_pointer
        self._curr_pointer = curr_pointer.get_next()
        return curr_pointer.get_value()


class Node:
    def __init__(self, value,
                 prev_pointer=None, next_pointer=None):
        self.set_value(value)
        self.set_prev(prev_pointer)
        self.set_next(next_pointer)

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next_pointer

    def get_prev(self):
        return self._prev_pointer

    def set_value(self, value):
        self._value = value

    def set_prev(self, prev_pointer):
        self._prev_pointer = prev_pointer

    def set_next(self, next_pointer):
        self._next_pointer = next_pointer

    def __str__(self):
        return str(self.get_value())

class List:
    def __init__(self, valuelist = []):
        self._start_pointer = None
        self._finish_pointer = None
        self._length = 0
        for i in valuelist:
            self.append(i)

    def __len__(self):
        return self._length

    def append(self, value):
        if self._length == 0:
            self._start_pointer = Node(value)
            self._finish_pointer = self._start_pointer
            self._length = 1
        else:
            self._finish_pointer.set_next(Node(value, self._finish_pointer))
            self._finish_pointer = self._finish_pointer.get_next()
            self._length += 1

    def pop(self, ind):
        if ind == 0:
            self._start_pointer = self._start_pointer.get_next()
            self._start_pointer.set_prev(None)
            self._length -= 1
            return

        if ind == len(self) - 1:
            self._finish_pointer = self._finish_pointer.get_prev()
            self._finish_pointer.set_next(None)
            self._length -= 1
            return

        if ind < len(self) / 2:
            curr_pointer = self._start_pointer
            for j in range(ind):
                curr_pointer = curr_pointer.get_next()
            curr_pointer.get_prev().set_next(curr_pointer.get_next())
            curr_pointer.get_next().set_prev(curr_pointer.get_prev())
            self._length -= 1
            return


        curr_pointer = self._finish_pointer
        for j in range(len(self) - ind - 1):
            curr_pointer = curr_pointer.get_prev()
        curr_pointer.get_prev().set_next(curr_pointer.get_next())
        curr_pointer.get_next().set_prev(curr_pointer.get_prev())
        self._length -= 1
        return

    def __getitem__(self, i):
        if i < 0 or i >= self._length:
            return False

        if i < len(self) / 2:
            curr_pointer = self._start_pointer
            for j in range(i):
                curr_pointer = curr_pointer.get_next()
            return curr_pointer.get_value()

        curr_pointer = self._finish_pointer
        for j in range(len(self) - i - 1):
            curr_pointer = curr_pointer.get_prev()
        return curr_pointer.get_value()

    def __str__(self):
        arr = []
        for i in self:
            arr.append(str(i))
        return "[" + ", ".join(arr) + "]"

    def __add__(self, other):
        if isinstance(other, List):
            B = List()
            for i in self:
                B.append(i)
            for i in other:
                B.append(i)
            return B

    def __radd__(self, other):
        if isinstance(other, List):
            B = List()
            for i in other:
                B.append(i)
            for i in self:
                B.append(i)
            return B

    def __iter__(self):
        return ListIterator(self)

    def save(self):
        with open("pickle_data.bin", mode="wb") as f:
            pickle.dump(self.__dict__, f)

    def loading(self):
        with open("pickle_data.bin", mode="rb") as f:
            self.__dict__ = pickle.load(f)


A = List([35, 40, 62, 41, 111, 25, 61, 7345, 246])
C = List([2895, 235, 523, 52, 135, 52])
A.pop(8)
A.append(254)
Q = List()
B = List([348, 3984, 93844, 23])
print(A)
print(B)
print(C)
print(A+B)
print(Q+A)
print(C+A)

p = A
p.save()

a = List()
a.loading()

print(type(a), a)