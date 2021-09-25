import subprocess
import os
import random
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    file_type = ['pdf']

    @classmethod
    def line_parse(cls, path: str) -> List[QuoteModel]:
        if cls.can_ingest(path):

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
        else:
            raise Exception('Cannot ingest this file type. {path}')

    @staticmethod
    def parse(lines):
        quotes = []
        for line in lines:
            if len(line) > 0:
                print(line)
                parsed = line.split(',')
                print(parsed)
                new_quote = QuoteModel(str(parsed[0]), str(parsed[1]))
                quotes.append(new_quote)
        return quotes
