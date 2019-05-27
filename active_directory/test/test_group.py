import unittest
from group import Group, MembershipFinder


class TestMembershipFinder(unittest.TestCase):
    # Tests the following scenario
    # group-1 ---> user-1
    #   |--------> user-2
    #   |--------> group-2
    #   |--------> group-3
    def test_membership_finder_when_all_users_belong_to_top_group(self):
        group_1 = Group('group-1')
        group_2 = Group('group-2')
        group_3 = Group('group-3')
        group_1.add_group(group_2)
        group_1.add_group(group_3)
        group_1.add_user('user-1')
        group_1.add_user('user-2')
        membership_finder = MembershipFinder([group_1, group_2, group_3], ['user-1', 'user-2'])
        # user-1 belongs to group-1. Expected return value from membership finder is True
        # Assert that it is true
        self.assertTrue(membership_finder.is_user_in_group('user-1', group_1))
        # user-1 does not belong to group-2. Expected return value from membership finder is False
        # Assert that it is false
        self.assertFalse(membership_finder.is_user_in_group('user-1', group_2))
        # user-1 does not belong  to group-3. Expected return value from membership finder is False
        # Assert that it is false
        self.assertFalse(membership_finder.is_user_in_group('user-1', group_3))

    # Tests the following scenario
    # group-1 ---> group-4 ---> group-5
    #               |---------> group-6
    #   |--------> group-2
    #   |--------> group-3
    def test_membership_finder_when_no_groups_contain_any_user(self):
        group_1 = Group('group-1')
        group_2 = Group('group-2')
        group_3 = Group('group-3')
        group_4 = Group('group-4')
        group_5 = Group('group-5')
        group_6 = Group('group-6')
        group_1.add_group(group_2)
        group_1.add_group(group_3)
        group_1.add_group(group_4)
        group_4.add_group(group_5)
        group_4.add_group(group_6)

        membership_finder = MembershipFinder([group_1, group_2, group_3, group_4, group_5, group_6], [])
        # user-1 does not belongs to group-1. Expected return value from membership finder is False
        # Assert that it is false
        self.assertFalse(membership_finder.is_user_in_group('user-1', group_1))
        # user-1 does not belong to group-3. Expected return value from membership finder is False
        # Assert that it is false
        self.assertFalse(membership_finder.is_user_in_group('user-1', group_3))
        # user-1 does not belong  to group-5. Expected return value from membership finder is False
        # Assert that it is false
        self.assertFalse(membership_finder.is_user_in_group('user-1', group_5))

    # Tests the following scenario
    # group-1 ---> group-2 ---> group-9 ----> user-5
    #                 |-------> group-10 ---> user-6
    #   |--------> group-3 ---> group-5
    #                 |-------> group-6 ----> group-7 ----> user-1
    #                                            |--------> user-2
    #                             |---------> group-8 ----> user-3
    #                                            | -------> user-4
    #   |--------> group-4 ---> user-7
    # Here user-1 be;ongs to multiple groups (group-10, group-7)
    # It will also get membership of (group-1, group-2, group-3, group-6) because of transitive dependency

    def test_membership_finder_for_transitive_membership(self):
        group_1 = Group("group-1")
        group_2 = Group("group-2")
        group_3 = Group("group-3")
        group_4 = Group("group-4")
        group_5 = Group("group-5")
        group_6 = Group("group-6")
        group_7 = Group("group-7")
        group_8 = Group("group-8")
        group_9 = Group("group-9")
        group_10 = Group("group-10")
        group_1.add_group(group_2)
        group_1.add_group(group_3)
        group_1.add_group(group_4)
        group_2.add_group(group_9)
        group_2.add_group(group_10)
        group_9.add_user('user-5')
        group_10.add_user('user-6')
        group_7.add_user('user-1')
        group_7.add_user('user-2')
        group_8.add_user('user-3')
        group_8.add_user('user-4')
        group_4.add_user('user-7')

        membership_finder = MembershipFinder(
            [group_1, group_2, group_3, group_4, group_5, group_6, group_7, group_8, group_9, group_10],
            ['user-1', 'user-2', 'user-3', 'user-4', 'user-5', 'user-6', 'user-7']
        )
        # Confirm user-5 belongs to group-9
        self.assertTrue(membership_finder.is_user_in_group('user-5', group_9))
        # Confirm user-5 belongs to group-2 because of transitivenes
        self.assertTrue(membership_finder.is_user_in_group('user-5', group_2))
        # Confirm user-5 belongs to group-1 because of transitivenes
        self.assertTrue(membership_finder.is_user_in_group('user-5', group_1))
        # Confirm user-5 does not belong to group-10 because of transitivenes
        self.assertFalse(membership_finder.is_user_in_group('user-5', group_10))
        self.assertFalse(membership_finder.is_user_in_group('user-3', group_3))