#################
# TOKENS
#################

#Defining Token Types
TT_INT = "TT_INT"
TT_FLOAT = "FLOAT"
TT_PLUS = "PLUS"
TT_MINUS = "MINUS"
TT_MUL = "MUL"
TT_DIV = "DIV"
TT_LPAREN = "LPAREN"
TT_RPAREN = "RPAREN"
DIG = [0,1,2,3,4,5,6,7,8,9]

class Error:
    def __init__(self,error_name,details):
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f"{self.error_name}:{self.details}"
        return result

class illegal_Char_Error(Error):
    def __init__(self,details):
        super().__init__("Illegal Character",details)

# Defining the Token Class
class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

# Lexer
class lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.curr_char = None
        self.advance()
    
    # To go to the next token/letter in somesort of code
    def advance(self):
        self.pos += 1
        if(self.pos < len(self.text)):
            self.curr_char = self.text[self.pos] 
        else:
            return None
    
    # Makes all the tokens and returns them to an list
    def make_tokens(self):
        tokens = []

        while self.curr_char != None:
            if self.curr_char in ' \t':
                self.advance()

            elif self.curr_char == "+":
                tokens.append(Token(TT_PLUS))
           
            elif self.curr_char == "-":
                tokens.append(Token(TT_MINUS))
                self.advance()
            
            elif self.curr_char == "/":
                tokens.append(Token(TT_DIV))
                self.advance()
           
            elif self.curr_char == "*":
                tokens.append(Token(TT_MUL))
                self.advance()
           
            elif self.curr_char == "(":
                tokens.append(Token(TT_LPAREN))
                self.advance()

            elif self.curr_char == ")":
                tokens.append(Token(TT_RPAREN))
                self.advance()

            else:
                char = self.current_char
                self.advance()
                return [],illegal_Char_Error("'" + char + "'")
            
        return tokens,None

def make_digits(self):
    num_str = "" #Keeping track of numbers in string form
    dot_count = 0 #Keeping count of Dots

    while self.current_char != None and self.current_char in DIG + ".":
        if self.current_char == "." :
            if dot_count == 1:
                break
            dot_count += 1
            num_str += "."
        else:
            num_str += self.current_char

    if dot_count == 0:
        return Token(TT_INT,int(num_str))
    else:
        return Token(TT_FLOAT,float(num_str))


