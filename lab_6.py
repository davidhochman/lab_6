def encode(password):
    password = list(password)
    for i in range(0, len(password)):
        if password[i] == '0':
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
    password = "".join(password)

    return password


run_again = True
if __name__ == '__main__':
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
            print('Your password has benn encoded and stored!')
            print(encoded_pass)

        elif user_input == 2:
            print(f'The encoded password is {encoded_pass}, and the original password is {decode(encoded_pass)}.')

        elif user_input == 3:
            run_again = False