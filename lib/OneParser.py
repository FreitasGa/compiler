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
        4,1,32,204,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,5,0,40,8,0,
        10,0,12,0,43,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,55,
        8,1,1,2,1,2,1,2,1,2,3,2,61,8,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,
        4,1,4,1,4,3,4,74,8,4,1,4,1,4,1,4,5,4,79,8,4,10,4,12,4,82,9,4,1,4,
        1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,99,8,
        5,10,5,12,5,102,9,5,1,5,1,5,3,5,106,8,5,1,6,1,6,1,6,1,6,1,6,1,6,
        1,7,1,7,1,7,1,7,3,7,118,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,
        1,8,3,8,130,8,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,4,10,139,8,10,11,10,
        12,10,140,1,10,1,10,1,11,1,11,1,12,1,12,1,12,5,12,150,8,12,10,12,
        12,12,153,9,12,1,13,1,13,1,13,5,13,158,8,13,10,13,12,13,161,9,13,
        1,14,1,14,1,14,5,14,166,8,14,10,14,12,14,169,9,14,1,15,1,15,1,15,
        5,15,174,8,15,10,15,12,15,177,9,15,1,16,1,16,1,16,3,16,182,8,16,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,192,8,17,1,18,1,18,
        1,18,1,18,1,18,5,18,199,8,18,10,18,12,18,202,9,18,1,18,0,0,19,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0,2,2,0,17,17,
        29,29,2,0,2,2,24,24,210,0,41,1,0,0,0,2,54,1,0,0,0,4,56,1,0,0,0,6,
        64,1,0,0,0,8,69,1,0,0,0,10,86,1,0,0,0,12,107,1,0,0,0,14,113,1,0,
        0,0,16,127,1,0,0,0,18,133,1,0,0,0,20,136,1,0,0,0,22,144,1,0,0,0,
        24,146,1,0,0,0,26,154,1,0,0,0,28,162,1,0,0,0,30,170,1,0,0,0,32,181,
        1,0,0,0,34,191,1,0,0,0,36,193,1,0,0,0,38,40,3,2,1,0,39,38,1,0,0,
        0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,41,
        1,0,0,0,44,45,5,0,0,1,45,1,1,0,0,0,46,55,3,4,2,0,47,55,3,6,3,0,48,
        55,3,8,4,0,49,55,3,10,5,0,50,55,3,12,6,0,51,55,3,14,7,0,52,55,3,
        16,8,0,53,55,3,18,9,0,54,46,1,0,0,0,54,47,1,0,0,0,54,48,1,0,0,0,
        54,49,1,0,0,0,54,50,1,0,0,0,54,51,1,0,0,0,54,52,1,0,0,0,54,53,1,
        0,0,0,55,3,1,0,0,0,56,57,5,21,0,0,57,60,5,29,0,0,58,59,5,1,0,0,59,
        61,3,22,11,0,60,58,1,0,0,0,60,61,1,0,0,0,61,62,1,0,0,0,62,63,5,6,
        0,0,63,5,1,0,0,0,64,65,5,29,0,0,65,66,5,1,0,0,66,67,3,22,11,0,67,
        68,5,6,0,0,68,7,1,0,0,0,69,70,5,21,0,0,70,71,7,0,0,0,71,73,5,7,0,
        0,72,74,3,36,18,0,73,72,1,0,0,0,73,74,1,0,0,0,74,75,1,0,0,0,75,76,
        5,8,0,0,76,80,5,9,0,0,77,79,3,2,1,0,78,77,1,0,0,0,79,82,1,0,0,0,
        80,78,1,0,0,0,80,81,1,0,0,0,81,83,1,0,0,0,82,80,1,0,0,0,83,84,3,
        16,8,0,84,85,5,10,0,0,85,9,1,0,0,0,86,87,5,11,0,0,87,88,5,7,0,0,
        88,89,3,22,11,0,89,90,5,8,0,0,90,100,3,20,10,0,91,92,5,12,0,0,92,
        93,5,11,0,0,93,94,5,7,0,0,94,95,3,22,11,0,95,96,5,8,0,0,96,97,3,
        20,10,0,97,99,1,0,0,0,98,91,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,
        0,100,101,1,0,0,0,101,105,1,0,0,0,102,100,1,0,0,0,103,104,5,12,0,
        0,104,106,3,20,10,0,105,103,1,0,0,0,105,106,1,0,0,0,106,11,1,0,0,
        0,107,108,5,15,0,0,108,109,5,7,0,0,109,110,3,22,11,0,110,111,5,8,
        0,0,111,112,3,20,10,0,112,13,1,0,0,0,113,114,5,16,0,0,114,117,5,
        7,0,0,115,118,3,4,2,0,116,118,3,6,3,0,117,115,1,0,0,0,117,116,1,
        0,0,0,118,119,1,0,0,0,119,120,3,22,11,0,120,121,5,6,0,0,121,122,
        5,29,0,0,122,123,5,1,0,0,123,124,3,22,11,0,124,125,5,8,0,0,125,126,
        3,20,10,0,126,15,1,0,0,0,127,129,5,14,0,0,128,130,3,22,11,0,129,
        128,1,0,0,0,129,130,1,0,0,0,130,131,1,0,0,0,131,132,5,6,0,0,132,
        17,1,0,0,0,133,134,3,22,11,0,134,135,5,6,0,0,135,19,1,0,0,0,136,
        138,5,9,0,0,137,139,3,2,1,0,138,137,1,0,0,0,139,140,1,0,0,0,140,
        138,1,0,0,0,140,141,1,0,0,0,141,142,1,0,0,0,142,143,5,10,0,0,143,
        21,1,0,0,0,144,145,3,24,12,0,145,23,1,0,0,0,146,151,3,26,13,0,147,
        148,5,22,0,0,148,150,3,26,13,0,149,147,1,0,0,0,150,153,1,0,0,0,151,
        149,1,0,0,0,151,152,1,0,0,0,152,25,1,0,0,0,153,151,1,0,0,0,154,159,
        3,28,14,0,155,156,5,23,0,0,156,158,3,28,14,0,157,155,1,0,0,0,158,
        161,1,0,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,27,1,0,0,0,161,159,
        1,0,0,0,162,167,3,30,15,0,163,164,5,24,0,0,164,166,3,30,15,0,165,
        163,1,0,0,0,166,169,1,0,0,0,167,165,1,0,0,0,167,168,1,0,0,0,168,
        29,1,0,0,0,169,167,1,0,0,0,170,175,3,32,16,0,171,172,5,25,0,0,172,
        174,3,32,16,0,173,171,1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,0,175,
        176,1,0,0,0,176,31,1,0,0,0,177,175,1,0,0,0,178,179,7,1,0,0,179,182,
        3,32,16,0,180,182,3,34,17,0,181,178,1,0,0,0,181,180,1,0,0,0,182,
        33,1,0,0,0,183,192,5,26,0,0,184,192,5,27,0,0,185,192,5,28,0,0,186,
        192,5,29,0,0,187,188,5,7,0,0,188,189,3,22,11,0,189,190,5,8,0,0,190,
        192,1,0,0,0,191,183,1,0,0,0,191,184,1,0,0,0,191,185,1,0,0,0,191,
        186,1,0,0,0,191,187,1,0,0,0,192,35,1,0,0,0,193,194,5,21,0,0,194,
        200,5,29,0,0,195,196,5,5,0,0,196,197,5,21,0,0,197,199,5,29,0,0,198,
        195,1,0,0,0,199,202,1,0,0,0,200,198,1,0,0,0,200,201,1,0,0,0,201,
        37,1,0,0,0,202,200,1,0,0,0,17,41,54,60,73,80,100,105,117,129,140,
        151,159,167,175,181,191,200
    ]

class OneParser ( Parser ):

    grammarFileName = "One.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'!'", "'&&'", "'||'", "','", "';'", 
                     "'('", "')'", "'{'", "'}'", "'if'", "'else'", "'function'", 
                     "'return'", "'while'", "'for'", "'main'", "'.'" ]

    symbolicNames = [ "<INVALID>", "Assign", "Bang", "And", "Or", "Comma", 
                      "Semicolon", "LeftParen", "RightParen", "LeftBrace", 
                      "RightBrace", "If", "Else", "Function", "Return", 
                      "While", "For", "Main", "Dot", "Whitespace", "Newline", 
                      "Type", "EqualityOperation", "ComparisonOperation", 
                      "AdditionOperation", "MultiplicationOperation", "BoolLiteral", 
                      "NumberLiteral", "StringLiteral", "Identifier", "Digit", 
                      "Letter", "EscapeSequence" ]

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

    ruleNames =  [ "program", "statement", "variable_declaration", "assignment", 
                   "function_declaration", "if_statement", "while_statement", 
                   "for_statement", "return_statement", "expression_statement", 
                   "block", "expression", "equality", "comparison", "addition", 
                   "multiplication", "unary", "primary", "parameters" ]

    EOF = Token.EOF
    Assign=1
    Bang=2
    And=3
    Or=4
    Comma=5
    Semicolon=6
    LeftParen=7
    RightParen=8
    LeftBrace=9
    RightBrace=10
    If=11
    Else=12
    Function=13
    Return=14
    While=15
    For=16
    Main=17
    Dot=18
    Whitespace=19
    Newline=20
    Type=21
    EqualityOperation=22
    ComparisonOperation=23
    AdditionOperation=24
    MultiplicationOperation=25
    BoolLiteral=26
    NumberLiteral=27
    StringLiteral=28
    Identifier=29
    Digit=30
    Letter=31
    EscapeSequence=32

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
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1025624196) != 0):
                self.state = 38
                self.statement()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
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
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.function_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.if_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                self.while_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 51
                self.for_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 52
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 53
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

        def Type(self):
            return self.getToken(OneParser.Type, 0)

        def Identifier(self):
            return self.getToken(OneParser.Identifier, 0)

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
            self.state = 56
            self.match(OneParser.Type)
            self.state = 57
            self.match(OneParser.Identifier)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 58
                self.match(OneParser.Assign)
                self.state = 59
                self.expression()


            self.state = 62
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

        def Identifier(self):
            return self.getToken(OneParser.Identifier, 0)

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
            self.state = 64
            self.match(OneParser.Identifier)
            self.state = 65
            self.match(OneParser.Assign)
            self.state = 66
            self.expression()
            self.state = 67
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

        def Type(self):
            return self.getToken(OneParser.Type, 0)

        def LeftParen(self):
            return self.getToken(OneParser.LeftParen, 0)

        def RightParen(self):
            return self.getToken(OneParser.RightParen, 0)

        def LeftBrace(self):
            return self.getToken(OneParser.LeftBrace, 0)

        def return_statement(self):
            return self.getTypedRuleContext(OneParser.Return_statementContext,0)


        def RightBrace(self):
            return self.getToken(OneParser.RightBrace, 0)

        def Identifier(self):
            return self.getToken(OneParser.Identifier, 0)

        def Main(self):
            return self.getToken(OneParser.Main, 0)

        def parameters(self):
            return self.getTypedRuleContext(OneParser.ParametersContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OneParser.StatementContext)
            else:
                return self.getTypedRuleContext(OneParser.StatementContext,i)


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
            self.state = 69
            self.match(OneParser.Type)
            self.state = 70
            _la = self._input.LA(1)
            if not(_la==17 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 71
            self.match(OneParser.LeftParen)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 72
                self.parameters()


            self.state = 75
            self.match(OneParser.RightParen)
            self.state = 76
            self.match(OneParser.LeftBrace)
            self.state = 80
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 77
                    self.statement() 
                self.state = 82
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 83
            self.return_statement()
            self.state = 84
            self.match(OneParser.RightBrace)
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

        def If(self, i:int=None):
            if i is None:
                return self.getTokens(OneParser.If)
            else:
                return self.getToken(OneParser.If, i)

        def LeftParen(self, i:int=None):
            if i is None:
                return self.getTokens(OneParser.LeftParen)
            else:
                return self.getToken(OneParser.LeftParen, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OneParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OneParser.ExpressionContext,i)


        def RightParen(self, i:int=None):
            if i is None:
                return self.getTokens(OneParser.RightParen)
            else:
                return self.getToken(OneParser.RightParen, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OneParser.BlockContext)
            else:
                return self.getTypedRuleContext(OneParser.BlockContext,i)


        def Else(self, i:int=None):
            if i is None:
                return self.getTokens(OneParser.Else)
            else:
                return self.getToken(OneParser.Else, i)

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
            self.state = 86
            self.match(OneParser.If)
            self.state = 87
            self.match(OneParser.LeftParen)
            self.state = 88
            self.expression()
            self.state = 89
            self.match(OneParser.RightParen)
            self.state = 90
            self.block()
            self.state = 100
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 91
                    self.match(OneParser.Else)
                    self.state = 92
                    self.match(OneParser.If)
                    self.state = 93
                    self.match(OneParser.LeftParen)
                    self.state = 94
                    self.expression()
                    self.state = 95
                    self.match(OneParser.RightParen)
                    self.state = 96
                    self.block() 
                self.state = 102
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 103
                self.match(OneParser.Else)
                self.state = 104
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
            self.state = 107
            self.match(OneParser.While)
            self.state = 108
            self.match(OneParser.LeftParen)
            self.state = 109
            self.expression()
            self.state = 110
            self.match(OneParser.RightParen)
            self.state = 111
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

        def Identifier(self):
            return self.getToken(OneParser.Identifier, 0)

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
            self.state = 113
            self.match(OneParser.For)
            self.state = 114
            self.match(OneParser.LeftParen)
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.state = 115
                self.variable_declaration()
                pass
            elif token in [29]:
                self.state = 116
                self.assignment()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 119
            self.expression()
            self.state = 120
            self.match(OneParser.Semicolon)
            self.state = 121
            self.match(OneParser.Identifier)
            self.state = 122
            self.match(OneParser.Assign)
            self.state = 123
            self.expression()
            self.state = 124
            self.match(OneParser.RightParen)
            self.state = 125
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
            self.state = 127
            self.match(OneParser.Return)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1023410308) != 0):
                self.state = 128
                self.expression()


            self.state = 131
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
            self.state = 133
            self.expression()
            self.state = 134
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
            self.state = 136
            self.match(OneParser.LeftBrace)
            self.state = 138 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 137
                self.statement()
                self.state = 140 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1025624196) != 0)):
                    break

            self.state = 142
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
            self.state = 144
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
            self.state = 146
            self.comparison()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 147
                self.match(OneParser.EqualityOperation)
                self.state = 148
                self.comparison()
                self.state = 153
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
            self.state = 154
            self.addition()
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 155
                self.match(OneParser.ComparisonOperation)
                self.state = 156
                self.addition()
                self.state = 161
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
            self.state = 162
            self.multiplication()
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 163
                self.match(OneParser.AdditionOperation)
                self.state = 164
                self.multiplication()
                self.state = 169
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
            self.state = 170
            self.unary()
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 171
                self.match(OneParser.MultiplicationOperation)
                self.state = 172
                self.unary()
                self.state = 177
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
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                _la = self._input.LA(1)
                if not(_la==2 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 179
                self.unary()
                pass
            elif token in [7, 26, 27, 28, 29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
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

        def Identifier(self):
            return self.getToken(OneParser.Identifier, 0)

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
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(OneParser.BoolLiteral)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.match(OneParser.NumberLiteral)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                self.match(OneParser.StringLiteral)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 4)
                self.state = 186
                self.match(OneParser.Identifier)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 5)
                self.state = 187
                self.match(OneParser.LeftParen)
                self.state = 188
                self.expression()
                self.state = 189
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

        def Type(self, i:int=None):
            if i is None:
                return self.getTokens(OneParser.Type)
            else:
                return self.getToken(OneParser.Type, i)

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(OneParser.Identifier)
            else:
                return self.getToken(OneParser.Identifier, i)

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
            self.state = 193
            self.match(OneParser.Type)
            self.state = 194
            self.match(OneParser.Identifier)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 195
                self.match(OneParser.Comma)
                self.state = 196
                self.match(OneParser.Type)
                self.state = 197
                self.match(OneParser.Identifier)
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





