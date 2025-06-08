class User:
    def __init__(self, username):
        self.username = username

    def verify_password(self, entered, stored):
        return entered == stored