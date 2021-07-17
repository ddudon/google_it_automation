# def strings(phrase):
#     first = phrase[0]
#     last = phrase[-1]
#     # if first == last:
#     if phrase[0] == phrase[-1]:
#         return True
#     else:
#         return False
#
# print(strings("else"))
# print(strings("tree"))


# def first_and_last(message):
#     if message[0] == message[-1]:
#         return True
#     else:
#         return False
#
# print(first_and_last("else"))
# print(first_and_last("tree"))
# # print(first_and_last(""))

def first_and_last(message):
    if message == "" or message[0] == message[-1]:
         return True
    # elif message[0] == message[-1]:
    #     return True
    else:
        return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))