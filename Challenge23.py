from decimal import *
class Fibonacci():
    def __init__(self, count, start):
        self.nums = []
        self.count = count
        self.start = start

    def sequence(self):
        self.nums = []
        prev = 0
        total = self.start
        for i in range(self.count):
            n_total = Decimal(prev + total)
            prev = Decimal(total)
            total = n_total
            self.nums.append(prev)
        return self.nums

while __name__ == "__main__":
    while True:
        try:
            print("Enter number of fibonacci numbers you want.")
            num = int(input(">"))
        except ValueError:
            print("You did not enter an integer value.")
            break
        try:
            print("Enter starting number")
            start = Decimal(input(">"))
        except ValueError:
            print("You did not enter a valid number.")
            break
        fib = Fibonacci(num, start)
        fibby = fib.sequence()
        for fibs in fibby:
            print(fibs)
        print("Count: {}".format(num))
        print("Reverse order y/n")
        user = input(">")
        user = user.lower()
        if user == "y":
            r_fibby = fibby[::-1]
            for r_fibs in r_fibby:
                print(r_fibs)
            print("Count: {}".format(num))
