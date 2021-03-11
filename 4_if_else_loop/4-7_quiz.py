i=1
#pin number 123
while i<=5:
    m=input("Type pin number: ")
    if m=='123':
        print('You are logged in now')
        break
    elif i==3:
        print('Sorry, you failed to login 3 times')
        break
    i=i+1