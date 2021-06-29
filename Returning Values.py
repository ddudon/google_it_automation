def triangle_area(base, height):
    return (base * height) / 2


area1 = triangle_area(5, 4)
area2 = triangle_area(7, 3)
sum1 = area1 + area2
print("The sum of two areas is:", sum1)
print("The sum of two areas is: " + str(sum1))


# Use the get_seconds function to work out the amount of seconds in 2 hours and 30 minutes,
# then add this number to the amount of seconds in 45 minutes and 15 seconds. Then print the result.
def get_seconds(hours, minutes, seconds):
    return 3600*hours + 60*minutes + seconds


amount_a = get_seconds(2, 30, 0)
amount_b = get_seconds(0, 45, 15)
result = amount_a + amount_b
print(result)


def convert_seconds(seconds_amount):
    hours = seconds_amount // 3600
    minutes = (seconds_amount - (hours * 3600)) // 60
    seconds = (seconds_amount - (hours * 3600) - (minutes * 60))
    return hours, minutes, seconds


hours, minutes, seconds = convert_seconds(5000)
print(str(hours) + ":" + str(minutes) + ":" + str(seconds))
# print(convert_seconds(3987))
