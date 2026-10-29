response = {
    "status": "success",
    "data": {
        "users": [
            {
                "id": 101,
                "name": "Dana",
                "active": True,
                "profile": {
                    "country": "Israel",
                    "score": 82
                }
            },
            {
                "id": 102,
                "name": "John",
                "active": False,
                "profile": {
                    "country": "UK",
                    "score": 91
                }
            },
            {
                "id": 103,
                "name": "Alice",
                "active": True,
                "profile": {
                    "country": "Israel",
                    "score": 95
                }
            }
        ]
    }
}


def get_active_users_from_country(response, country):
    users = response["data"]["users"]
    active_users = [
        user for user in users
        if user["active"] and user["profile"]["country"] == country
    ]
    sorted_users = sorted(
        active_users,
        key=lambda user: user["profile"]["score"],
        reverse=True
    )
    return [user["name"] for user in sorted_users]

print(get_active_users_from_country(response, "Israel"))