def input_error(func):
    def inner(*args, **kwargs):
        contact = args[0]
        try:
            return func(*args, **kwargs)
        except ValueError as error:
            str_error = str(error)
            if str_error == "not enough values to unpack (expected at least 1, got 0)" or str_error == "not enough values to unpack (expected 1, got 0)":
                return "❗ Enter user name"
            if str_error.startswith("not enough values to unpack (expected 2"):
                return "❗ Give me please name and phone"
            return str_error
        except KeyError:
            name = contact[0]
            return f"😳 Contact {name} doesn't exist. Please add contact first"
        except IndexError:
            return "❗ Enter user name"
    return inner

def input_error_days(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("Enter amount of days after command 'birthdays'")
            return 
    return inner
