class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def close(self):
        print("API client closed")

    def get_user(self, user_id):
        return {"id": user_id, "name": "John"}
