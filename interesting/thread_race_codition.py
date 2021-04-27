import threading

from queue import Queue


class RaceObject:
    def __init__(self, attr1: int = 0, attr2: int = 0, attr3: int = 0):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3

    def change_point(self, to: 'RaceObject', attr1: int = 0, attr2: int = 0, attr3: int = 0):
        self.make_change(-attr1, -attr2, -attr3)
        to.make_change(attr1, attr2, attr3)

    def make_change(self, attr1: int, attr2: int, attr3: int):
        self.attr1 += attr1
        self.attr2 += attr2
        self.attr3 += attr3

    def __repr__(self):
        return str(self.attr1) + ", " + str(self.attr2) + ", " + str(self.attr3)


target = RaceObject(attr1=100, attr2=100, attr3=100)


class Manage(threading.Thread):
    def __init__(self):
        super().__init__(target=self.manager)
        self.obj = RaceObject(attr1=0, attr2=0, attr3=0)
        self.tasks = Queue()

    def manager(self):
        while True:
            task = self.tasks.get()
            if task == 'put':
                target.change_point(to=self.obj, attr1=5, attr2=5, attr3=5)
            elif task == 'get':
                self.obj.change_point(to=target, attr1=5, attr2=5, attr3=5)
            else:
                return


workers = [Manage() for i in range(10)]


for worker in workers:
    for i in range(100000):
        worker.tasks.put('put')
        worker.tasks.put('get')
    worker.tasks.put('shutdown')

print('Before :', target)
for worker in workers:
    worker.start()

for worker in workers:
    worker.join()
print('Result :', target)
