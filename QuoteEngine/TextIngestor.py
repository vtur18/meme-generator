"""Read and parse text file to load quotes."""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Consume txt files."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse text file to load quotes."""
        if not cls.can_ingest(path):
            raise Exception('Not a txt file, cannot ingest exception')

        quotes = []
        with open(path, 'r', encoding='utf-8-sig') as f:
            for line in f.readlines():
                if len(line) > 0:
                    line = line.strip('\n\r').strip()
                    parse = line.split(' - ')
                    new_quote = QuoteModel(parse[0], parse[1])
                    quotes.append(new_quote)

        return quotes
