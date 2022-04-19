from Queue import Queue


def spin(queue, n):
    for i in range(n):
        queue.enqueue(queue.dequeue())