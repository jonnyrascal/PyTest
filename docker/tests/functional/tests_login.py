""""""

import pytest

from tests.constants.constants import AdminUser, JackUser
from tests.application.application import API


@pytest.fixture()
def application():
    return API()


@pytest.fixture(autouse=True)
def run_around_test(application):
    print('login')
    application.login_user(user=AdminUser.user, password=AdminUser.password)
    yield
    print('logout')
    response = application.logout_user(user=AdminUser.user,
                                       token=application.token)
    print(response.json()['content'])


def test():
    assert True
    print('hello')


def test_reset_all(application):
    """Reset to initial state"""
    response = application.reset_all()
    assert response.json()["content"]


def test_login(application):
    """Positive testing login and logout as admin"""
    # login as admin
    response = application.login_user(user=AdminUser.user,
                                      password=AdminUser.password)
    assert response.status_code == 200
    assert len(application.token) == 32

    # display user name
    response = application.get_user_name(token=application.token)
    assert response.json()['content'] == "admin"

    # logout as admin
    response = application.logout_user(user=AdminUser.user,
                                       token=application.token)
    assert response.json()['content']


def test_login_negative(application):
    """Negative testing login as admin"""
    response = application.login_user(user=AdminUser.user, password='123')
    #assert response.json()['content']
    assert len(application.token) == 32


def test_get_token(application):
    """Testing token length"""
    application.login_user(user='admin', password='qwerty')
    assert len(application.token) == 32


def test_change_password(application):
    """Testing of changing user password"""

    response = application.login_user(user=AdminUser.user,
                                      password=AdminUser.password)
    response = application.change_password(token=application.token,
                                           oldPassword='qwerty',
                                           newPassword='qwerty2')
    assert response.json()['content']

    # login as admin with new password
    response = application.login_user(user='admin', password='qwerty2')
    #assert response.status_code == 200
    assert len(application.token) == 32

def test_user_jack(application):
    """Creating user Jack, login Jack, logout Jack, delete Jack"""
    createUser = application.create_new_user(token=application.token,
                                             name='Jack', password='qwerty',
                                             adminRights=False)
    assert createUser.status_code == 200
    assert createUser.json()['content']

    # login as Jack and check Jack's token length
    application.login_user_Jack(user=JackUser.user, password=JackUser.password)
    assert len(application.token) == 32

    # logout as user Jack
    response = application.logout_Jack(user=JackUser.user,
                                       token=application.token)
    assert response.json()['content']

    # login as admin
    response = application.login_user(user=AdminUser.user,
                                      password=AdminUser.password)
    assert response.status_code == 200

    # delete user Jack as admin
    response = application.delete_user(token=application.token, user='Jack')
    assert response.json()['content']

    # after deleting user Jack, try to log as Jack
    response = application.login_user_Jack(user=JackUser.user,
                                           password=JackUser.password)
    assert response.json()['content'] == 'ERROR, user not found'


def test_users_list(application):
    """Testing user list"""
    response = application.get_users_list(token=application.token)
    assert 'admin' in response.json()['content']


def test_check_admins_list(application):
    """Display list of admins"""
    response = application.check_admins_list(token=application.token)
    assert '0 \tadmin\n' in response.json()['content']


def test_logged_admins_list(application):
    """Displays list of logged admins"""
    response = application.logged_admins_list(token=application.token)
    assert "admin" in response.json()['content']


def test_locked_admins_list(application):
    """Displays list of locked admins"""
    response = application.logged_admins_list(token=application.token)
    assert "" in response.json()['content']


def test_logged_users_list(application):
    """Displays list of logged users"""
    response = application.logged_users_list(token=application.token)
    assert "admin" in response.json()['content']
    assert response.status_code == 200


def test_logged_tokens(application):
    """Displays list of logged tokens"""
    application.logged_tockens(token=application.token)
    assert len(application.token) >= 36


def test_to_lock_user(application):
    """Lock user Jack, unlock user Jack"""
    response = application.login_user(user='admin', password='qwerty')
    assert response.status_code == 200
    assert len(application.token) >= 32

    # create user Jack
    createUser = application.create_new_user(token=application.token,
                                             name='Jack', password='qwerty',
                                             adminRights=False)
    assert createUser.status_code == 200
    assert createUser.json()['content']

    # lock user Jack
    response = application.to_lock_user(token=application.token, name='Jack')
    assert response.json()['content']

    # display locked user list
    response = application.locked_users_list(token=application.token)
    assert response.json()["content"] == "0 \tJack\n"

    # login as admin
    application.login_user(user='admin', password='qwerty')

    # unlock user Jack
    response = application.unlock_user(token=application.token,
                                       name=JackUser.user)
    assert response.json()["content"]

    # login user Jack
    application.login_user_Jack(user=JackUser.user, password=JackUser.password)
    assert len(application.token) == 32


def test_unlock_all_users(application):
    """Unlock all locked users"""
    response = application.unlock_all_users(token=application.token)
    assert response.json()["content"]


def test_user_item_list(application):
    """Show user item and item's index"""

    # add user item
    response = application.add_user_item(token=application.token,
                                         item='door', index='1')
    assert response.json()['content']

    # update user item
    response = application.update_item(token=application.token,
                                       item='table', index='1')
    assert response.json()['content']

    # display user items list
    response = application.user_item_list(token=application.token,
                                          name='admin', index='1')
    assert response.json()['content'] == '1 \ttable\n'

    # delete user item by item's index
    response = application.delete_item(token=application.token, index='1')
    assert response.json()['content']

    # display user item's list
    response = application.user_item_list(token=application.token,
                                          name='admin', index='1')
    assert response.json()['content'] == ''


def test_get_all_items_list(application):
    """Add user item and display all items"""
    # add user item 'door'
    response = application.add_user_item(token=application.token,
                                         item='door', index='1')
    assert response.json()['content']

    # display all user item
    response = application.get_all_items_list(token=application.token)
    assert response.json()['content'] == '1 \tdoor\n'


def test_all_items_indexes(application):
    """Display all item's indexes"""
    response = application.all_items_indexes(token=application.token)
    assert response.json()['content'] == '1 '
