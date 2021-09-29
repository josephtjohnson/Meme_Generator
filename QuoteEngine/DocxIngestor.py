from docx import Document
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """
    A class that inherits from IngestorInterface and creates a list of quotes.
    ...
    Attributes
    ----------
    path : str
        file path
        
    Methods
    -------
    parse(path):
        Receives the quote file path and returns list of QuoteModel objects that contains the quote body and author.
    """
    
    file_types = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parses an accepted file and returns a list of QuoteModel objects that contains the quote body and author.
        
        Parameters
        ----------
            path : str
                file path
        """        
        
        if not cls.can_ingest(path):
            raise Exception(f'Cannot ingest {path}')
        quotes = []
        doc = Document(path)
        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(' - ')
                new_quote = QuoteModel(str(parse[0]), str(parse[1]))
                quotes.append(new_quote)
        return quotes
