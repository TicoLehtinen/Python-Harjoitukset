def is_empty(arvo):
    return arvo == ""


def is_number(arvo):

    try:
        float(arvo)
        return True
    except ValueError:
        return False
