from system.core.controller import *
class Main(Controller):
    def __init__(self, action):
        super(Main, self).__init__(action)
        print 'Note that we have to load the model before using it in the methods below'
        self.load_model('Main')
    
    def index(self):
        return self.load_view('Main/index.html')

    def login(self):

        user_info = {
            "email" : request.form['email'],
            "password" : request.form['password']
        }
        login_status = self.models['Main'].login_user(user_info)

        if login_status['status'] == True:
            print 'loging in'
            print str(login_status['user']['id'])
            print str(login_status['user']['first_name'])
            print str(login_status['user']['last_name'])
            session['id'] = login_status['user']['id'] 
            session['first_name'] = login_status['user']['first_name']
            session['last_name'] = login_status['user']['last_name']
            url = '/home/'+session['id']
            return redirect(url)
        else:
            message = 'Incorrect password/email combination'
            flash(message)
            return self.load_view('Main/index.html')

    # def success(self):                                                  #this will be home
    #     print 'success page loding'
    #     return self.load_view('Main/success.html')

    print 'method to display registration page'

    def register(self):                                                  
        return self.load_view('Main/new.html')

    print 'method to create a user'
    def process(self):
        print 'gather data posted to our create method and format it to pass it to the model'
        user_info = {
             "first_name" : request.form['first_name'],
             "last_name" : request.form['last_name'],
             "email" : request.form['email'],
             "password" : request.form['password'],
             "pw_confirmation" : request.form['pw_confirmation'],
             "zipcode" : request.form['zipcode']
        }
        print 'call create_user method from model and write some logic based on the returned value'
        print 'notice how we passed the user_info to our model method'
        create_status = self.models['Main'].register(user_info)
        if create_status['status'] == True:
            print 'the user should have been created in the model'
            print 'we can set the newly-created users id and name to session'
            session['id'] = create_status['user']['id'] 
            session['first_name'] = create_status['user']['first_name']
            session['last_name'] = create_status['user']['last_name']
            print 'we can redirect to the users profile page here'
            url = '/home/'+session['id']
            return redirect(url)
        else:
            print 'set flashed error messages here from the error messages we returned from the Model'
            for message in create_status['errors']:
                flash(message, 'regis_errors')
            print 'redirect to the method that renders the form'
            return self.load_view('Main/new.html')

    def logout(self):
        print "start logout"
        user_info = {
            session['id'] : '',
             sesion["first_name"] : '',
             sesion["last_name"] : '',
             sesion["email"] : '',
             sesion["password"] : '',
             sesion["pw_confirmation"] : ''
        }
        return redirect('/index')
