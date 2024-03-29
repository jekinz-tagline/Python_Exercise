def memoize(func):
    fib_cache = {}
    def check_fibbo_cache(element):
        if element not in fib_cache:
            fib_cache[element] = func(element)
        return fib_cache[element]
    return check_fibbo_cache

@memoize
def fibonacci(term_number):
    if term_number == 1:
        return 1
    elif term_number == 2:
        return 1
    else:
        return (fibonacci(term_number-1) + fibonacci(term_number-2))
nth_term = int(input("Enter Number:- "))
print(f"{nth_term} term number is:- ",fibonacci(nth_term))

# sub-question
def getSum(iterable):
    if not iterable:
        return 0
    else:
        return iterable[0] + getSum(iterable[1:])
    
numbers = [23, 44, 5, 67, 1, 1, 2, 4, 5]
print("Sum of list using recursion is :- ",getSum(numbers))