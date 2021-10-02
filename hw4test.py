import unittest

from hw4 import get_repo_and_commits

# A known valid account name and repository
ID = 'kushal1223'


class TestHw4(unittest.TestCase):

    def test_get_repos(self):
        repos = get_repo_and_commits(ID)
        self.assertEqual(repos, True)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()