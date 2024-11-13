class Token():

    def __init__(self, lexiema, Tstring, numLinhas):
        self.lexiema = lexiema, 
        self.Tstring = Tstring, 
        self.numLinhas = numLinhas 

    def __str__(self):
        st = f"{str(self.lexiema)}\n {str(self.Tstring)}\n {str(self.numLinhas)}"

        return st
    
    def __eq__(self, value):
        if type(value) == str: 
            if self.lexiema == value: 
                return True
            else: 
                return False
            
        if type(value) == Token():
            if self.lexiema == value.lexiema:
                return True
            else: 
                return False