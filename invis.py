guess = input("Guess number: ")
secret = input("Secret number: ")

# Makes each digit into a string; puts them in a list
secret_digit_list = list(str(secret))
guess_digit_list = list(str(guess))

# Compares the digits of `secret` and `guess  !!! NOT WORKING !!!
for n,(a,b) in enumerate(zip(guess_digit_list,secret_digit_list)):
    if a!=b:
        print('numbers on index {} are different'.format(n))
    else:
        print('numbers on index {} are same'.format(n))


# if int(secret_digit_list[1]) == int(guess_digit_list[1]):
#     print("The second digits are the same.")
#
# else:
#     print("The second digits are different.")