users = [
    {"id": 101, "name": "Dana", "age": 32, "active": True, "roles": ["admin", "user"]},
    {"id": 102, "name": "John", "age": 27, "active": False, "roles": ["user"]},
    {"id": 103, "name": "Alice", "age": 41, "active": True, "roles": ["user", "editor"]},
    {"id": 104, "name": "Mike", "age": 35, "active": True, "roles": ["admin"]}
]

print(users[0]["name"])

for user in users:
    print(user["name"], user["age"])


for user in users:
    if user["active"]:
        print(user["name"])

def count_active_users(users):
    count = 0
    for user in users:
        if user["active"]:
            count += 1
    return count

print(count_active_users(users))

def get_active_users(users):
    active_users = []
    for user in users:
        if user["active"]:
           active_users.append(user)
    return active_users
print(get_active_users(users))

def get_active_user_names(users):
    active_user_names = []
    for user in users:
        if user["active"]:
            active_user_names.append(user["name"])
    return active_user_names

print(get_active_user_names(users))


def get_users_older_than(users, age):
    users_older = []
    for user in users:
        if user["age"] > age:
            users_older.append(user["name"])
    return users_older
print(get_users_older_than(users, 30))

def get_active_users_older_than(users, age):
    active_older_users = []
    for user in users:
        if user["active"] and user["age"] > age:
            active_older_users.append(user["name"])
    return active_older_users
print(get_active_users_older_than(users, 30))
print(get_active_users_older_than(users, 35))

# def get_users_by_role(users, role):
#     role_users = []
#     for user in users:
#         if role in user["roles"]:
#             role_users.append(user["name"])
#     return role_users
# print(get_users_by_role(users, "admin"))
# print(get_users_by_role(users, "user"))

def find_user_by_id(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None
print(find_user_by_id(users, 102))
print(find_user_by_id(users, 999))

def assert_user_exists(users, user_id):
    user = find_user_by_id(users, user_id)
    assert user is not None, f"User with id {user_id} was not found"

assert_user_exists(users, 102)
# assert_user_exists(users, 999)

users_over_30 = [user["name"] for user in users if user["age"] > 30]
print(users_over_30)

active_users_over_30 = [user["name"] for user in users if user["age"] > 30 and user["active"]]
print(active_users_over_30)

sorted_users = sorted(users, key=lambda user: user["age"], reverse=True)
sorted_names = [user["name"] for user in sorted_users]
print(sorted_names)


active_users = [user for user in users if user["active"]]
sorted_active_names = [user["name"] for user in sorted(active_users, key=lambda user: user["age"], reverse=True)]
print(sorted_active_names)

def get_active_names_sorted_by_age(users):
    active_names = [user for user in users if user["active"]]
    sorted_active_users = [user["name"] for user in
                           sorted(active_names, key=lambda user: user["age"], reverse=True)]
    return sorted_active_users
print(get_active_names_sorted_by_age(users))


def get_active_users_by_role(users, role):
    active_user = [user for user in users if user["active"]]
    role_users = [user for user in active_user if role in user["roles"]]
    sorted_active_users_by_role = [user["name"] for user in
                           sorted(role_users, key=lambda user: user["age"], reverse=True)]
    return sorted_active_users_by_role

print(get_active_users_by_role(users, "admin"))
print(get_active_users_by_role(users, "user"))

