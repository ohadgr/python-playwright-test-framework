from playwright.sync_api import APIRequestContext, APIResponse


class UsersApi:
    def __init__(self, api_context: APIRequestContext):
        self.api_context = api_context

    def get_user(self, user_id: int) -> APIResponse:
        return self.api_context.get(
            f"/users/{user_id}"
        )
