class Token():
    def __init__(self, Tstring:str, lex:str, nlinhas:int):
        self.Tstring = Tstring
        self.lex = lex 
        self.nlinhas = nlinhas

    def __str__(self):
        return f"{self.Tstring} {self.lex} {self.nlinhas}"

    def __eq__(self, value):
        if self.Tstring == value:
            return True
        else: 
            return False
        """
        if type(value) == Token:
            if self.Tstring == value.Tstring: 
                return True
            else: 
                return False
        """        
    def __repr__(self):
            return f"Tstring: '{self.Tstring}', Lexema: '{self.lex}', Linha: {self.nlinhas})"

    def to_dict(self):
        return {
            "Token": self.Tstring,
            "Lexema": self.lex,
            "Linhas": self.nlinhas
        }