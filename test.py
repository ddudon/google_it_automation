# def is_power_of_two(n):
#   # Check if the number can be divided by two without a remainder
#   while n != 0 and n % 2 == 0:
#     n = n / 2
#   # If after dividing by two the number is 1, it's a power of two
#   if n == 1:
#     return True
#   return False
#
# print(is_power_of_two(1))
# print(is_power_of_two(4))

def power_of_three(n):
    while n !=0 and n % 3 == 0:
        n = n / 3
        # print(n)
    if n == 1:
        return True
    return False


print(power_of_three(27))
print(power_of_three(81))
print(power_of_three(10))
print(power_of_three(5))
