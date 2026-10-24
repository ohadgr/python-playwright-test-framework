import pytest

from nested_json import response


def test_get_user(users_api):
    response = users_api.get_user(1)
    assert response.status == 200
    data = response.json()
    assert data["id"] == 1
    assert data["username"]


def test_get_non_existing_user(users_api):
    response = users_api.get_user(99999)
    assert response.status == 404


def test_create_post(posts_api):
    post_data = {"title": "Automation Test", "body": "Created by Playwright", "userId": 1}
    response = posts_api.create_post(post_data)
    assert response.status == 201
    data = response.json()
    assert data["title"] == post_data["title"]
    assert data["body"] == post_data["body"]
    assert data["userId"] == post_data["userId"]
    assert data["id"]


def test_get_comment(comments_api):
    response = comments_api.get_comment(1)
    assert response.status == 200
    data = response.json()
    assert data["id"] == 1
    assert data["email"]


def test_file_manager(file_manager):
    assert file_manager is not None


def test_user_service(user_service):
    user = user_service.get_user(1)
    assert user["id"] == 1


@pytest.mark.parametrize("user_id", [
    999,
    99999,
    999999
])
def test_get_non_existing_user(users_api, user_id):
    response = users_api.get_user(user_id)
    assert response.status == 404

def test_update_post(posts_api):
    post_data = {"title": "Automation Test Updated", "body": "Created by Playwright", "userId": 11}
    response = posts_api.update_post(1, post_data)
    assert response.status == 200
    data = response.json()
    assert data["title"] == post_data["title"]
    assert data["body"] == post_data["body"]
    assert data["userId"] == post_data["userId"]
    assert data["id"] == 1

def test_delete_post(posts_api):
    response = posts_api.delete_post(1)
    assert response.status == 200

def test_posts_by_user(posts_api):
    response = posts_api.get_posts_by_user(2)
    assert response.status == 200
    data = response.json()
    assert data
    for post in data:
        assert post["userId"] == 2
        assert post["title"]

@pytest.mark.parametrize(
    "field, expected_type",
    [
        ("id", int),
        ("userId", int),
        ("title", str),
        ("body", str),
    ]
)
def test_post_field_types(posts_api, field, expected_type):
    response = posts_api.get_posts_by_user(2)
    assert response.status == 200

    data = response.json()
    assert data

    for post in data:
        assert isinstance(post[field], expected_type)

def test_post_schema(posts_api):
    response = posts_api.get_post(1)
    assert response.status == 200
    data = response.json()
    assert isinstance(data["id"], int)
    assert isinstance(data["userId"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)
    assert data["title"]