import unittest

from hw4 import get_repo_and_commits

# A known valid account name and repository
ID = 'richkempinski'


class TestHw4(unittest.TestCase):

    def test_get_repos1(self):
        repos = get_repo_and_commits(ID)
        self.assertIsInstance(repos, list)
    
    def test_get_repos2(self):
        repos = get_repo_and_commits(ID)
        test = ['Repo: csp  Number Of Commits: 2', 'Repo: hellogitworld  Number Of Commits: 30', 'Repo: helloworld  Number Of Commits: 6', 'Repo: Mocks  Number Of Commits: 10', 'Repo: Project1  Number Of Commits: 2', 'Repo: richkempinski.github.io  Number Of Commits: 9', 'Repo: threads-of-life  Number Of Commits: 1', 'Repo: try_nbdev  Number Of Commits: 2', 'Repo: try_nbdev2  Number Of Commits: 5']
        self.assertEquals(repos, test)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()