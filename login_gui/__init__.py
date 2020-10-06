#    _________             .__
#   /   _____/____    _____|  |__ _____
#   \_____  \\__  \  /  ___/  |  \\__  \
#   /        \/ __ \_\___ \|   Y  \/ __ \_
#  /_______  (____  /____  >___|  (____  /
#          \/     \/     \/     \/     \/
#    _________       _____  __
#   /   _____/ _____/ ____\/  |_
#   \_____  \ /  _ \   __\\   __\
#   /        (  <_> )  |   |  |
#  /_______  /\____/|__|   |__|
#          \/
#  Copyright (c) 2020.

"""
login module build gui
"""
from tkinter import Tk

from login_gui.frame import LoginFrame
from login_gui.user import User

__all__ = ['LoginGui', 'User']


class LoginGui:
    """main window"""
    __root = None

    def __init__(self, root=None):
        if root is None or not isinstance(root, Tk):
            self.root = Tk(className=" Jira login")
            self.__center_window()
            self.root.mainloop()
        else:
            LoginFrame(self.root)


    @property
    def root(self):
        """root Tk window"""
        return self.__root

    @root.setter
    def root(self, value):
        if isinstance(value, Tk):
            self.__root = value
            return
        raise Exception('no Tk is value')

    def __center_window(self, wight=300, height=100):
        """create standard issue"""
        # get screen width and height
        wight_screen = self.root.winfo_screenwidth()
        height_screen = self.root.winfo_screenheight()
        # calculate position x, y
        x = (wight_screen / 2) - (wight / 2)  # pylint: disable=invalid-name
        y = (height_screen / 2) - (height / 2)  # pylint: disable=invalid-name
        self.root.geometry('%dx%d+%d+%d' % (wight, height, x, y))
