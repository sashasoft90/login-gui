"""
test folder with all tests of common lib
"""
from login_gui import MainGui, User

if __name__ == '__main__':
    functions = [
        "test function",
        "test function 1",
        "test function 2",
    ]
    print(MainGui(functions, 'My Gui').result)
    print(MainGui([], 'My Gui').result)
    print(str(User().decode()))
    functions = [
        (True, "test function 0"),
        (False, "test function 1"),
        (True, "test function 2"),
    ]

    print(MainGui(functions, 'My Gui').result)
