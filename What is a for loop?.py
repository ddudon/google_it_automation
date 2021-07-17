def greeting(friends):
    for friend in friends:
        if friend != "Misha":
            print("Hello, " + friend)
        else:
            print("Dear " + friend + ", you are the devil!")


friends = ['Vitalii', 'Misha', 'Bohdan', 'Yurii']
greeting(friends)
greeting(['Alex', 'Rostik', 'Anton'])

# values = [32, 23, 57, 64, 72]
# sum = 0
# lenght = 0
# for value in values:
#     sum += value
#     lenght += 1
# print("Total sum = " + str(sum) + " Average = " + str(sum/lenght))
