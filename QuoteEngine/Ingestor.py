from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .TxtIngestor import TxtIngestor
from .PDFIngestor import PDFIngestor
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('ingestor.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


class Ingestor(IngestorInterface):
    ingestors = [DocxIngestor, TxtIngestor, PDFIngestor, CSVIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        try:
            ext = path.split('.')[-1].lower()
        except ValueError:
            logger.exception(f'{path} is not a valid file path')
        try:
            if not Ingestor.can_ingest(ext):
                raise ValueError(f'Unsupported file type found: {ext}')
            else:
                if ext == 'txt':
                    return TxtIngestor.parse(path)
                if ext == 'docx':
                    return DocxIngestor.parse(path)
                if ext == 'pdf':
                    return PDFIngestor.parse(path)
                if ext == 'csv':
                    return CSVIngestor.parse(path)
        except Exception as e:
            logger.exception(e)
