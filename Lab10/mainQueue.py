# Author: Michael Savino
# Date: 11/22/24
# Description: Main file that uses the queue class

from Queue import Queue, EmptyQueueException

def main():
    queue = Queue()

    with open("inputQueue.txt", "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith("enqueue"):
                command, value = line.split()
                queue.enqueue(value)
                print(f"Enqueued {value}")

            elif line == "dequeue":
                try:
                    value = queue.dequeue()
                    print(f"Dequeued {value}")
                except EmptyQueueException as e:
                    print(e)

            elif line == "peek":
                try:
                    value = queue.peek()
                    print(f"Peeked at {value}")
                except EmptyQueueException as e:
                    print(e)

            elif line == "clear":
                queue.clear()
                print("Cleared out the queue.")

            else:
                print(queue)


main()