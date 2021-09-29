from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('ingestorinterface.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


class IngestorInterface(ABC):
    """
    An abstract class that will be used to determine if files can be ingested and to parse the files for quotes.
    ...
    Attributes
    ----------
    path : str
        file path
        
    Methods
    -------
    can_ingest(path):
        Receives the quote file path and returns True if it can be ingested.
    parse(path):
        Receives the quote file path and returns list of QuoteModel objects that contains the quote body and author.
    """
    
    file_types = ['txt', 'docx', 'pdf', 'csv']

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Determines if a file can be ingested and returns True or False.
        
        Parameters
        ----------
            path : str
                file path
        """      
        
        ext = path.split('.')[-1]
        logger.info(f'Can ingest? {str(ext in cls.file_types)}')
        return ext in cls.file_types

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Will be used in the classes that inherit from IngestorInterface to parse accepted files.
        
        Parameters
        ----------
            path : str
                file path
        """   
        
        pass
