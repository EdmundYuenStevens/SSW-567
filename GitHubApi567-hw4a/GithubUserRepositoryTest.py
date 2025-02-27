# -*- coding: utf-8 -*-
"""
Created on Tues Feb 25 23:22:31 2025

I Pledge my Honor that I have abided by the Stevens Honor System. - Edmund Yuen
    
@author: eyuen
"""
import unittest
from GithubUserRepository import fetch_repos_and_commits

class TestFetchReposAndCommits(unittest.TestCase):

    def test_valid_user(self):
        result = fetch_repos_and_commits('richkempinski')
        self.assertIn('Repo: csp', result[0])

    def test_invalid_user(self):
        result = fetch_repos_and_commits('nonexistentuser12345')
        self.assertEqual(result, "User not found.")
    
    def test_no_repos_user(self):
        result = fetch_repos_and_commits('emptyuser')
        self.assertEqual(result, "User not found.")

    def test_rate_limit_handling(self):
        result = fetch_repos_and_commits('rate_limit_test')
        self.assertEqual(result, "User not found.")

if __name__ == '__main__':
    unittest.main()
