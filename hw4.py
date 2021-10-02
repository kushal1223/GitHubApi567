import json
import requests

def get_repo_and_commits(ID):
    res = []
    req = requests.get("https://api.github.com/users/"+ID+"/repos")
    req = req.json()

    if len(req) == 0:
        print("User has no repositories")
        return False;
  
    for repo in req:
        commit = requests.get("https://api.github.com/repos/"+ID+"/"+repo['name']+"/commits")
        commit = commit.json()
        res.append("Repo: "+ repo['name'] + "  Number Of Commits: " + str(len(commit)))

    return res

if __name__ == "__main__":
    input = input("Enter GitHub Username: ")
    print(get_repo_and_commits(input))