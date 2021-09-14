import subprocess
import os
import random
from typing import List
from .IngestorInterface import Ingestor
from .QuoteModel import QuoteModel

class PDFIngestor(IngestorInterface):
    file_types = ['pdf']

    @classmethod
    def line_parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            return Exception(f'Cannot ingest this file type. Please ensure \
            file extension is {file_types}')

        tmp = f'./tmp{random.randint(1,1000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])
        file = open(tmp, 'r') if tmp is not "" else raise Exception('file \
        empty')

        lines = []
        for line in file.readlines():
            line = line.strip('\n\r').strip()
            lines.append(line)

        file.close()
        os.remove(tmp)
        return lines

    @staticmethod
    def parse(lines):
        quotes = []
        for line in lines:
            if len(line) > 0:
                parsed = line.split(',')
                new_quote = QuoteModel(path, str(parsed[0]), str(parsed[1])
                quotes.append(new_quote)

        return quotes
