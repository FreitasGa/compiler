# Generated from D:/Coding/python/compiler/One.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,44,191,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,5,0,44,8,0,10,0,12,0,47,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,3,1,59,8,1,1,2,1,2,1,2,1,2,3,2,65,8,2,1,3,1,3,1,3,1,
        3,1,4,1,4,1,4,1,4,3,4,75,8,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,3,5,87,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,99,8,
        7,1,7,1,7,3,7,103,8,7,1,7,1,7,3,7,107,8,7,1,7,1,7,1,7,1,8,1,8,3,
        8,114,8,8,1,9,1,9,1,10,1,10,5,10,120,8,10,10,10,12,10,123,9,10,1,
        10,1,10,1,11,1,11,1,12,1,12,1,12,5,12,132,8,12,10,12,12,12,135,9,
        12,1,13,1,13,1,13,5,13,140,8,13,10,13,12,13,143,9,13,1,14,1,14,1,
        14,5,14,148,8,14,10,14,12,14,151,9,14,1,15,1,15,1,15,5,15,156,8,
        15,10,15,12,15,159,9,15,1,16,1,16,1,16,3,16,164,8,16,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,1,17,3,17,174,8,17,1,18,1,18,1,18,1,18,1,
        18,1,18,5,18,182,8,18,10,18,12,18,185,9,18,1,19,1,19,1,20,1,20,1,
        20,0,0,21,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,0,6,1,0,8,9,1,0,10,13,1,0,2,3,1,0,4,6,2,0,2,3,7,7,1,0,31,34,196,
        0,45,1,0,0,0,2,58,1,0,0,0,4,60,1,0,0,0,6,66,1,0,0,0,8,70,1,0,0,0,
        10,79,1,0,0,0,12,88,1,0,0,0,14,94,1,0,0,0,16,111,1,0,0,0,18,115,
        1,0,0,0,20,117,1,0,0,0,22,126,1,0,0,0,24,128,1,0,0,0,26,136,1,0,
        0,0,28,144,1,0,0,0,30,152,1,0,0,0,32,163,1,0,0,0,34,173,1,0,0,0,
        36,175,1,0,0,0,38,186,1,0,0,0,40,188,1,0,0,0,42,44,3,2,1,0,43,42,
        1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,48,1,0,0,0,
        47,45,1,0,0,0,48,49,5,0,0,1,49,1,1,0,0,0,50,59,3,4,2,0,51,59,3,6,
        3,0,52,59,3,8,4,0,53,59,3,10,5,0,54,59,3,12,6,0,55,59,3,14,7,0,56,
        59,3,16,8,0,57,59,3,18,9,0,58,50,1,0,0,0,58,51,1,0,0,0,58,52,1,0,
        0,0,58,53,1,0,0,0,58,54,1,0,0,0,58,55,1,0,0,0,58,56,1,0,0,0,58,57,
        1,0,0,0,59,3,1,0,0,0,60,61,3,38,19,0,61,64,3,40,20,0,62,63,5,1,0,
        0,63,65,3,22,11,0,64,62,1,0,0,0,64,65,1,0,0,0,65,5,1,0,0,0,66,67,
        3,40,20,0,67,68,5,1,0,0,68,69,3,22,11,0,69,7,1,0,0,0,70,71,3,38,
        19,0,71,72,3,40,20,0,72,74,5,19,0,0,73,75,3,36,18,0,74,73,1,0,0,
        0,74,75,1,0,0,0,75,76,1,0,0,0,76,77,5,20,0,0,77,78,3,20,10,0,78,
        9,1,0,0,0,79,80,5,25,0,0,80,81,5,19,0,0,81,82,3,22,11,0,82,83,5,
        20,0,0,83,86,3,20,10,0,84,85,5,26,0,0,85,87,3,20,10,0,86,84,1,0,
        0,0,86,87,1,0,0,0,87,11,1,0,0,0,88,89,5,29,0,0,89,90,5,19,0,0,90,
        91,3,22,11,0,91,92,5,20,0,0,92,93,3,20,10,0,93,13,1,0,0,0,94,95,
        5,30,0,0,95,98,5,19,0,0,96,99,3,4,2,0,97,99,3,6,3,0,98,96,1,0,0,
        0,98,97,1,0,0,0,98,99,1,0,0,0,99,100,1,0,0,0,100,102,5,17,0,0,101,
        103,3,22,11,0,102,101,1,0,0,0,102,103,1,0,0,0,103,104,1,0,0,0,104,
        106,5,17,0,0,105,107,3,6,3,0,106,105,1,0,0,0,106,107,1,0,0,0,107,
        108,1,0,0,0,108,109,5,20,0,0,109,110,3,20,10,0,110,15,1,0,0,0,111,
        113,5,28,0,0,112,114,3,22,11,0,113,112,1,0,0,0,113,114,1,0,0,0,114,
        17,1,0,0,0,115,116,3,22,11,0,116,19,1,0,0,0,117,121,5,21,0,0,118,
        120,3,2,1,0,119,118,1,0,0,0,120,123,1,0,0,0,121,119,1,0,0,0,121,
        122,1,0,0,0,122,124,1,0,0,0,123,121,1,0,0,0,124,125,5,22,0,0,125,
        21,1,0,0,0,126,127,3,24,12,0,127,23,1,0,0,0,128,133,3,26,13,0,129,
        130,7,0,0,0,130,132,3,26,13,0,131,129,1,0,0,0,132,135,1,0,0,0,133,
        131,1,0,0,0,133,134,1,0,0,0,134,25,1,0,0,0,135,133,1,0,0,0,136,141,
        3,28,14,0,137,138,7,1,0,0,138,140,3,28,14,0,139,137,1,0,0,0,140,
        143,1,0,0,0,141,139,1,0,0,0,141,142,1,0,0,0,142,27,1,0,0,0,143,141,
        1,0,0,0,144,149,3,30,15,0,145,146,7,2,0,0,146,148,3,30,15,0,147,
        145,1,0,0,0,148,151,1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,
        29,1,0,0,0,151,149,1,0,0,0,152,157,3,32,16,0,153,154,7,3,0,0,154,
        156,3,32,16,0,155,153,1,0,0,0,156,159,1,0,0,0,157,155,1,0,0,0,157,
        158,1,0,0,0,158,31,1,0,0,0,159,157,1,0,0,0,160,161,7,4,0,0,161,164,
        3,32,16,0,162,164,3,34,17,0,163,160,1,0,0,0,163,162,1,0,0,0,164,
        33,1,0,0,0,165,174,5,38,0,0,166,174,5,39,0,0,167,174,5,40,0,0,168,
        174,3,40,20,0,169,170,5,19,0,0,170,171,3,22,11,0,171,172,5,20,0,
        0,172,174,1,0,0,0,173,165,1,0,0,0,173,166,1,0,0,0,173,167,1,0,0,
        0,173,168,1,0,0,0,173,169,1,0,0,0,174,35,1,0,0,0,175,176,3,38,19,
        0,176,183,3,40,20,0,177,178,5,16,0,0,178,179,3,38,19,0,179,180,3,
        40,20,0,180,182,1,0,0,0,181,177,1,0,0,0,182,185,1,0,0,0,183,181,
        1,0,0,0,183,184,1,0,0,0,184,37,1,0,0,0,185,183,1,0,0,0,186,187,7,
        5,0,0,187,39,1,0,0,0,188,189,5,41,0,0,189,41,1,0,0,0,17,45,58,64,
        74,86,98,102,106,113,121,133,141,149,157,163,173,183
    ]

class OneParser ( Parser ):

    grammarFileName = "One.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'!'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'&&'", "'||'", "','", "';'", "':'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "'if'", "'else'", "'function'", 
                     "'return'", "'while'", "'for'", "'bool'", "'int'", 
                     "'float'", "'string'", "'.'" ]

    symbolicNames = [ "<INVALID>", "Assign", "Plus", "Minus", "Asterisk", 
                      "Slash", "Percent", "Bang", "Equal", "NotEqual", "Less", 
                      "Greater", "LessEqual", "GreaterEqual", "And", "Or", 
                      "Comma", "Semicolon", "Colon", "LeftParen", "RightParen", 
                      "LeftBrace", "RightBrace", "LeftBracket", "RightBracket", 
                      "If", "Else", "Function", "Return", "While", "For", 
                      "Bool", "Int", "Float", "String", "Dot", "Whitespace", 
                      "Newline", "BoolLiteral", "NumberLiteral", "StringLiteral", 
                      "Identifier", "Digit", "Letter", "EscapeSequence" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_variable_declaration = 2
    RULE_assignment = 3
    RULE_function_declaration = 4
    RULE_if_statement = 5
    RULE_while_statement = 6
    RULE_for_statement = 7
    RULE_return_statement = 8
    RULE_expression_statement = 9
    RULE_block = 10
    RULE_expression = 11
    RULE_equality = 12
    RULE_comparison = 13
    RULE_addition = 14
    RULE_multiplication = 15
    RULE_unary = 16
    RULE_primary = 17
    RULE_parameters = 18
    RULE_type = 19
    RULE_variable_name = 20

    ruleNames =  [ "program", "statement", "variable_declaration", "assignment", 
                   "function_declaration", "if_statement", "while_statement", 
                   "for_statement", "return_statement", "expression_statement", 
                   "block", "expression", "equality", "comparison", "addition", 
                   "multiplication", "unary", "primary", "parameters", "type", 
                   "variable_name" ]

    EOF = Token.EOF
    Assign=1
    Plus=2
    Minus=3
    Asterisk=4
    Slash=5
    Percent=6
    Bang=7
    Equal=8
    NotEqual=9
    Less=10
    Greater=11
    LessEqual=12
    GreaterEqual=13
    And=14
    Or=15
    Comma=16
    Semicolon=17
    Colon=18
    LeftParen=19
    RightParen=20
    LeftBrace=21
    RightBrace=22
    LeftBracket=23
    RightBracket=24
    If=25
    Else=26
    Function=27
    Return=28
    While=29
    For=30
    Bool=31
    Int=32
    Float=33
    String=34
    Dot=35
    Whitespace=36
    Newline=37
    BoolLiteral=38
    NumberLiteral=39
    StringLiteral=40
    Identifier=41
    Digit=42
    Letter=43
    EscapeSequence=44

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(OneParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OneParser.StatementContext)
            else:
                return self.getTypedRuleContext(OneParser.StatementContext,i)


        def getRuleIndex(self):
            return OneParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = OneParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4157293985932) != 0):
                self.state = 42
                self.statement()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(OneParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(OneParser.Variable_declarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(OneParser.AssignmentContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(OneParser.Function_declarationContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(OneParser.If_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(OneParser.While_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(OneParser.For_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(OneParser.Return_statementContext,0)


        def expression_statement(self):
            return self.getTypedRuleContext(OneParser.Expression_statementContext,0)


        def getRuleIndex(self):
            return OneParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = OneParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.function_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.if_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 54
                self.while_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 55
                self.for_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 56
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 57
                self.expression_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(OneParser.TypeContext,0)


        def variable_name(self):
            return self.getTypedRuleContext(OneParser.Variable_nameContext,0)


        def Assign(self):
            return self.getToken(OneParser.Assign, 0)

        def expression(self):
            return self.getTypedRuleContext(OneParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OneParser.RULE_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declaration" ):
                listener.enterVariable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declaration" ):
                listener.exitVariable_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = OneParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variable_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.type_()
            self.state = 61
            self.variable_name()
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 62
                self.match(OneParser.Assign)
                self.state = 63
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_name(self):
            return self.getTypedRuleContext(OneParser.Variable_nameContext,0)


        def Assign(self):
            return self.getToken(OneParser.Assign, 0)

        def expression(self):
            return self.getTypedRuleContext(OneParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OneParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = OneParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.variable_name()
            self.state = 67
            self.match(OneParser.Assign)
            self.state = 68
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(OneParser.TypeContext,0)


        def variable_name(self):
            return self.getTypedRuleContext(OneParser.Variable_nameContext,0)


        def LeftParen(self):
            return self.getToken(OneParser.LeftParen, 0)

        def RightParen(self):
            return self.getToken(OneParser.RightParen, 0)

        def block(self):
            return self.getTypedRuleContext(OneParser.BlockContext,0)


        def parameters(self):
            return self.getTypedRuleContext(OneParser.ParametersContext,0)


        def getRuleIndex(self):
            return OneParser.RULE_function_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_declaration" ):
                listener.enterFunction_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_declaration" ):
                listener.exitFunction_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = OneParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.type_()
            self.state = 71
            self.variable_name()
            self.state = 72
            self.match(OneParser.LeftParen)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0):
                self.state = 73
                self.parameters()


            self.state = 76
            self.match(OneParser.RightParen)
            self.state = 77
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def If(self):
            return self.getToken(OneParser.If, 0)

        def LeftParen(self):
            return self.getToken(OneParser.LeftParen, 0)

        def expression(self):
            return self.getTypedRuleContext(OneParser.ExpressionContext,0)


        def RightParen(self):
            return self.getToken(OneParser.RightParen, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OneParser.BlockContext)
            else:
                return self.getTypedRuleContext(OneParser.BlockContext,i)


        def Else(self):
            return self.getToken(OneParser.Else, 0)

        def getRuleIndex(self):
            return OneParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = OneParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(OneParser.If)
            self.state = 80
            self.match(OneParser.LeftParen)
            self.state = 81
            self.expression()
            self.state = 82
            self.match(OneParser.RightParen)
            self.state = 83
            self.block()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 84
                self.match(OneParser.Else)
                self.state = 85
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def While(self):
            return self.getToken(OneParser.While, 0)

        def LeftParen(self):
            return self.getToken(OneParser.LeftParen, 0)

        def expression(self):
            return self.getTypedRuleContext(OneParser.ExpressionContext,0)


        def RightParen(self):
            return self.getToken(OneParser.RightParen, 0)

        def block(self):
            return self.getTypedRuleContext(OneParser.BlockContext,0)


        def getRuleIndex(self):
            return OneParser.RULE_while_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_statement" ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_statement" ):
                listener.exitWhile_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = OneParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(OneParser.While)
            self.state = 89
            self.match(OneParser.LeftParen)
            self.state = 90
            self.expression()
            self.state = 91
            self.match(OneParser.RightParen)
            self.state = 92
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def For(self):
            return self.getToken(OneParser.For, 0)

        def LeftParen(self):
            return self.getToken(OneParser.LeftParen, 0)

        def Semicolon(self, i:int=None):
            if i is None:
                return self.getTokens(OneParser.Semicolon)
            else:
                return self.getToken(OneParser.Semicolon, i)

        def RightParen(self):
            return self.getToken(OneParser.RightParen, 0)

        def block(self):
            return self.getTypedRuleContext(OneParser.BlockContext,0)


        def variable_declaration(self):
            return self.getTypedRuleContext(OneParser.Variable_declarationContext,0)


        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OneParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(OneParser.AssignmentContext,i)


        def expression(self):
            return self.getTypedRuleContext(OneParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OneParser.RULE_for_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_statement" ):
                listener.enterFor_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_statement" ):
                listener.exitFor_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = OneParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(OneParser.For)
            self.state = 95
            self.match(OneParser.LeftParen)
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31, 32, 33, 34]:
                self.state = 96
                self.variable_declaration()
                pass
            elif token in [41]:
                self.state = 97
                self.assignment()
                pass
            elif token in [17]:
                pass
            else:
                pass
            self.state = 100
            self.match(OneParser.Semicolon)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4123169128588) != 0):
                self.state = 101
                self.expression()


            self.state = 104
            self.match(OneParser.Semicolon)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 105
                self.assignment()


            self.state = 108
            self.match(OneParser.RightParen)
            self.state = 109
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Return(self):
            return self.getToken(OneParser.Return, 0)

        def expression(self):
            return self.getTypedRuleContext(OneParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OneParser.RULE_return_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_statement" ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_statement" ):
                listener.exitReturn_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = OneParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(OneParser.Return)
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 112
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(OneParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OneParser.RULE_expression_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_statement" ):
                listener.enterExpression_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_statement" ):
                listener.exitExpression_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_statement" ):
                return visitor.visitExpression_statement(self)
            else:
                return visitor.visitChildren(self)




    def expression_statement(self):

        localctx = OneParser.Expression_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expression_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LeftBrace(self):
            return self.getToken(OneParser.LeftBrace, 0)

        def RightBrace(self):
            return self.getToken(OneParser.RightBrace, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OneParser.StatementContext)
            else:
                return self.getTypedRuleContext(OneParser.StatementContext,i)


        def getRuleIndex(self):
            return OneParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = OneParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(OneParser.LeftBrace)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4157293985932) != 0):
                self.state = 118
                self.statement()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
            self.match(OneParser.RightBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality(self):
            return self.getTypedRuleContext(OneParser.EqualityContext,0)


        def getRuleIndex(self):
            return OneParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = OneParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.equality()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OneParser.ComparisonContext)
            else:
                return self.getTypedRuleContext(OneParser.ComparisonContext,i)


        def Equal(self, i:int=None):
            if i is None:
                return self.getTokens(OneParser.Equal)
            else:
                return self.getToken(OneParser.Equal, i)

        def NotEqual(self, i:int=None):
            if i is None:
                return self.getTokens(OneParser.NotEqual)
            else:
                return self.getToken(OneParser.NotEqual, i)

        def getRuleIndex(self):
            return OneParser.RULE_equality

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality" ):
                listener.enterEquality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality" ):
                listener.exitEquality(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality" ):
                return visitor.visitEquality(self)
            else:
                return visitor.visitChildren(self)




    def equality(self):

        localctx = OneParser.EqualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.comparison()
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8 or _la==9:
                self.state = 129
                _la = self._input.LA(1)
                if not(_la==8 or _la==9):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 130
                self.comparison()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OneParser.AdditionContext)
            else:
                return self.getTypedRuleContext(OneParser.AdditionContext,i)


        def Greater(self, i:int=None):
            if i is None:
                return self.getTokens(OneParser.Greater)
            else:
                return self.getToken(OneParser.Greater, i)

        def Less(self, i:int=None):
            if i is None:
                return self.getTokens(OneParser.Less)
            else:
                return self.getToken(OneParser.Less, i)

        def GreaterEqual(self, i:int=None):
            if i is None:
                return self.getTokens(OneParser.GreaterEqual)
            else:
                return self.getToken(OneParser.GreaterEqual, i)

        def LessEqual(self, i:int=None):
            if i is None:
                return self.getTokens(OneParser.LessEqual)
            else:
                return self.getToken(OneParser.LessEqual, i)

        def getRuleIndex(self):
            return OneParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = OneParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.addition()
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 15360) != 0):
                self.state = 137
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15360) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 138
                self.addition()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplication(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OneParser.MultiplicationContext)
            else:
                return self.getTypedRuleContext(OneParser.MultiplicationContext,i)


        def Plus(self, i:int=None):
            if i is None:
                return self.getTokens(OneParser.Plus)
            else:
                return self.getToken(OneParser.Plus, i)

        def Minus(self, i:int=None):
            if i is None:
                return self.getTokens(OneParser.Minus)
            else:
                return self.getToken(OneParser.Minus, i)

        def getRuleIndex(self):
            return OneParser.RULE_addition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddition" ):
                listener.enterAddition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddition" ):
                listener.exitAddition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddition" ):
                return visitor.visitAddition(self)
            else:
                return visitor.visitChildren(self)




    def addition(self):

        localctx = OneParser.AdditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_addition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.multiplication()
            self.state = 149
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 145
                    _la = self._input.LA(1)
                    if not(_la==2 or _la==3):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 146
                    self.multiplication() 
                self.state = 151
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OneParser.UnaryContext)
            else:
                return self.getTypedRuleContext(OneParser.UnaryContext,i)


        def Asterisk(self, i:int=None):
            if i is None:
                return self.getTokens(OneParser.Asterisk)
            else:
                return self.getToken(OneParser.Asterisk, i)

        def Slash(self, i:int=None):
            if i is None:
                return self.getTokens(OneParser.Slash)
            else:
                return self.getToken(OneParser.Slash, i)

        def Percent(self, i:int=None):
            if i is None:
                return self.getTokens(OneParser.Percent)
            else:
                return self.getToken(OneParser.Percent, i)

        def getRuleIndex(self):
            return OneParser.RULE_multiplication

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplication" ):
                listener.enterMultiplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplication" ):
                listener.exitMultiplication(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplication" ):
                return visitor.visitMultiplication(self)
            else:
                return visitor.visitChildren(self)




    def multiplication(self):

        localctx = OneParser.MultiplicationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_multiplication)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.unary()
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0):
                self.state = 153
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 154
                self.unary()
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(OneParser.UnaryContext,0)


        def Plus(self):
            return self.getToken(OneParser.Plus, 0)

        def Minus(self):
            return self.getToken(OneParser.Minus, 0)

        def Bang(self):
            return self.getToken(OneParser.Bang, 0)

        def primary(self):
            return self.getTypedRuleContext(OneParser.PrimaryContext,0)


        def getRuleIndex(self):
            return OneParser.RULE_unary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary" ):
                return visitor.visitUnary(self)
            else:
                return visitor.visitChildren(self)




    def unary(self):

        localctx = OneParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 140) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 161
                self.unary()
                pass
            elif token in [19, 38, 39, 40, 41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BoolLiteral(self):
            return self.getToken(OneParser.BoolLiteral, 0)

        def NumberLiteral(self):
            return self.getToken(OneParser.NumberLiteral, 0)

        def StringLiteral(self):
            return self.getToken(OneParser.StringLiteral, 0)

        def variable_name(self):
            return self.getTypedRuleContext(OneParser.Variable_nameContext,0)


        def LeftParen(self):
            return self.getToken(OneParser.LeftParen, 0)

        def expression(self):
            return self.getTypedRuleContext(OneParser.ExpressionContext,0)


        def RightParen(self):
            return self.getToken(OneParser.RightParen, 0)

        def getRuleIndex(self):
            return OneParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = OneParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_primary)
        try:
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.match(OneParser.BoolLiteral)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(OneParser.NumberLiteral)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 3)
                self.state = 167
                self.match(OneParser.StringLiteral)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 4)
                self.state = 168
                self.variable_name()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 5)
                self.state = 169
                self.match(OneParser.LeftParen)
                self.state = 170
                self.expression()
                self.state = 171
                self.match(OneParser.RightParen)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OneParser.TypeContext)
            else:
                return self.getTypedRuleContext(OneParser.TypeContext,i)


        def variable_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OneParser.Variable_nameContext)
            else:
                return self.getTypedRuleContext(OneParser.Variable_nameContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(OneParser.Comma)
            else:
                return self.getToken(OneParser.Comma, i)

        def getRuleIndex(self):
            return OneParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = OneParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.type_()
            self.state = 176
            self.variable_name()
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 177
                self.match(OneParser.Comma)
                self.state = 178
                self.type_()
                self.state = 179
                self.variable_name()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Bool(self):
            return self.getToken(OneParser.Bool, 0)

        def Int(self):
            return self.getToken(OneParser.Int, 0)

        def Float(self):
            return self.getToken(OneParser.Float, 0)

        def String(self):
            return self.getToken(OneParser.String, 0)

        def getRuleIndex(self):
            return OneParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = OneParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(OneParser.Identifier, 0)

        def getRuleIndex(self):
            return OneParser.RULE_variable_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_name" ):
                listener.enterVariable_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_name" ):
                listener.exitVariable_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_name" ):
                return visitor.visitVariable_name(self)
            else:
                return visitor.visitChildren(self)




    def variable_name(self):

        localctx = OneParser.Variable_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_variable_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(OneParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





