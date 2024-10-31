from interfaces import IDocumentCreator, IDocument
from dataclasses import dataclass

@dataclass
class PDFDocumentCreator(IDocumentCreator):

    document: IDocument

    def factory_method(self):
        return self.document()
