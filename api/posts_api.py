from playwright.sync_api import APIRequestContext, APIResponse


class PostsApi:
    def __init__(self, api_context: APIRequestContext):
        self.api_context = api_context

    def create_post(self, post_data) -> APIResponse:
        return self.api_context.post("/posts", data=post_data)

    def update_post(self, post_id, post_data) -> APIResponse:
        return self.api_context.put(f"/posts/{post_id}", data=post_data)

    def delete_post(self, post_id) -> APIResponse:
        return self.api_context.delete(f"/posts/{post_id}")

    def get_posts_by_user(self, user_id) -> APIResponse:
        return self.api_context.get(
            "/posts",
            params={"userId": user_id}
        )

    def get_post(self, post_id) -> APIResponse:
        return self.api_context.get(f"/posts/{post_id}")