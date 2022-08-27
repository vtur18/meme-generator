from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Consume a pdf file."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = f'./tmp/{random.randint(0,100000)}.txt'
        call = subprocess.call(['pdftotext', '-layout', path, tmp])
        quotes = []
        with open(tmp, "r", encoding='utf-8-sig') as file_ref:
            lines = file_ref.readlines()
            for line in lines:
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split(' - ')
                    new_quote = QuoteModel(parse[0], parse[-1])
                    quotes.append(new_quote)
        file_ref.close()
        os.remove(tmp)
        return quotes
