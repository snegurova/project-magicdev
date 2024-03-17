from .colors import magenta, yellow


def input_error(func):
    def inner(*args, **kwargs):
        contact = args[0]
        try:
            return func(*args, **kwargs)
        except ValueError as error:
            str_error = str(error)
            if (
                str_error == "not enough values to unpack (expected at least 1, got 0)"
                or str_error == "not enough values to unpack (expected 1, got 0)"
            ):
                return magenta("❗ Enter user name")
            if str_error.startswith("not enough values to unpack (expected 2"):
                return magenta("❗ Give me please name and phone")
            elif str_error.startswith("not enough values to unpack (expected 3"):
                return magenta("❗ Give me please name, old phone and new phone")
            return str_error
        except KeyError:
            name = contact[0]
            return yellow(f"😳 Contact {name} doesn't exist. Please add contact first")
        except IndexError:
            return magenta("❗ Enter user name")

    return inner


def input_error_days(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print(yellow("❗ Enter amount of days after command 'birthdays'"))
            return

    return inner
