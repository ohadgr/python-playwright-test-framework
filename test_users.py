import pytest


def get_user_response():
    return {
        "status_code": 200,
        "body": {
            "id": 101,
            "name": "Dana",
            "active": True,
            "roles": ["admin", "user"]
        }
    }


def test_get_user():
    response = get_user_response()

    assert response["status_code"] == 200, \
        f"Expected status 200, got {response['status_code']}"
    assert response["body"]["id"] == 101
    assert response["body"]["active"]
    assert "admin" in response["body"]["roles"]


def test_get_user_details():
    response = get_user_response()

    assert response["status_code"] == 200, \
        f"Expected status 200, got {response['status_code']}"
    assert response["body"]["name"] == "Dana"
    assert response["body"]["active"]
    assert "user" in response["body"]["roles"]


def is_adult(age):
    return age >= 18


@pytest.mark.parametrize(
    "age, expected",
    [
        (17, False),
        (18, True),
        (25, True),
    ]
)
def test_is_adult(age, expected):
    assert is_adult(age) == expected


@pytest.fixture
def user():
    return {
        "id": 101,
        "name": "Dana",
        "active": True
    }


def test_user_details(user):
    assert user["id"] == 101
    assert user["name"] == "Dana"


@pytest.fixture
def users():
    return [
        {"id": 101, "name": "Dana", "active": True},
        {"id": 102, "name": "John", "active": False},
        {"id": 103, "name": "Alice", "active": True}
    ]

def test_active_users(users):
    active_names = [user["name"] for user in users if user["active"]]
    assert active_names == ["Dana", "Alice"]


@pytest.fixture
def test_user():
    print("Creating user")
    user = {"id": 101, "name": "Dana"}
    yield user
    print("Deleting user")

def test_user_name(test_user):
    assert test_user["name"] == "Dana"
