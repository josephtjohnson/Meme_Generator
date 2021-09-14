from abc import ABC, abstractmethod
from typing import list

class IngestorInterface(ABC):
    file_types = []

    @classmethod
    def can_ingest(cls, path: str) -> boolean:
        ext = path.rstrip('.')
        return ext in cls.file_types

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
