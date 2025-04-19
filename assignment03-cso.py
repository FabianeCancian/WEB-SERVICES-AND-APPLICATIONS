import requests
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

# Making a GET request to the to the URL to recieve the dataset
response = requests.get(url)

# Create a file named cso.json and write the content of the response into the file
f = open("cso.json", "w")
f.write(response.text)



