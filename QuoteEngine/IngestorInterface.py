from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class Ingestor(ABC):
    file_types = ['pdf', 'csv', 'txt', 'docx']

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.file_types

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List:
        pass
