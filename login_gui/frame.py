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
login frame for gui
"""
from tkinter import Frame, Label, Entry, IntVar, Checkbutton, Button, NORMAL, DISABLED, E

from login_gui.loader import Loader
from login_gui.user import User

HEIGHT = 1
WIDTH = 17


class LoginFrame(Frame):  # pylint: disable=too-many-ancestors
    """build frame for gui"""

    def __init__(self, master):
        super().__init__(master)
        self.__label_username = Label(self, text="Username")
        self.__label_password = Label(self, text="Password")

        self.__entry_username = Entry(self)
        self.__entry_password = Entry(self, show="*")

        self.__label_username.grid(row=0, sticky=E)
        self.__label_password.grid(row=1, sticky=E)
        self.__entry_username.grid(row=0, column=1)
        self.__entry_password.grid(row=1, column=1)

        self.__var = IntVar()
        self.__var.set(1)
        self.__checkbox = Checkbutton(self, text="Save login data (64-bit)", variable=self.__var)

        self.__checkbox.grid(columnspan=2)

        self.__loader = Loader()

        self.__login_button = Button(self, text="login", command=self.__login_click, height=HEIGHT, width=WIDTH)
        self.__load_button = Button(self, text="Load from " + self.__loader.last_date, command=self.__close,
                                    height=HEIGHT,
                                    width=WIDTH)
        self.__login_button.config(state=NORMAL)

        self.__load_button.config(state=DISABLED)
        if self.__loader.is_exist:
            self.__load_button.config(state=NORMAL)

        self.__login_button.grid(row=3, column=0)
        self.__load_button.grid(row=3, column=1)

        self.pack()

    def __login_click(self):
        User().user64 = '{}:{}'.format(self.__entry_username.get(), self.__entry_password.get())
        if self.__var.get():
            self.__loader.write(User().user64)
        self.__close()

    def __close(self):
        self.master.destroy()
