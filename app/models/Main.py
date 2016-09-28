from system.core.model import *
import re
class Main(Model):
    def __init__(self):
        super(Main, self).__init__()
    def register(self, info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        if not info['first_name']:
            errors.append('Name cannot be blank')
        elif len(info['first_name']) < 2:
            errors.append('Name must be at least 2 characters long')
        if not info['last_name']:
            errors.append('Name cannot be blank')
        elif len(info['last_name']) < 2:
            errors.append('Name must be at least 2 characters long')
        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid!')
        if not info['password']:
            errors.append('Password cannot be blank')
        elif len(info['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif info['password'] != info['pw_confirmation']:
            errors.append('Password and confirmation must match!')
        if not info['zipcode']:
            errors.append('zipcode cannot be blank')
        elif len(info['zipcode']) != 5 :
            errors.append('Must be valid zipcode')
        # zip_str = info['zipcode']                                         #mysterious bug doesnt like that elif
        # elif (zip_str).isdigit() = False :
        #     errors.append('Must be valid zipcode')
        if errors:
            return {"status": False, "errors": errors}
        else:
            hashed_pw = self.bcrypt.generate_password_hash(info['password'])
            get_user_query = "INSERT INTO users (first_name, last_name, email, password, zipcode) VALUES(:first_name, :last_name, :email, :password, zipcode)"
            data = { 
                'first_name' : info['first_name'],
                'last_name' : info['last_name'],
                'email' : info['email'],
                'password' : info['password'],
                'zipcode' : info['zipcode']
            }
            users = self.db.query_db(get_user_query, data)
            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_user_query)
            return { "status": True, "user": users[0] }

    def login_user(self, info):
        password = info['password']
        user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        user_data = {'email': info['email']}
        user = self.db.get_one(user_query, user_data)
        if user:
            if self.bcrypt.check_password_hash(user.password, password):
                get_user_query = 'SELECT * FROM users WHERE email = :email LIMIT 1'
                user_data = {'email': info['email']}
                users = self.db.query_db(get_user_query, user_data)
                print 'user'
                print user
                return { "status": True, "user": user }
        return { "status": False }