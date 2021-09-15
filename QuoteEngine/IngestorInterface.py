from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class Ingestor(ABC):
    file_types = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.rstrip('.')
        return ext in cls.file_types

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
