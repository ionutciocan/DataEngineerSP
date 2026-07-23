def has_permission(user, action, users, roles):
    r=users[user]
    if action in roles[r]:
        return True
    else:
        return False

def different_roles(role1,role2,roles):
    res=roles[role1].difference(roles[role2])
    return res

def intersect_roles(role1,role2,roles):
    res=roles[role1].intersection(roles[role2])
    return res

def find_permission(perm,roles):
    res=set()
    for k,v in roles.items():
        if perm in v:
            res.add(k)
    return res


def get_temp_permissions(username, temp_role):
    base_role = users[username]
    base_perms = roles[base_role]
    temp_perms = roles[temp_role]
    combined_perms = frozenset(base_perms | temp_perms)
    return combined_perms

roles = {
 'admin': {'read','write','delete','publish','manage_users'},
 'editor': {'read','write','publish'},
 'viewer': {'read'},
}
users = {'alice':'admin', 'bob':'editor', 'carol':'viewer', 'dave':'editor'}

print(has_permission('bob','read',users,roles))
print(has_permission('bob','delete',users,roles))
print(different_roles('admin','editor',roles))
print(intersect_roles('editor','viewer',roles))
print(find_permission('delete',roles))
print(get_temp_permissions('bob', 'admin'))

