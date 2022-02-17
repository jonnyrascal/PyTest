"""In this file are are constants for testing"""
BASEURL = 'http://localhost:8080'


"""In this class are all endpoints for testing"""
class Endpoints:
    resetToDefault = '/reset'
    login = '/login'
    logout = '/logout'
    user = '/user'
    users = '/users'
    admins = '/admins'
    logged_admins = '/login/admins'
    locked_admins = '/locked/admins'
    logged_users = '/login/users'
    loging_tockens = '/login/tockens'
    lock_user = '/locked/user/'      # lockUser, method POST {name}
    locked_users = '/locked/users'  # getLockedUsers
    unlock_user = '/locked/user/'    # unlockUser, method PUT {name}
    names = ["Jack", "admin", "Bob", "Sam"]
    items = ["table", "chair", "door"]
    all_users_unlock = '/locked/reset'
    add_user_items = '/item/'        # add user item, method POST
    get_user_items = '/item/user/'   # {item}
    update_user_item = '/item/'
    delete_user_item = '/item/'
    get_all_items = '/items/'
    all_item_indexes = '/itemindexes'

class AdminUser:
    """This is data we are using in a tests_login file"""
    user = 'admin'
    password = 'qwerty'
    adminRights = True

class JackUser:
    """This is data we are using in a tests_login file where user's name is Jack""
    user = 'Jack'
    password = 'qwerty'
    adminRights = False
