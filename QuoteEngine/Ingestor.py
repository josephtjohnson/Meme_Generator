from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .TxtIngestor import TxtIngestor
from .PDFIngestor import PDFIngestor
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class Ingestor(IngestorInterface):
    ingestors = (DocxIngestor, TxtIngestor, PDFIngestor, CSVIngestor)

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
            else:
                raise Exception(f'{path} cannot be ingested by {ingestor}')
