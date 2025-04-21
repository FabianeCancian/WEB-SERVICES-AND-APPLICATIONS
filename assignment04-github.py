from github import Github
from key import config as cfg
import requests

# Get GitHub API key from config in key.py file
apikey = cfg["gitkey"]
# Authenticate to GitHub using the access token and access the repository
g = Github(apikey)
repo = g.get_repo("FabianeCancian/test.txt")

# Get the file information for "story.txt"
fileInfo = repo.get_contents("story.txt")
# Get the direct download URL of the file
urlOfFile = fileInfo.download_url
#print (urlOfFile)

# Download the raw content of the file from GitHub
response = requests.get(urlOfFile)
contentOfFile = response.text

# Replace all instances of "Andrew" with "Fabiane"
new_content = contentOfFile.replace("Andrew", "Fabiane")

# Update the file on GitHub with the new content
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",
new_content,fileInfo.sha)
print (gitHubResponse)
