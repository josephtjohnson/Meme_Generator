import pandas as pd
from typing import List
from .IngestorInterface import Ingestor
from .QuoteModel import QuoteModel

class TxtIngestor(IngestorInterface):
    file_types = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            return Exception(f'Cannot ingest this file type. Please ensure \
            file extension is {file_types}')

        quotes = []
        csv = pd.read_csv(path, header=None, names=['body', 'author'])

        for index, row in csv.iterrows:
            new_quote = QuoteModel(path, str(row['body']), str(row['author']))
            quotes.append(new_quote)

        return quotes
