import subprocess
import os
import random
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
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
    
    file_types = ['pdf']

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

        tmp = f'./tmp{random.randint(1,1000)}.txt'
        subprocess.call(['pdftotext', '-raw', path, tmp])

        if tmp is not None:
            file = open(tmp, 'r')
        else:
            raise Exception('file empty')

        lines = []
        for line in file.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split(' - ')
                new_quote = QuoteModel(str(parsed[0]), str(parsed[1]))
                lines.append(new_quote)
        file.close()
        os.remove(tmp)
        return lines
