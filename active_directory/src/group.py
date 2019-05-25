class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

class MembershipFinder:
    def __init__(self, groups):
        self.groups = groups
        self.stack = []
        for g in self.groups:
            self.stack.append((g, '/' + g.get_name()))
        self.user_group_map = {}
        self.traverse()

    def traverse(self):
        while len(self.stack) > 0:
            grp, path = self.stack.pop()
            for u in grp.get_users():
                for p in path.split('/')[1:]:
                    self.user_group_map[u + ',' + p] = True
            for g in grp.get_groups():
                self.stack.append((g, path + '/' + g.get_name()))

    def is_user_in_group(self, user, group):
        """
        Return True if user is in the group, False otherwise.

        Args:
          user(str): user name/id
          group(class:Group): group to check user membership against
        """
        return self.user_group_map.get(user + ',' + group.get_name(), None) is not None

if __name__ == '__main__':


    groups = [Group("Group-%s" % str(i + 1)) for i in range(0, 3)]
    groups[0].add_group(groups[1])
    groups[1].add_group(groups[2])
    groups[0].add_user('user_1')
    groups[2].add_user('user_2')

    membership_finder = MembershipFinder(groups)
    print(membership_finder.is_user_in_group('user_2', groups[0]))
    print(membership_finder.is_user_in_group('user_1', groups[2]))

