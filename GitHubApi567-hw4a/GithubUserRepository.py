# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:22:31 2025

I Pledge my Honor that I have abided by the Stevens Honor System. - Edmund Yuen
    
@author: eyuen
"""
import requests
import json

def get_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    
    if response.status_code != 200:
        return None
    
    return response.json()

def get_commits(username, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}/commits"
    response = requests.get(url)
    
    if response.status_code != 200:
        return None
    
    return len(response.json())

def fetch_repos_and_commits(username):
    repos = get_repositories(username)
    
    if not repos:
        return "User not found."
    
    result = []
    
    for repo in repos:
        repo_name = repo['name']
        commits = get_commits(username, repo_name)
        if commits is not None:
            result.append(f"Repo: {repo_name} Commits: {commits}")
        else:
            result.append(f"Repo: {repo_name} - Could not retrieve commits")
    return result
