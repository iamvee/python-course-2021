import urllib.request
import re


class Website:
    def __init__(self, url):
        self.__url = url
        self.__text = ""
        self.__links = None

    @property
    def url(self):
        return self.__url

    @property
    def text(self):
        if self.__text == "":
            with urllib.request.urlopen(self.url) as req:
                self.__text = req.read().decode('utf-8')

        return self.__text

    @property
    def links(self):
        if self.__links is None:
            urls = re.findall(r'href="(https?://.+?)"', self.text)
            self.__links = [Website(url) for url in urls]
        return self.__links

    def __repr__(self):
        return f"WEBSITE[{self.url}]"


url = "https://www.python.org/"
website = Website(url)
text = website.text
list_of_websites = website.links
# print(list_of_websites[5].text)

print(website, id(website))

website_2 = website.links[5].links[5].links[1]
print(website_2, id(website_2))
