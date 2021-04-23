'''
Given an integer, implement a function, called sum_of_digits(n) that calculates the sum of n's digits.
If a negative number is given, our function should work as if it was positive.
'''
def sum_of_digits(digits):

     digits = str(digits)
     list_digits = []
     idx = 0

     while idx < len(digits):
          if digits[idx] == "-":
               digit = digits[idx:idx+2]
               list_digits.append(digit)
               idx += 2
          else:
               digit = digits[idx]
               list_digits.append(digit)
               idx +=1

     sum_digits = 0

     for item in list_digits:
          sum_digits += int(item)

     return(sum_digits)

# testing the function
print(sum_of_digits(-101325132435356)) # == 42
