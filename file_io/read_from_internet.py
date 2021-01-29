import urllib.request


with urllib.request.urlopen("https://www.python.org") as req:
    response = req.read()

print(response)


