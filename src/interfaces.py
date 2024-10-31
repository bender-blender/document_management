from abc import abstractmethod, ABC


class IDocument(ABC):
    @abstractmethod
    def create(self):
        raise NotImplementedError()


class IDocumentCreator(ABC):
    @abstractmethod
    def factory_method(self):
        raise NotImplementedError()

    def create_document(self) -> str:
        document = self.factory_method()
        return document.create()
