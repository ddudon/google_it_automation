# In math, the factorial of a number is defined as the product of an integer and all the integers below it.
# For example, the factorial of four (4!) is equal to 1*2*3*4=24.
# Fill in the blanks to make the factorial function return the right number.

# def factorial(n):
#     fac = 1
#     for i in range(1, n + 1):
#         fac *= i
#     return fac
#
#
# print(factorial(4))
# print(factorial(5))
#
#
# def far_to_cel(n):
#     far = (n - 32)*5/9
#     return far
#
# for n in range(1, 101, 20):
#     print(n, far_to_cel(n))

def ip_print(n1, n2, n3, ips):
    if ips % 2 != 0:
        print("IP: " + str(n1) + "." + str(n2) + "." + str(n3) + "." + str(ips) + " is odd")
    else:
        print("IP: " + str(n1) + "." + str(n2) + "." + str(n3) + "." + str(ips) + " is even")
    return n1, n2, n3, ips


for ips in range(1, 50):
    ip_print(192, 168, 1, ips)
