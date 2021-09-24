from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .TxtIngestor import TxtIngestor
from .PDFIngestor import PDFIngestor
from .IngestorInterface import Ingestor
from .QuoteModel import QuoteModel
from typing import List


class Ingestors(Ingestor):
    ingestors = [DocxIngestor, CSVIngestor, TxtIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                print('yes')
                print(ingestor)
                print(path)
                return ingestor.parse(path)
            else:
                return print('File type not supported.')
