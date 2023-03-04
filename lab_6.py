def encode(password):
    password = list(password)
    for i in range(0, len(password)):
        if password[i] == '0':          #changes numbers in passcode
            password[i] = 3
        elif password[i] == '1':
            password[i] = 4
        elif password[i] == '2':
            password[i] = 5
        elif password[i] == '3':
            password[i] = 6
        elif password[i] == '4':
            password[i] = 7
        elif password[i] == '5':
            password[i] = 8
        elif password[i] == '6':
            password[i] = 9
        elif password[i] == '7':
            password[i] = 0
        elif password[i] == '8':
            password[i] = 1
        elif password[i] == '9':
            password[i] = 2
        else:
            pass

    password = map(str, password)
    password = "".join(password)            #joins numbers in passcode

    return password

def decode(x):
    # Made by Harrison Lucas
    num1 = ''
    for i in str(x):
        if int(i) >= 3:
            num1 += str(int(i) -3)

        elif int(i) == 2:
            num1 += '9'

        elif int(i) == 1:
            num1 += '8'

        elif int(i) == 0:
            num1 += '7'
    return num1



def menu():
    run_again = True
    while run_again:
        print('''Menu  
------------- 
1. Encode  
2. Decode  
3. Quit 
 ''')
        user_input = int(input('Please enter and option: '))

        if user_input == 1:
            user_pass = input('Please enter your password to encode: ')
            encoded_pass = encode(user_pass)
            print('Your password has benn encoded and stored!\n')

        elif user_input == 2:
            print(f'The encoded password is {encoded_pass}, and the original password is {decode(encoded_pass)}.')

        elif user_input == 3:
            break

if __name__ == '__main__':
    menu()