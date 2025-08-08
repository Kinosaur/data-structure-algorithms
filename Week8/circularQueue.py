class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, data):
        if self.is_full():
            print("Queue Overflow")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        data = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return data

    def front_item(self):
        if not self.is_empty():
            return self.queue[self.front]
        return None

    def rear_item(self):
        if not self.is_empty():
            return self.queue[self.rear]
        return None


# Example Usage
queue = CircularQueue(3)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.dequeue())  # Output: 10
queue.enqueue(40)
print(queue.front_item())  # Output: 20
print(queue.rear_item())  # Output: 40
