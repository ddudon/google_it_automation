# x = 1
# while x < 10:
#     print("Not yet - x = " + str(x))
#     x += 1
# print("x = " + str(x))


def attempts(count):
    x = 1
    while x < count:
        print("Attempt #" + str(x))
        x += 1
    print("Done!")


attempts(10)