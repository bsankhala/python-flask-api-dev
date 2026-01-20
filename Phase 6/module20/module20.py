
class Iterator:
    def __init__(self, start, limit):
        self.current = start
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration


def even(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i


start = 3
limit = 10

print("Iterator Output:")
for num in Iterator(start, limit):
    print(num, end=" ")

print("\n\nGenerator Output (Even Numbers):")
for even in even(limit):
    print(even, end=" ")
