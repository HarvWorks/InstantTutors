"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

routes['default_controller'] = 'Main'
routes['POST']['/register'] = 'Main#register'
routes['POST']['/login'] = 'Main#login'
routes['POST']['/process'] = 'Main#process'
routes['GET']['/logout'] = 'Main#logout'

routes['GET']['/success'] = 'Main#success'			#FOR DEBUG PURPOSES ONLY!!!!!!!!!!!!!


# routes['GET']['/home'] = 'Profile#home'
# routes['GET']['/calander'] = 'Profile#calender'
# routes['GET']['/contact'] = 'Profile#contact'
# routes['GET']['/find'] = 'Profile#find'
# routes['GET']['/pupil'] = 'Profile#pupil'


# routes['GET']['/tutor'] = 'appointment#tutor'
# routes['GET']['/tutor/<user_id>'] = 'appointment#showprofile'
# routes['GET']['/tutor/order'] = 'appointment#acceptFriend'
# routes['GET']['/chat'] = 'appointment#chat'
# routes['GET']['/tutor/<tutor_id>/review'] = 'appointment#review'
# routes['GET']['/tutor/<tutor_id>/calender'] = 'appointment#calender'
# routes['GET']['/tutor/<tutor_id>/review/add'] = 'appointment#add_review'
# routes['GET']['/tutor/<tutor_id>/review/post'] = 'appointment#post'
# routes['GET']['/tutor/<tutor_id>/hire'] = 'appointment#hire'
# routes['GET']['/tutor/<tutor_id>/map'] = 'appointment#map'
# routes['GET']['/tutor/<tutor_id>/order'] = 'appointment#order'
# routes['GET']['/tutor/<tutor_id>/appoint'] = 'appointment#appoint'
