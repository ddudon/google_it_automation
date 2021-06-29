def check_username_len(username):
    if len(username) < 5:
        print("The username " + username + " isn't valid it's too short!")
    else:
        print("The username " + username + " is valid!")


check_username_len("roma")
check_username_len("rdudchenko")
check_username_len("don")
check_username_len("ddudon")


def is_positive(number):
    if number > 0:
        return True
    else:
        return False


print(is_positive(-11))
print(is_positive(5))
print(is_positive(0))



def number_group(number):
    if number > 0:
        return "Positive"
    elif number == 0:
        return "Zero"
    else:
        return "Negative"


print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative