class PriorityQueue:
    def __init__(self):
        self.queue = MaxHeap()

    def enqueue(self, element):
        self.queue.insert(element)

    def peek(self):
        return self.queue.get_max()

    def dequeue(self, element):
        return self.queue.extract_max()

    def is_empty(self):
        return len(self.queue.heap) == 0

    def change_priority_by_index(self, i, new):
        self.queue.update_by_index(i, new)

    def change_priority(self, old, new):
        self.queue.update(old, new)