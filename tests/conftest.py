import pytest
from playwright.sync_api import Playwright

from api.api_client import ApiClient
from api.comments_api import CommentsApi
from api.database import Database
from api.file_manager import FileManager
from api.posts_api import PostsApi
from api.user_service import UsersService
from api.users_api import UsersApi
from pages.login_page import LoginPage


@pytest.fixture
def logged_in_page(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    return page


@pytest.fixture
def api_request_context(playwright: Playwright):
    context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com")
    yield context
    context.dispose()


@pytest.fixture
def users_api(api_request_context):
    return UsersApi(api_request_context)


@pytest.fixture
def posts_api(api_request_context):
    return PostsApi(api_request_context)


@pytest.fixture
def comments_api(api_request_context):
    return CommentsApi(api_request_context)


@pytest.fixture
def database():
    db = Database()
    db.connect()
    yield db
    db.close()


@pytest.fixture
def file_manager():
    fm = FileManager()
    fm.open()
    yield fm
    fm.close()


@pytest.fixture
def api_client():
    api_client_context = ApiClient(base_url="https://example.com")
    yield api_client_context
    api_client_context.close()


@pytest.fixture
def user_service(api_client):
    return UsersService(api_client)
