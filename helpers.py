def user_input(STRING):
    try: 
        input = raw_input
    except NameError: 
        pass
    return input(STRING)