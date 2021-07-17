def is_valid_user(user):
    if len(user) > 3:
        return True
    else:
        return False


def validate_users(users):
    for user in users:
        if is_valid_user(user):
            print("The username:", user, "is valid.")
        else:
            print("The username:", user, "is invalid")


validate_users(["Nick", "Rostik", "Jo", "Joe", "Anton"])
