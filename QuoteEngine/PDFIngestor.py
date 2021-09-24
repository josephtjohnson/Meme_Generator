import subprocess
import os
import random
from typing import List
from .IngestorInterface import Ingestor
from .QuoteModel import QuoteModel


class PDFIngestor(Ingestor):
    file_types = ['pdf']

    @classmethod
    def line_parse(cls, path: str) -> List:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest this file type. {path}')

        tmp = f'./tmp{random.randint(1,1000)}.txt'
        subprocess.call(['pdftotext', path, tmp])

        if tmp is not None:
            file = open(tmp, 'r')
        else:
            raise Exception('file empty')

        lines = []
        for line in file.readlines():
            line = line.strip('\n\r').strip()
            lines.append(line)

        file.close()
        os.remove(tmp)
        return lines

    @staticmethod
    def parse(path, lines):
        quotes = []
        for line in lines:
            if len(line) > 0:
                parsed = line.split(',')
                new_quote = QuoteModel(path, str(parsed[0]), str(parsed[1]))
                quotes.append(new_quote)
        return quotes
