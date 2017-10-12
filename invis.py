guess = input("Guess a number: ")
secret = input("Secret number: ")

# Makes each digit into a string; puts them in a list
secret_digit_list = list(str(secret))
guess_digit_list = list(str(guess))

# Compares the digits of `secret` and `guess  !!! NOT WORKING !!!

if int(secret_digit_list[1]) == int(guess_digit_list[1]):
    print("The second digits are the same.")

else:
    print("The second digits are different.")