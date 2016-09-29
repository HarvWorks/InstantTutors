from system.core.controller import *
class Profile(Controller):
    def __init__(self, action):
        super(Profile, self).__init__(action)
        print 'Note that we have to load the model before using it in the methods below'
        self.load_model('Profile')
    
    def home(self, user_id):
    	user = self.models['Profile'].user_info(user_id)
        return self.load_view('Profile/home.html', user = user)

    def calender(self,user_id):
    	skype = self.models['Profile'].skype_appointments(user_id)
    	travel = self.models['Profile'].travel_appointments(user_id)
    	return self.load_view('Profile/calender.html', travel = travel, skype = skype, user_id = user_id)

