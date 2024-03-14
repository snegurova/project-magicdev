def input_error_address(func):
    """decorator for exceptions"""

    def inner(*args, **kwargs):
        contact = args[0]
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name please."
        except KeyError:
            name = contact[0]
            return f"Contact {name} doesn't exist. Please add contact first"
        except IndexError:
            return "Enter user name"

    return inner
