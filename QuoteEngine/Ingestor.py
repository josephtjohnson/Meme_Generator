from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .TxtIngestor import TxtIngestor
from .PDFIngestor import PDFIngestor
from .IngestorInterface import Ingestor
from .QuoteModel import QuoteModel
from typing import List


class Ingestor(Ingestor):
    ingestors = ['DocxIngestor', 'CSVIngestor', 'TxtIngestor', 'PDFIngestor']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
