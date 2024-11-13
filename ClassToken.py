class Token():
    def __init__(self, Tstring: str, lexema: str, numLinhas: int):
        self.Tstring = Tstring, 
        self.lexema = lexema, 
        self.numLinhas = numLinhas 

    def __str__(self):
        st = f"{str(self.lexema)}\n {str(self.Tstring)}\n {str(self.numLinhas)}"

        return st
    
    def __eq__(self, value):
        if type(value) == str: 
            if self.Tstring == value: 
                return True
            else: 
                return False
            
        #if type(value) == Token():
        #    if self.Tstring == value.lexema:
        #        return True
        #    else: 
        #        return False
    