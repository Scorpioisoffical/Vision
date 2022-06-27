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

# defining the token class
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
    
    # to go to the next token/letter in somesort of code
    def advance(self):
        self.pos += 1
        if(self.pos < len(self.text)):
            self.curr_char = self.text[self.pos] 
        else:
            return None
            # self.curr_char = self.text[self.pos] if self.pos < len(self.text) else None 
    
    # makes all the tokens and returns them to an list
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
            
        return tokens

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


