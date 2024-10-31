from interfaces import IDocument,IDocumentCreator
from pdf_document import PDFDocument
from text_document import TextDocument
from pdf_document_creator import PDFDocumentCreator
from text_document_creator import TextDocumentCreator

def client_code(creator: IDocumentCreator):
    
    print(creator.create_document())

if __name__ == "__main__":

    client_code(PDFDocumentCreator(PDFDocument))
    client_code(TextDocumentCreator(TextDocument))