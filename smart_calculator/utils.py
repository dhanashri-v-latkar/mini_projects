def get_number(message):
    while True:
        user_input = input(message)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("invalid input")