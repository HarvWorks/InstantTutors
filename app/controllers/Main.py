from system.core.controller import *
import datetime
from flask_socketio import SocketIO, join_room, leave_room, emit, send
from system import socketio
import time


class Main(Controller):
    def __init__(self, action):
        super(Main, self).__init__(action)
        self.load_model('InstantTutor')

    def index(self):
        if "user" in session:
            return redirect('/wall')
        return self.load_view('index.html')

    def register(self):
        if "user" in session:
            return redirect('/wall')
        return self.load_view("register.html")

    def login(self):
        if "user" in session:
            return redirect('/wall')
        return self.load_view("login.html")
