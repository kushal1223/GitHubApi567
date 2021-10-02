import json
import requests

def get_repo_and_commits(ID):
    req = requests.get("https://api.github.com/users/"+ID+"/repos")
    req = req.json()

    if len(req) == 0:
        print("User has no repositories")
  
    for repo in req:
        commit = requests.get("https://api.github.com/repos/"+ID+"/"+repo['name']+"/commits")
        commit = commit.json()
        print("Repo: "+ repo['name'] + "  Number Of Commits: " + str(len(commit)))
        return True

if __name__ == "__main__":
    input = input("Enter GitHub Username: ")
    get_repo_and_commits(input)