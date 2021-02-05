from sections import PersonalInfo, Story
from abc import ABCMeta, abstractmethod


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.create_sections()

    @abstractmethod
    def create_sections(self):
        pass

    def get_sections(self):
        return self.sections

    def add_section(self, section):
        self.sections.append(section)



class Twitter(Profile):
    def create_sections(self):
        self.add_section(PersonalInfo())
        self.add_section(Story())
