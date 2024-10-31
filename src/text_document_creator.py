from interfaces import IDocumentCreator, IDocument
from dataclasses import dataclass


@dataclass
class TextDocumentCreator(IDocumentCreator):

    document: IDocument

    def factory_method(self):
        return self.document()
