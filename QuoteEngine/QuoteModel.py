class QuoteModel():
    """
    A class that creates a quote object.
    ...
    Attributes
    ----------
    body : str
        quote text
    author : str
        quote author
        
    Methods
    -------
    parse(path):
        Receives the quote file path and returns list of QuoteModel objects that contains the quote body and author.
    """
    
    def __init__(self, body, author):
        """
        Constructs attributes for quote object.
        
        Parameters
        ----------
            body : str
                quote text
            author : str
                quote author
        """   
        
        self.body = body
        self.author = author

    def __str__(self):
        """
        Returns __init__ parameters in a structured string representation.
        
        """   
        
        return f'{self.body} \n -{self.author}'

    def __repr__(self):
        """
        Returns __init__ parameters in string representation.
        
        """   
        
        return f'<{self.body}, {self.author}>'
