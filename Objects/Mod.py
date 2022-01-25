class Moderator:
    Identity=None
    Username=None
    Status=None
    Timestamp=None
    def __init__(self, ID, username, status, timestamp):
        self.Identity = ID
        self.Username = username
        self.Status = status
        self.Timestamp = timestamp