import pandas as pd
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    file_types = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception(f'Cannot ingest {path}')
        quotes = []
        csv = pd.read_csv(path, header=0, names=['body', 'author'])
        print(csv)
        for index, row in csv.iterrows:
            new_quote = QuoteModel(str(row['body']),
                                   str(row['author']))
            quotes.append(new_quote)

        return quotes
