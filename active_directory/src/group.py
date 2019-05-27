
"""
Class to implement entity: group
Users or other groups can belong to a group
"""
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = [] # list storing the groups that belong to this group
        self.users = []  # list of users who are part of this group

    # Method to add a group to a parent group
    def add_group(self, group):
        self.groups.append(group)

    # Method to add user to a group
    def add_user(self, user):
        self.users.append(user)

    # Method that returns list of groups
    def get_groups(self):
        return self.groups

    # Method that returns list of users
    def get_users(self):
        return self.users

    # Returns the name of the group
    def get_name(self):
        return self.name

"""
Class that forms the data structure so that membership can be checked efficiently
The initialization 
"""

class MembershipFinder:
    def __init__(self, groups, users):
        # Dictionary that maps user or group to an integer number (id)
        object_id_map = {}
        # Dictionary that maps id (see above) to object (user or group)
        id_object_map = {}
        # Final dictionary to map user to the group or groups that it belongs to
        # If user: u belongs to group g1 & group g2 then this dictionary will look like
        # user_group_map[u,g1] = True and user_group_map[u,g2] = True
        self.user_group_map = {}
        data = [i for i in range(0, len(groups) + len(users))]
        for g in groups:
            index = len(object_id_map)
            object_id_map[g] = index
            id_object_map[index] = g
        for u in users:
            index = len(object_id_map)
            object_id_map[u] = index
            id_object_map[index] = u
        # Implement union algorithm without path compression
        for g in groups:
            for s in g.get_groups():
                index = object_id_map[s]
                data[index] = object_id_map[g]
            for u in g.get_users():
                index = object_id_map[u]
                data[index] = object_id_map[g]
        for u in users:
            index = object_id_map[u]
            while index != data[index]:
                self.user_group_map[u + ',' + id_object_map[data[index]].get_name()] = True
                index = data[index]

    """
    Return True if user is in the group, False otherwise.
    Args:
        user(str): user name
        group(class:Group): group to check user membership against
    """
    def is_user_in_group(self, user, group):

        return self.user_group_map.get(user + ',' + group.get_name(), None) is not None


