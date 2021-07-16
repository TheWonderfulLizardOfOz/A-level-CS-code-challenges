def times_table(*args):
    total = 1
    for arg in args:
        total = total*arg
    print(total)

def percentages(num, perc):
    perc = perc/100
    value = num*perc
    print(value)

def factorial(num):
    nums = []
    total = 1
    for i in range(num):
        nums.append(i + 1)
    for no in nums:
        total = total*no
    print(total)

while __name__ == "__main__":
    print("""1. Multiply
2. Percentages
3. Factorial
4. Quit""")
    try:
        no = int(input(">"))
    except ValueError:
        no = 5
    if no == 1:
        nums = []
        while True:
            print("Enter the numbers you want to multiply if you're done enter a letter")
            try:
                num = float(input(">"))
                nums.append(num)
            except ValueError:
                times_table(*nums)
                break
    elif no == 2:
        while True:
            try:
                num = float(input("Enter the number you would like to find the percentage of: "))
                break
            except ValueError:
                print("Please enter a valid input")
        while True:
            try:
                perc = float(input("Enter percentage you want to find: "))
                break
            except:
                print("Please enter a valid input")
        percentages(num, perc)
    elif no == 3:
        print("Enter the number you want to find the factorial of.")
        while True:
            try:
                num = int(input(">"))
                break
            except ValueError:
                print("Please enter a valid input.")
        factorial(num)
    elif no == 4:
        break
    else:
        print("Please enter a valid input")
