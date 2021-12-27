def seconds_to_date_time(seconds):
    hours = seconds // 3600
    minutes = (seconds - 3600*hours) // 60
    seconds_left = (seconds - minutes*60 - hours*3600)
    return hours, minutes, seconds_left


    # print(hours + '' + minutes + '' + seconds_left)


    # print('Code ran')


#hours,minutes,seconds_left=seconds_to_date_time(7510)
#print(hours + "Hrs " + minutes + " Minutes and " + seconds_left)


print(seconds_to_date_time(710))

for i in range(0,10):
    print(i)