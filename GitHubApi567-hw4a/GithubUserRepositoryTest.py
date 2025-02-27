import unittest
from unittest.mock import patch
from GithubUserRepository import fetch_repos_and_commits

class TestGitHubApi(unittest.TestCase):
    
    @patch('requests.get')
    def test_fetch_repos_and_commits(self, mock_get):
        mock_repos_response = [
            {"name": "Repo1"},
            {"name": "Repo2"}
        ]
        
        mock_commits_response_Repo1 = [
            {"sha": "commit1"}, {"sha": "commit2"}
        ]
        mock_commits_response_Repo2 = [
            {"sha": "commit1"}
        ]
        
        mock_get.side_effect = [
            unittest.mock.Mock(status_code=200, json=lambda: mock_repos_response),
            unittest.mock.Mock(status_code=200, json=lambda: mock_commits_response_Repo1),
            unittest.mock.Mock(status_code=200, json=lambda: mock_commits_response_Repo2)
        ]
        
        result = fetch_repos_and_commits('test_user')
        
        self.assertEqual(result, [
            "Repo: Repo1 Commits: 2",
            "Repo: Repo2 Commits: 1"
        ])
        
    @patch('requests.get')
    def test_user_not_found(self, mock_get):
        mock_get.return_value = unittest.mock.Mock(status_code=404, json=lambda: {})
        
        result = fetch_repos_and_commits('invalid_user')
        self.assertEqual(result, "User not found.")

if __name__ == "__main__":
    unittest.main()