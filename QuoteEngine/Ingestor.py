from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .TxtIngestor import TxtIngestor
from .PDFIngestor import PDFIngestor
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class Ingestor(IngestorInterface):
    ingestors = [DocxIngestor, TxtIngestor, PDFIngestor, CSVIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        ext = path.split('.')[-1].lower()
        if not Ingestor.can_ingest(ext):
            raise Exception('Could not ingest file type')
        else:
            if ext == 'txt':
                return TxtIngestor.parse(path)
            if ext == 'docx':
                return DocxIngestor.parse(path)
            if ext == 'pdf':
                return PDFIngestor.parse(path)
            if ext == 'csv':
                return CSVIngestor.parse(path)
