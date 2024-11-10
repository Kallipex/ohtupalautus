class Project:
    def __init__(self, name, description, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_content(self, content):
        return "\n - ".join(content) if len(content) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}\n"
            f"\nAuthors:\n - {self._stringify_content(self.authors)}\n"
            f"\nDependencies:\n - {self._stringify_content(self.dependencies)}\n"
            f"\nDevelopment dependencies:\n - {self._stringify_content(self.dev_dependencies)}"
        )
