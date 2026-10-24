class UsersService:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_user(self, user_id):
        return self.api_client.get_user(user_id)