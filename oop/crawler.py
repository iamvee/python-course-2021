import urllib.request
import re



class Website:
    def __init__(self, url):
        self.url = url
        self.text = ""

    def get_text(self):
        with urllib.request.urlopen(self.url) as req:
            self.text = req.read().decode('utf-8')

        return self.text

    def get_links(self):
        urls = re.findall(r'href="(https?://.+?)"', self.text)
        return [Website(url) for url in urls]




url = "https://python.org"
website = Website(url)
# print(website.get_text())
text = website.get_text()
list_of_websites = website.get_links()
print(list_of_websites[5].get_text())