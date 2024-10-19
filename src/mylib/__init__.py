def my_sub_print(mstring: str) -> None:
    """Even more pointless subfunction"""
    print(mstring)

def my_print(mstring: str) -> None:
    """Pointless subfunction"""
    my_sub_print(mstring)
    return

def make_fullname(forename: str, surname: str) -> str:
    """Makes a full name from first and surname"""
    full_name = forename + " " + surname
    return full_name

def say_hello(forename: str, surname: str) -> None:
    """Says hello to the full name"""
    full_name = make_fullname(forename, surname)
    my_print(f"Hello, {full_name}!")
    return