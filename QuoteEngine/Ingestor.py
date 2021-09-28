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
        ext = path.split('.')[-1]
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                if ext = 'docx':
                    return ingestors[0].parse(path)
                elif ext = 'txt':
                    return ingestors[1].parse(path)
                elif ext = 'pdf':
                    return ingestors[2].parse(path)
                elif ext = 'csv':
                    return ingestors[3].parse(path) 
            else:
                raise Exception(f'Unsupported file type: {ext}')
