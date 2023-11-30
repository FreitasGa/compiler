# Generated from C:/Users/gafre/Documents/Coding/python/compiler/One.g4 by ANTLR 4.13.1
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
        4,1,34,189,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        5,0,42,8,0,10,0,12,0,45,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,3,1,57,8,1,1,2,1,2,1,2,1,2,3,2,63,8,2,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,1,4,1,4,1,4,1,4,3,4,76,8,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,3,5,88,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,100,
        8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,3,8,112,8,8,1,8,1,8,
        1,9,1,9,1,9,1,10,1,10,5,10,121,8,10,10,10,12,10,124,9,10,1,10,1,
        10,1,11,1,11,1,12,1,12,1,12,5,12,133,8,12,10,12,12,12,136,9,12,1,
        13,1,13,1,13,5,13,141,8,13,10,13,12,13,144,9,13,1,14,1,14,1,14,5,
        14,149,8,14,10,14,12,14,152,9,14,1,15,1,15,1,15,5,15,157,8,15,10,
        15,12,15,160,9,15,1,16,1,16,1,16,3,16,165,8,16,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,3,17,175,8,17,1,18,1,18,1,18,1,18,1,18,5,
        18,182,8,18,10,18,12,18,185,9,18,1,19,1,19,1,19,0,0,20,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,0,1,2,0,2,2,26,26,192,
        0,43,1,0,0,0,2,56,1,0,0,0,4,58,1,0,0,0,6,66,1,0,0,0,8,71,1,0,0,0,
        10,80,1,0,0,0,12,89,1,0,0,0,14,95,1,0,0,0,16,109,1,0,0,0,18,115,
        1,0,0,0,20,118,1,0,0,0,22,127,1,0,0,0,24,129,1,0,0,0,26,137,1,0,
        0,0,28,145,1,0,0,0,30,153,1,0,0,0,32,164,1,0,0,0,34,174,1,0,0,0,
        36,176,1,0,0,0,38,186,1,0,0,0,40,42,3,2,1,0,41,40,1,0,0,0,42,45,
        1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,43,1,0,0,0,
        46,47,5,0,0,1,47,1,1,0,0,0,48,57,3,4,2,0,49,57,3,6,3,0,50,57,3,8,
        4,0,51,57,3,10,5,0,52,57,3,12,6,0,53,57,3,14,7,0,54,57,3,16,8,0,
        55,57,3,18,9,0,56,48,1,0,0,0,56,49,1,0,0,0,56,50,1,0,0,0,56,51,1,
        0,0,0,56,52,1,0,0,0,56,53,1,0,0,0,56,54,1,0,0,0,56,55,1,0,0,0,57,
        3,1,0,0,0,58,59,5,23,0,0,59,62,3,38,19,0,60,61,5,1,0,0,61,63,3,22,
        11,0,62,60,1,0,0,0,62,63,1,0,0,0,63,64,1,0,0,0,64,65,5,6,0,0,65,
        5,1,0,0,0,66,67,3,38,19,0,67,68,5,1,0,0,68,69,3,22,11,0,69,70,5,
        6,0,0,70,7,1,0,0,0,71,72,5,23,0,0,72,73,3,38,19,0,73,75,5,8,0,0,
        74,76,3,36,18,0,75,74,1,0,0,0,75,76,1,0,0,0,76,77,1,0,0,0,77,78,
        5,9,0,0,78,79,3,20,10,0,79,9,1,0,0,0,80,81,5,14,0,0,81,82,5,8,0,
        0,82,83,3,22,11,0,83,84,5,9,0,0,84,87,3,20,10,0,85,86,5,15,0,0,86,
        88,3,20,10,0,87,85,1,0,0,0,87,88,1,0,0,0,88,11,1,0,0,0,89,90,5,18,
        0,0,90,91,5,8,0,0,91,92,3,22,11,0,92,93,5,9,0,0,93,94,3,20,10,0,
        94,13,1,0,0,0,95,96,5,19,0,0,96,99,5,8,0,0,97,100,3,4,2,0,98,100,
        3,6,3,0,99,97,1,0,0,0,99,98,1,0,0,0,100,101,1,0,0,0,101,102,3,22,
        11,0,102,103,5,6,0,0,103,104,3,38,19,0,104,105,5,1,0,0,105,106,3,
        22,11,0,106,107,5,9,0,0,107,108,3,20,10,0,108,15,1,0,0,0,109,111,
        5,17,0,0,110,112,3,22,11,0,111,110,1,0,0,0,111,112,1,0,0,0,112,113,
        1,0,0,0,113,114,5,6,0,0,114,17,1,0,0,0,115,116,3,22,11,0,116,117,
        5,6,0,0,117,19,1,0,0,0,118,122,5,10,0,0,119,121,3,2,1,0,120,119,
        1,0,0,0,121,124,1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,125,
        1,0,0,0,124,122,1,0,0,0,125,126,5,11,0,0,126,21,1,0,0,0,127,128,
        3,24,12,0,128,23,1,0,0,0,129,134,3,26,13,0,130,131,5,24,0,0,131,
        133,3,26,13,0,132,130,1,0,0,0,133,136,1,0,0,0,134,132,1,0,0,0,134,
        135,1,0,0,0,135,25,1,0,0,0,136,134,1,0,0,0,137,142,3,28,14,0,138,
        139,5,25,0,0,139,141,3,28,14,0,140,138,1,0,0,0,141,144,1,0,0,0,142,
        140,1,0,0,0,142,143,1,0,0,0,143,27,1,0,0,0,144,142,1,0,0,0,145,150,
        3,30,15,0,146,147,5,26,0,0,147,149,3,30,15,0,148,146,1,0,0,0,149,
        152,1,0,0,0,150,148,1,0,0,0,150,151,1,0,0,0,151,29,1,0,0,0,152,150,
        1,0,0,0,153,158,3,32,16,0,154,155,5,27,0,0,155,157,3,32,16,0,156,
        154,1,0,0,0,157,160,1,0,0,0,158,156,1,0,0,0,158,159,1,0,0,0,159,
        31,1,0,0,0,160,158,1,0,0,0,161,162,7,0,0,0,162,165,3,32,16,0,163,
        165,3,34,17,0,164,161,1,0,0,0,164,163,1,0,0,0,165,33,1,0,0,0,166,
        175,5,28,0,0,167,175,5,29,0,0,168,175,5,30,0,0,169,175,3,38,19,0,
        170,171,5,8,0,0,171,172,3,22,11,0,172,173,5,9,0,0,173,175,1,0,0,
        0,174,166,1,0,0,0,174,167,1,0,0,0,174,168,1,0,0,0,174,169,1,0,0,
        0,174,170,1,0,0,0,175,35,1,0,0,0,176,177,5,23,0,0,177,183,3,38,19,
        0,178,179,5,5,0,0,179,180,5,23,0,0,180,182,3,38,19,0,181,178,1,0,
        0,0,182,185,1,0,0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,37,1,0,0,
        0,185,183,1,0,0,0,186,187,5,31,0,0,187,39,1,0,0,0,15,43,56,62,75,
        87,99,111,122,134,142,150,158,164,174,183
    ]

class OneParser ( Parser ):

    grammarFileName = "One.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'!'", "'&&'", "'||'", "','", "';'", 
                     "':'", "'('", "')'", "'{'", "'}'", "'['", "']'", "'if'", 
                     "'else'", "'function'", "'return'", "'while'", "'for'", 
                     "'.'" ]

    symbolicNames = [ "<INVALID>", "Assign", "Bang", "And", "Or", "Comma", 
                      "Semicolon", "Colon", "LeftParen", "RightParen", "LeftBrace", 
                      "RightBrace", "LeftBracket", "RightBracket", "If", 
                      "Else", "Function", "Return", "While", "For", "Dot", 
                      "Whitespace", "Newline", "Types", "EqualityOperation", 
                      "ComparisonOperation", "AdditionOperation", "MultiplicationOperation", 
                      "BoolLiteral", "NumberLiteral", "StringLiteral", "Identifier", 
                      "Digit", "Letter", "EscapeSequence" ]

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
    RULE_variable_name = 19

    ruleNames =  [ "program", "statement", "variable_declaration", "assignment", 
                   "function_declaration", "if_statement", "while_statement", 
                   "for_statement", "return_statement", "expression_statement", 
                   "block", "expression", "equality", "comparison", "addition", 
                   "multiplication", "unary", "primary", "parameters", "variable_name" ]

    EOF = Token.EOF
    Assign=1
    Bang=2
    And=3
    Or=4
    Comma=5
    Semicolon=6
    Colon=7
    LeftParen=8
    RightParen=9
    LeftBrace=10
    RightBrace=11
    LeftBracket=12
    RightBracket=13
    If=14
    Else=15
    Function=16
    Return=17
    While=18
    For=19
    Dot=20
    Whitespace=21
    Newline=22
    Types=23
    EqualityOperation=24
    ComparisonOperation=25
    AdditionOperation=26
    MultiplicationOperation=27
    BoolLiteral=28
    NumberLiteral=29
    StringLiteral=30
    Identifier=31
    Digit=32
    Letter=33
    EscapeSequence=34

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
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4102963460) != 0):
                self.state = 40
                self.statement()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
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
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.function_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 51
                self.if_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 52
                self.while_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 53
                self.for_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 54
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 55
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

        def Types(self):
            return self.getToken(OneParser.Types, 0)

        def variable_name(self):
            return self.getTypedRuleContext(OneParser.Variable_nameContext,0)


        def Semicolon(self):
            return self.getToken(OneParser.Semicolon, 0)

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
            self.state = 58
            self.match(OneParser.Types)
            self.state = 59
            self.variable_name()
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 60
                self.match(OneParser.Assign)
                self.state = 61
                self.expression()


            self.state = 64
            self.match(OneParser.Semicolon)
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


        def Semicolon(self):
            return self.getToken(OneParser.Semicolon, 0)

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
            self.state = 69
            self.match(OneParser.Semicolon)
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

        def Types(self):
            return self.getToken(OneParser.Types, 0)

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
            self.state = 71
            self.match(OneParser.Types)
            self.state = 72
            self.variable_name()
            self.state = 73
            self.match(OneParser.LeftParen)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 74
                self.parameters()


            self.state = 77
            self.match(OneParser.RightParen)
            self.state = 78
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
            self.state = 80
            self.match(OneParser.If)
            self.state = 81
            self.match(OneParser.LeftParen)
            self.state = 82
            self.expression()
            self.state = 83
            self.match(OneParser.RightParen)
            self.state = 84
            self.block()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 85
                self.match(OneParser.Else)
                self.state = 86
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
            self.state = 89
            self.match(OneParser.While)
            self.state = 90
            self.match(OneParser.LeftParen)
            self.state = 91
            self.expression()
            self.state = 92
            self.match(OneParser.RightParen)
            self.state = 93
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OneParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OneParser.ExpressionContext,i)


        def Semicolon(self):
            return self.getToken(OneParser.Semicolon, 0)

        def variable_name(self):
            return self.getTypedRuleContext(OneParser.Variable_nameContext,0)


        def Assign(self):
            return self.getToken(OneParser.Assign, 0)

        def RightParen(self):
            return self.getToken(OneParser.RightParen, 0)

        def block(self):
            return self.getTypedRuleContext(OneParser.BlockContext,0)


        def variable_declaration(self):
            return self.getTypedRuleContext(OneParser.Variable_declarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(OneParser.AssignmentContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(OneParser.For)
            self.state = 96
            self.match(OneParser.LeftParen)
            self.state = 99
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.state = 97
                self.variable_declaration()
                pass
            elif token in [31]:
                self.state = 98
                self.assignment()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 101
            self.expression()
            self.state = 102
            self.match(OneParser.Semicolon)
            self.state = 103
            self.variable_name()
            self.state = 104
            self.match(OneParser.Assign)
            self.state = 105
            self.expression()
            self.state = 106
            self.match(OneParser.RightParen)
            self.state = 107
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

        def Semicolon(self):
            return self.getToken(OneParser.Semicolon, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(OneParser.Return)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4093640964) != 0):
                self.state = 110
                self.expression()


            self.state = 113
            self.match(OneParser.Semicolon)
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


        def Semicolon(self):
            return self.getToken(OneParser.Semicolon, 0)

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
            self.state = 116
            self.match(OneParser.Semicolon)
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
            self.state = 118
            self.match(OneParser.LeftBrace)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4102963460) != 0):
                self.state = 119
                self.statement()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 125
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
            self.state = 127
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


        def EqualityOperation(self, i:int=None):
            if i is None:
                return self.getTokens(OneParser.EqualityOperation)
            else:
                return self.getToken(OneParser.EqualityOperation, i)

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
            self.state = 129
            self.comparison()
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 130
                self.match(OneParser.EqualityOperation)
                self.state = 131
                self.comparison()
                self.state = 136
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


        def ComparisonOperation(self, i:int=None):
            if i is None:
                return self.getTokens(OneParser.ComparisonOperation)
            else:
                return self.getToken(OneParser.ComparisonOperation, i)

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
            self.state = 137
            self.addition()
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 138
                self.match(OneParser.ComparisonOperation)
                self.state = 139
                self.addition()
                self.state = 144
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


        def AdditionOperation(self, i:int=None):
            if i is None:
                return self.getTokens(OneParser.AdditionOperation)
            else:
                return self.getToken(OneParser.AdditionOperation, i)

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
            self.state = 145
            self.multiplication()
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 146
                self.match(OneParser.AdditionOperation)
                self.state = 147
                self.multiplication()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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


        def MultiplicationOperation(self, i:int=None):
            if i is None:
                return self.getTokens(OneParser.MultiplicationOperation)
            else:
                return self.getToken(OneParser.MultiplicationOperation, i)

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
            self.state = 153
            self.unary()
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 154
                self.match(OneParser.MultiplicationOperation)
                self.state = 155
                self.unary()
                self.state = 160
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


        def AdditionOperation(self):
            return self.getToken(OneParser.AdditionOperation, 0)

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
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                _la = self._input.LA(1)
                if not(_la==2 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 162
                self.unary()
                pass
            elif token in [8, 28, 29, 30, 31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
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
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(OneParser.BoolLiteral)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.match(OneParser.NumberLiteral)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 168
                self.match(OneParser.StringLiteral)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 4)
                self.state = 169
                self.variable_name()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 5)
                self.state = 170
                self.match(OneParser.LeftParen)
                self.state = 171
                self.expression()
                self.state = 172
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

        def Types(self, i:int=None):
            if i is None:
                return self.getTokens(OneParser.Types)
            else:
                return self.getToken(OneParser.Types, i)

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
            self.state = 176
            self.match(OneParser.Types)
            self.state = 177
            self.variable_name()
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 178
                self.match(OneParser.Comma)
                self.state = 179
                self.match(OneParser.Types)
                self.state = 180
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
        self.enterRule(localctx, 38, self.RULE_variable_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(OneParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





