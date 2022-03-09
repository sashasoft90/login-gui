class User(object):
    passclass User(object):
    pass# login_gui
It is a Gui Package. In the gui you can specify the user with password. There is a possibility to save the entered data. This is stored in the User Data section of Windows. The class is a singleton and returns the last entered data with every call in the process.

Example code:
```python
from login_gui import MainGui, User

if __name__ == '__main__':
    functions = [
        "test function",
        "test function 1",
        "test function 2",
    ]
    print(MainGui(functions, 'My Gui').result)
>>> [1,0,1]
    print(MainGui([], 'My Gui').result)
>>> None
    print(str(User().decode()))
>>> 'user:password'
functions = [
        (True, "test function 0"),
        (False, "test function 1"),
        (True, "test function 2"),
    ]

    print(MainGui(functions, 'My Gui').result)
>>> 'user:password'
```
Example Video:

![Dome](https://github.com/sashasoft90/login-gui/blob/master/image/demo.gif)

### Development environment

1. you need [python 3.8.5](https://www.python.org/downloads/release/python-385/)
1. if you don't have python in windows environment variable, you must add to python absolut path
1. start CMD in you repo path
1. build venv folder with environment python for development `python -m venv venv`
1. activate python with `venv\Scripts\activate.bat`
1. upgrade pip to new version `python -m pip install --upgrade pip`
1. install all package for development `pip install -r requirements.txt`
1.

### Tools for Development 

1. For working with python scripts you can use [PyCharm](https://www.jetbrains.com/de-de/pycharm/download/#section=windows)
1. For edit of other files you can use [NotePad++](https://notepad-plus-plus.org/downloads/)

### PyCharm plugins

1. As code analyzer [PyLint](https://plugins.jetbrains.com/plugin/11084-pylint)
