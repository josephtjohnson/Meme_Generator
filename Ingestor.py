import DocxIngestor
import CSVIngestor
import TxtIngestor
import PDFIngestor
from IngestorInterface import Ingestor
import QuoteModel
from typing import List


class Ingestor(Ingestor):
    ingestors = ['DocxIngestor', 'CSVIngestor', 'TxtIngestor', 'PDFIngestor']

    @classmethod
    def parse(cls, path: str) -> List:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
            else:
                return print('File type not supported.')
