
class Localhost:
    def __init__(self, local ='http://localhost:8080', login='/login', logout='/logout'):
        self.logout = logout
        self.local = local
        self.login = login

    def log_in(self):
        return self.local + self.login

    def log_out(self):
        return self.local + self.logout

endPointLogin = Localhost()
endPointLogout = Localhost()

print(endPointLogin.log_in())
print(endPointLogout.log_out())









