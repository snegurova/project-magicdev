from .colors import magenta, yellow

def input_error_address(func):
    """decorator for exceptions"""

    def inner(*args, **kwargs):
        contact = args[0]
        try:
            return func(*args, **kwargs)
        except ValueError:
            return magenta("❗ Give me name and address please.")
        except KeyError:
            name = contact[0]
            return yellow(f"😳 Contact {name} doesn't exist. Please add contact first")
        except IndexError:
            return magenta("❗ Enter user name")

    return inner
