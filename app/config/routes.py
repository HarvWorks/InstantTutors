"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

routes['default_controller'] = 'InstantTutors'
routes['GET']['/register'] = 'InstantTutors#register'
routes['GET']['/login'] = 'InstantTutors#login'
routes['POST']['/process'] = 'InstantTutors#process'
routes['GET']['/wall'] = 'InstantTutors#wall'
routes['POST']['/wall/post'] = 'InstantTutors#postWall'
routes['GET']['/logout'] = 'InstantTutors#logout'
routes['GET']['/dashboard'] = 'InstantTutors#dashboard'
routes['GET']['/profile'] = 'InstantTutors#edit'
routes['GET']['/profile/<user_id>'] = 'InstantTutors#profile'
routes['GET']['/requestfriend/<user_id>'] = 'InstantTutors#requestFriend'
routes['GET']['/acceptfriend/<user_id>'] = 'InstantTutors#acceptFriend'
routes['GET']['/unfriend/<user_id>'] = 'InstantTutors#unfriend'
routes['POST']['/process/<user_id>'] = 'InstantTutors#processUser'
routes['GET']['/message'] = 'InstantTutors#message'
routes['GET']['/message/<user_id>'] = 'InstantTutors#userMessage'
routes['POST']['/message/<user_id>/send'] = 'InstantTutors#userMessageSend'
routes['GET']['/ignore/<user_id>'] = 'InstantTutors#ignore'
routes['GET']['/cancelrequest/<user_id>'] = 'InstantTutors#cancelRequest'
routes['GET']['/newwall_json'] = 'InstantTutors#newWall_json'
routes['GET']['/grabMessages/<user_id>'] = 'InstantTutors#grabMessages'
