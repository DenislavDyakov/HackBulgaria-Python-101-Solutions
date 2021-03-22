'''
Implement a function fact_digits(n), that takes an integer and returns the sum of the factorials of each digit of n.
For example, if n = 145, we want 1! + 4! + 5!.
'''

def factorial(number):
     if number == 0 or number == 1:
          return 1
     else:
          return number * factorial(number - 1)


def fact_digits(number):
     total = 0
     for char in str(number):
          total += factorial(int(char))
     return total

print(fact_digits(145)) # == 145
print(fact_digits(101)) # == 3
print(fact_digits(111)) # == 3
print(fact_digits(999)) # == 1088640
