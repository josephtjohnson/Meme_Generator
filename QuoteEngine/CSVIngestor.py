import pandas as pd
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(Ingestor):
    file_types = ['csv']

    @classmethod
    def parse(cls, path: str) -> List:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest this file type. {path}')

        quotes = []
        csv = pd.read_csv(path, header=0)

        for index, row in csv.iterrows:
            new_quote = QuoteModel(path, str(row['body']), str(row['author']))
            quotes.append(new_quote)

        return quotes
