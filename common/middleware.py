
def get_auth():
    class User:
        def __init__(self):
            self.id = "02bbd7b278b16e8757d09318aa746733"
            self.last_name = 'Manager'
            self.first_name = 'System'
            self.email = 'manager@system.gmail.com'

    class DummyAuth:
        def __init__(self):
            self.user = User()

    return DummyAuth()
