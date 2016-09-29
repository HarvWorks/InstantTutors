from system.core.model import *
import re
class Main(Model):
    def __init__(self):
        super(Main, self).__init__()

        def user_info(self, user_id):
        	user_query = "SELECT * FROM users WHERE id = :id LIMIT 1"
        	user_data = {'id': user_id}
        	user = self.db.get_one(user_query, user_data)
        	return user

        def skype_appointments(self, user_id):
        	user_query = "SELECT * FROM skype_appointments WHERE id = :id LIMIT 1"
        	user_data = {'id': user_id}
        	apt = self.db.get_one(user_query, user_data)
        	return apt

        def travel_appointments(self, user_id):
        	user_query = "SELECT * FROM travel_appointments WHERE id = :id LIMIT 1"
        	user_data = {'id': user_id}
        	apt = self.db.get_one(user_query, user_data)
        	return apt