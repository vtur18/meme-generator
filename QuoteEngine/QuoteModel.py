"""Body and author for the quotes."""
class QuoteModel():
    """Quote model."""

    def __init__(self, body, author):
        """Variables for the quotes."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Return readable object."""
        return f'<{self.body}, {self.author}>'
