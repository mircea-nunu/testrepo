from re import X


def multiply(x, y):
    """Return the product of two numbers x and y."""
    product = x * y
    return product

def run_function():
    num = multiply(2, 4)
    print(num)

def loops():
    n=1
    while n<5:
        print(n)
        n=n+1
def positive_number():
    num = float(input("Enter a positive number: "))
    while num<=0:
        print("That's not a positive number!")
        num = float(input("Enter a positive number: "))
    print(f'The number is {num}')

def letters():
    for letter in 'Python':
        print(letter)

def split_amount():
    amount = float(input("Enter an amount: "))
    for num_people in range(2, 6):
        print(f"{num_people} people: ${amount / num_people:,.2f} each")

def nested_loop():
    for n in range(1, 4):
        for j in range(4, 7):
            print(f"n = {n} and j = {j}")
def range_loop():
    print('For Loop')
    for n in range(2, 10):
        print(n)
    n = 2
    print('While Loop')
    while n<10:
        
        print(n)
        n=n+1
def double_range(n):
    double_n = n*2
    return double_n

def double_3_times():
    x=1
    y =float(input("Enter a number: "))
    while x<=3:
        y=double_range(y)
        print(y)
        x=x+1

if __name__ == '__main__':
    double_3_times()