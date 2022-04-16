from Queue import Queue


def spin(queue, n):
    for i in range(n):
        value = queue.dequeue()
        queue.enqueue(value)