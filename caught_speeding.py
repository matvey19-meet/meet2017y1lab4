speed = 50
is_birthday = True

if is_birthday:
    if speed < 36:
        print('ticket')
    elif (speed > 35) and (speed < 56):
        print("small ticket")
    elif speed > 56:
        print("BIG TICKET")
    else:
        print("no ticket :)")
else:
        if speed < 31:
            print("small ticket")
        elif (speed > 30) and (speed < 51):
            print("small ticket")
        elif speed > 50:
            print("BIG TICKET")
        else:
            print("no ticket")
