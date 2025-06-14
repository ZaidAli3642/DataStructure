from collections import deque

class QueueReverseer:
    def reverse(self,queue: deque, k):
        if k < 0 or k > len(queue):
            raise Exception("Invalid index")
        
        stack = []

        for _ in range(k):
            stack.append(queue.popleft())

        while stack:
            queue.append(stack.pop())

        for _ in range(len(queue) - k):
            queue.append(queue.popleft())
        
        return queue


q = deque([10, 20, 30, 40, 50])
queue_reverser = QueueReverseer()
queue_reverser.reverse(q, 3)

