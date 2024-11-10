from urllib import request
from project import Project
from toml import loads

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = loads(request.urlopen(self._url).read().decode("utf-8"))["tool"]["poetry"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(content["name"], content["description"], content["authors"], content["dependencies"], content["group"]["dev"]["dependencies"])