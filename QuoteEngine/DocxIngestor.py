import docx
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    file_type = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if cls.can_ingest(path):

            quotes = []
            doc = docx.Document(path)

            for para in doc.paragraphs:
                if para.text != "":
                    parse = para.text.split(' - ')
                    new_quote = QuoteModel(str(parse[0]), str(parse[1]))
                    quotes.append(new_quote)

            return quotes
        else:
            raise Exception('Cannot ingest this file type. {path}')
