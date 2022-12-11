import threading
import time
import random

class Philosopher(threading.Thread):
    def __init__(self, number, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.number = number
        self.left_fork = left_fork
        self.right_fork = right_fork

    def try_to_eat(self):
        fork1, fork2 = self.left_fork, self.right_fork
        while True:
            fork1.acquire()
            locked = fork2.acquire(False)
            if locked: break
            fork1.release()
            print('Philosopher %s swaps forks.' % self.number)
            fork1, fork2 = fork2, fork1
        else:
            return
        print('Philosopher %s is eating.' % self.number)
        time.sleep(1)
        print('Philosopher %s stop eating.' % self.number)
        fork2.release()
        fork1.release()

    def run(self):
        while True:
            print('Philosopher %s try eat.' % self.number)
            time.sleep(random.randint(1, 2))
            self.try_to_eat()

def main():
    forks = [threading.Condition(threading.Lock()) for idx in range(5)]
    philosophers = [Philosopher(idx, forks[idx], forks[(idx + 1) % 5]) for idx in range(5)]

    for philo in philosophers:
        philo.start()

if __name__ == '__main__':
    main()