import pandas as pd
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
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
    
    file_types = ['csv']

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
        csv = pd.read_csv(path, header=0, names=['body', 'author'])
        for index, row in csv.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)
        return quotes
