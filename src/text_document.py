from interfaces import IDocument


class TextDocument(IDocument):
    def create(self):
        return "Текстовый документ создан"
