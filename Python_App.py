import re

# from kivy.properties import Clock
from logging import root

import messagebox
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles
from kivy.uix.screenmanager import ScreenManager, Screen, ScreenManagerException
from kivymd.uix.button import MDRectangleFlatButton, MDRectangleFlatIconButton, MDIconButton, MDFloatingActionButton
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.list import MDList, TwoLineListItem
import mysql.connector
from kivy.uix.slider import Slider
from kivymd.color_definitions import colors, light_colors, text_colors, theme_colors

Window.size = (350, 600)


class Career_Clinic(MDApp):
    dialog = None
    database = mysql.connector.Connect(host="localhost", user="root", password="Shreyas@123", database="cc")
    cursor = database.cursor()
    cursor.execute("select * from sign_up")
    for i in cursor.fetchall():
        print(i[5], i[6])

    def build(self):
        # to change color theme
        self.theme_cls.primary_palette = "Orange"
        # global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("Login.kv"))
        screen_manager.add_widget(Builder.load_file("explore.kv"))
        screen_manager.add_widget(Builder.load_file("Signup.kv"))
        screen_manager.add_widget(Builder.load_file("ForgotPassword.kv"))
        screen_manager.add_widget(Builder.load_file("diploma.kv"))
        screen_manager.add_widget(Builder.load_file("ITI.kv"))
        screen_manager.add_widget(Builder.load_file("Others.kv"))
        screen_manager.add_widget(Builder.load_file("ActOthers.kv"))
        screen_manager.add_widget(Builder.load_file("AdvOthers.kv"))
        screen_manager.add_widget(Builder.load_file("AgriOthers.kv"))
        screen_manager.add_widget(Builder.load_file("science_pcm.kv"))
        screen_manager.add_widget(Builder.load_file("it_jobs.kv"))
        screen_manager.add_widget(Builder.load_file("diplomas.kv"))
        screen_manager.add_widget(Builder.load_file("after_10.kv"))
        screen_manager.add_widget(Builder.load_file("ug.kv"))
        screen_manager.add_widget(Builder.load_file("eng.kv"))
        screen_manager.add_widget(Builder.load_file("it.kv"))
        screen_manager.add_widget(Builder.load_file("yes.kv"))
        screen_manager.add_widget(Builder.load_file("pg.kv"))
        screen_manager.add_widget(Builder.load_file("class_12.kv"))

        return screen_manager

    """
    def on_start(self):
        Clock.schedule_once(self.login, 5)

    def login(self, *args):
        screen_manager.current = "login"

    def show_password(self, checkbox, value):
        if value:
            self.root.ids.password.password = True
            self.root.ids.password_text.text = "Hide password"
        else:
            self.root.ids.password_text.text = "Show password"
    """

    def send_data(self, fname, lname, dob, email, phone, username, password):
        # here is a function to send data from python to mysql
        # if re.fullmatch(self.regex, username.text):
        self.cursor.execute(
            f"insert into sign_up values('{fname.text}', '{lname.text}', '{dob.text}', '{email.text}', '{phone.text}', '{username.text}', '{password.text}')")
        self.database.commit()  # this is imp. to insert query to database
        fname.text = ""
        lname.text = ""
        dob.text = ""
        email.text = ""
        phone.text = ""
        username.text = ""
        password.text = ""

    def receive_data(self, username, password):
        # here is a function to receive data from mysql to python and validate ir with textfield text
        self.cursor.execute("select * from sign_up")
        username_list = []
        for i in self.cursor.fetchall():
            username_list.append(i[5])
        if username.text in username_list and username.text != "":
            self.cursor.execute(f"select password from sign_up where username='{username.text}'")
            for j in self.cursor:
                if password.text == j[0]:
                    messagebox.showinfo("", "You have Successfully LoggedIn!")
                    print("You have Successfully LoggedIn!")
                else:
                    messagebox.showinfo("", "Incorrect Password")
                    print("Incorrect Password")
        else:
            messagebox.showinfo("", "Incorrect Username")
            print("Incorrect Username")


if __name__ == "__main__":
    Career_Clinic().run()
