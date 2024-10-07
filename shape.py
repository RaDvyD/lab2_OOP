class Shape:
    def __init__(self, name="Unknown"):
        self.name = name

    def description(self):
        return f"This is a shape called {self.name}."
