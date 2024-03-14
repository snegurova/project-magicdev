from .colors import magenta, yellow

def tag_input_error(func):
    def inner(*args, **kwargs):
        if len(args) < 2:
            print(magenta("❗ Give me please note title and tag"))
            return
        try:
            return func(*args, **kwargs)
        except ValueError as error:
            str_error = str(error)
            if (
                str_error == "not enough values to unpack (expected at least 1, got 0)"
                or str_error == "not enough values to unpack (expected 1, got 0)"
            ):
                print(magenta("❗ Enter note title"))
            elif str_error.startswith("not enough values to unpack (expected 2"):
                print(magenta("❗ Give me please note title and tag"))
            else:
                print(str_error)
        except KeyError:
            name = args[0]
            print(yellow(f"😳 Note {name} doesn't exist. Please add note first"))
        except IndexError:
            print(magenta("❗ Give me please note title and tag"))

    return inner
