from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TxtIngestor(IngestorInterface):
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
    
    file_types = ['txt']

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
        with open(path, 'r', encoding='utf8') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip().split('-')
                new_quote = QuoteModel(line[0], line[1])
                quotes.append(new_quote)
        return quotes
