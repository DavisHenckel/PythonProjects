def ask():
    while (True):
        try: 
            userInput = int(input("Enter an integer: "))
        except:
            print('There is an error.\nI\'m gonna ask you again')
            continue
        else:
            print(userInput ** 2)
            break
    
if __name__ == "__main__":
    for i in ['a','b','c']:
        try:
            print(i**2)
        except TypeError:
            print('There is a Type Error. We are attempting to raise {} to the 2nd power'.format(i))
        else:
            print(i**2)
    x = 5
    y = 0
    try:
        z = x/y
    except ZeroDivisionError:
        print('Cannot divide by Zero')
    finally:
        print("All done")
    ask()

