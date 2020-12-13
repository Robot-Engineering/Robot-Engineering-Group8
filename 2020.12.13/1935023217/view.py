import document


class View:

    def __init__(self, entity):
        assert isinstance(entity, document.Document)
        self.document = entity

    def show(self):
        self.document.show()




