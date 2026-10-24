from playwright.sync_api import APIRequestContext, APIResponse


class CommentsApi:
    def __init__(self, api_context: APIRequestContext):
        self.api_context = api_context

    def get_comment(self, comment_id: int) -> APIResponse:
        return self.api_context.get(
            f"/comments/{comment_id}"
        )
