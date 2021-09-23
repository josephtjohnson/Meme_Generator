import docx
from typing import List
from IngestorInterface import Ingestor
import QuoteModel


class DocxIngestor(Ingestor):
    file_types = ['docx']

    @classmethod
    def parse(cls, path: str) -> List:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest this file type. {path}')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                new_quote = QuoteModel(path, str(parse[0]), str(parse[1]))
                quotes.append(new_quote)

        return quotes
