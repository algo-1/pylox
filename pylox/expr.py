from abc import ABC

from pylox.token import Token


class Expr(ABC):
    pass


class Binary(Expr):

    def __init__(self, left: Expr, operator: Token, right: Expr):    
        self.left = left
        self.operator = operator
        self.right = right


class Grouping(Expr):

    def __init__(self, exprerssion: Expr):    
        self.exprerssion = exprerssion


class Literal(Expr):

    def __init__(self, value: object):    
        self.value = value


class Unary(Expr):

    def __init__(self, operator: Token, right: Expr):    
        self.operator = operator
        self.right = right
