import re
from system.core.model import Model
from system.core.controller import *

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
lowercase = re.compile("[a-z]+")
uppercase = re.compile("[A-Z]+")
number = re.compile('[0-9]+')
class InstantTutor(Model):
    def __init__(self):
        super(InstantTutor, self).__init__()
