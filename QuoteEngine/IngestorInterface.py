from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    file_types = ['txt', 'docx', 'pdf', 'csv']

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        if ext in cls.file_types:
            return ext in cls.file_types
        else:
            raise Exception(f'{ext} not found in{cls.file_types}.')

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
