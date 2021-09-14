import docx
from typing import List
from .IngestorInterface import Ingestor
from .QuoteModel import QuoteModel

class DocxIngestor(IngestorInterface):
    file_types = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            return Exception(f'Cannot ingest this file type. Please ensure \
            file extension is {file_types}')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                new_quote = QuoteModel(path, str(parse[0]), str(parse[1])
                quotes.append(new_quote)
                                       
        return quotes
