from interfaces import IDocument


class PDFDocument(IDocument):
    def create(self):
        return "PDF документ создан."
