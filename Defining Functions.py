def greeting(name, sername):
    # print("Hello, " + name + " " + sername + "!")
    message = "Hello, " + name + " " + sername + "!"
    return message

def know_something(stranger):
    print("The name of the stranger is", stranger + "!")
    message = "The name of the stranger is", stranger + "!"
    return message

name = input("What's your name? ")
sername = input("What's your sername? ")

fullname = greeting(name, sername)
print(fullname)
# greeting(your_name, your_sername)
#
# stranger = input("Do you know something about? ")
# know_something(stranger)

# def print_seconds(hours, minutes, seconds):
#     print((hours * 3600) + (minutes * 60 ) + seconds)
#
# print_seconds(1,2,3)
