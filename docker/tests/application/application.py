""""""
from cgitb import text

import requests

# from test2 import data
from tests.constants.constants import AdminUser, BASEURL, Endpoints, JackUser


class API:
    """"""

    def __init__(self):
        # self.url = URL
        self.session = requests.session()
        self.token = ''
        self.content = ''

    def __del__(self):
        self.session.close()

    @staticmethod
    def _generate_url(endpoint):
        return BASEURL + endpoint

    def reset_all(self):
        """Reset to initial state"""
        resetAll = self.session.get(self._generate_url(Endpoints.resetToDefault))
        return resetAll

    def login_user(self, user, password):
        """Login as admin"""
        loginUser = self.session.post(self._generate_url(Endpoints.login), params={'name': user, 'password': password})
        self.token = r.json()['content']
        return loginUser

    def logout_user(self, user, token):
        """Login as admin"""
        logOut = self.session.post(self._generate_url(Endpoints.logout), params={'name': user, 'token': token})
        return logOut


    def create_new_user(self, token, name, password, adminRights):
        """Create new user"""
        newUser = self.session.post(self._generate_url(Endpoints.user), params={'token': token, 'name': name, 'password': password, 'adminRights': adminRights})
        return newUser


    def login_user_Jack(self, user, password):
        """Login as user named Jack"""
        user_name = self.session.post(self._generate_url(Endpoints.login), params={'name': user, 'password': password})
        self.token = user_name.json()['content']
        return user_name

    def logout_Jack(self, user, token):
        """Logout as user named Jack"""
        logout = self.session.post(self._generate_url(Endpoints.logout), params={'name': user, 'token': token})
        return logout


    def change_password(self, token, oldPassword, newPassword):
        """Change user password"""
        changePsw = self.session.post(self._generate_url(Endpoints.user), params={'token': token, 'oldPassword': oldPassword, 'newPassword': newPassword})
        #self.content = p.json()['content']
        return changePsw

    def get_user_name(self, token):
        """Display logged user name"""
        userName = self.session.get(self._generate_url(Endpoints.user), params={'token': token})
        self.content = userName.json()['content']
        return userName

    def get_users_list(self, token):
        """Display all users list"""
        usersList = self.session.get(self._generate_url(Endpoints.users), params={'token': token})
        self.content = usersList.json()['content']
        return usersList

    def delete_user(self, token, user):
        """Delete user"""
        userName = self.session.delete(self._generate_url(Endpoints.user), params={'token': token, 'name': user})
        self.token = userName.json()['content']
        return userName

    def check_admins_list(self, token):
        """Display all admins """
        adminsList = self.session.get(self._generate_url(Endpoints.admins), params={'token': token})
        return adminsList


    def logged_admins_list(self, token):
        """Display all logged admins"""
        logged_admins = self.session.get(self._generate_url(Endpoints.logged_admins), params={'token': token})
        self.token = logged_admins.json()['content']
        return logged_admins

    def locked_admins_list(self, token):
        """Display all locked admins"""
        locked_admins = self.session.get(self._generate_url(Endpoints.locked_admins), params={'token': token})
        self.token = locked_admins.json()['content']
        return locked_admins

    def logged_users_list(self, token):
        """Display all logged users"""
        logged_users = self.session.get(self._generate_url(Endpoints.logged_users), params={'token': token})
        self.token = logged_users.json()['content']
        return logged_users

    def logged_tockens(self, token):
        """Display all logged tockens list"""
        loggedTokens = self.session.get(self._generate_url(Endpoints.loging_tockens), params={'token': token})
        self.token = loggedTokens.json()['content']
        return loggedTokens

    def to_lock_user(self, token, name):
        """Lock user by name"""
        userLock = self.session.post(self._generate_url(Endpoints.lock_user + name), params={'token': token, 'name': name})
        return userLock


    def locked_users_list(self, token):
        """Displays locked user list"""
        lockedUsers = self.session.get(self._generate_url(Endpoints.locked_users), params={'token': token})
        self.token = lockedUsers.json()['content']
        return lockedUsers

    def unlock_user(self, token, name):
        """Unlock user by name"""
        unlockUser = self.session.put(self._generate_url(Endpoints.unlock_user + name), params={'token': token, 'name': name})
        return unlockUser

    def unlock_all_users(self, token):
        """Unlock all users"""
        unlockAllUsers = self.session.put(self._generate_url(Endpoints.all_users_unlock), params={'token': token})
        self.token = unlockAllUsers.json()['content']
        return unlockAllUsers

    def add_user_item(self, token, item, index):
        """Add item to user"""
        addUserItem = self.session.post(self._generate_url(Endpoints.add_user_items + index), params={'token': token, 'item': item, 'index': index})
        return addUserItem

    def user_item_list(self, token, name, index):
        """Display user items list"""
        itemList = self.session.get(self._generate_url(Endpoints.get_user_items + name), params={'token': token, 'name': name, 'index': index})
        return itemList

    def update_item(self, token, index, item):
        """Update user's item"""
        updateItem = self.session.put(self._generate_url(Endpoints.update_user_item + index), params={'token': token, 'index': index, 'item': item})
        return updateItem


    def get_all_items_list(self, token):
        """Display all items list"""
        allItems = self.session.get(self._generate_url(Endpoints.get_all_items), params={'token': token})
        self.token = allItems.json()['content']
        return allItems

    def delete_item(self, token, index):
        """Delete item by index"""
        itemDelete = self.session.delete(self._generate_url(Endpoints.delete_user_item + index), params={'token': token, 'index': index})
        self.token = itemDelete.json()['content']
        return itemDelete

    def all_items_indexes(self, token):
        """Display all items indexes"""
        itemsIndexes = self.session.get(self._generate_url(Endpoints.all_item_indexes), params={'token': token})
        #self.token = itemsIndexes.json()['content']
        return itemsIndexes