def note_input_error(func):
    def inner(*args, **kwargs):
        note = args[0]
        try:
            return func(*args, **kwargs)
        except ValueError as error:
            str_error = str(error)
            if str_error == "not enough values to unpack (expected at least 1, got 0)" or str_error == "not enough values to unpack (expected 1, got 0)":
                return "Enter note title"
            if str_error.startswith("not enough values to unpack (expected 2"):
                return "Give me please note title and description"
            return str_error
        except KeyError:
            name = note[0]
            return f"Note {name} doesn't exist. Please add note first"
        except IndexError:
            return "Enter note title"
    return inner