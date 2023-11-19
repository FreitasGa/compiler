# Generated from C:/Users/SAMSUNG/PycharmProjects/compiler/One.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .OneParser import OneParser
else:
    from OneParser import OneParser

# This class defines a complete listener for a parse tree produced by OneParser.
class OneListener(ParseTreeListener):

    # Enter a parse tree produced by OneParser#program.
    def enterProgram(self, ctx:OneParser.ProgramContext):
        pass

    # Exit a parse tree produced by OneParser#program.
    def exitProgram(self, ctx:OneParser.ProgramContext):
        pass


    # Enter a parse tree produced by OneParser#statement.
    def enterStatement(self, ctx:OneParser.StatementContext):
        pass

    # Exit a parse tree produced by OneParser#statement.
    def exitStatement(self, ctx:OneParser.StatementContext):
        pass


    # Enter a parse tree produced by OneParser#variableDecl.
    def enterVariableDecl(self, ctx:OneParser.VariableDeclContext):
        pass

    # Exit a parse tree produced by OneParser#variableDecl.
    def exitVariableDecl(self, ctx:OneParser.VariableDeclContext):
        pass


    # Enter a parse tree produced by OneParser#assignment.
    def enterAssignment(self, ctx:OneParser.AssignmentContext):
        pass

    # Exit a parse tree produced by OneParser#assignment.
    def exitAssignment(self, ctx:OneParser.AssignmentContext):
        pass


    # Enter a parse tree produced by OneParser#functionDecl.
    def enterFunctionDecl(self, ctx:OneParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by OneParser#functionDecl.
    def exitFunctionDecl(self, ctx:OneParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by OneParser#ifStatement.
    def enterIfStatement(self, ctx:OneParser.IfStatementContext):
        pass

    # Exit a parse tree produced by OneParser#ifStatement.
    def exitIfStatement(self, ctx:OneParser.IfStatementContext):
        pass


    # Enter a parse tree produced by OneParser#whileStatement.
    def enterWhileStatement(self, ctx:OneParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by OneParser#whileStatement.
    def exitWhileStatement(self, ctx:OneParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by OneParser#forStatement.
    def enterForStatement(self, ctx:OneParser.ForStatementContext):
        pass

    # Exit a parse tree produced by OneParser#forStatement.
    def exitForStatement(self, ctx:OneParser.ForStatementContext):
        pass


    # Enter a parse tree produced by OneParser#returnStatement.
    def enterReturnStatement(self, ctx:OneParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by OneParser#returnStatement.
    def exitReturnStatement(self, ctx:OneParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by OneParser#expressionStatement.
    def enterExpressionStatement(self, ctx:OneParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by OneParser#expressionStatement.
    def exitExpressionStatement(self, ctx:OneParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by OneParser#block.
    def enterBlock(self, ctx:OneParser.BlockContext):
        pass

    # Exit a parse tree produced by OneParser#block.
    def exitBlock(self, ctx:OneParser.BlockContext):
        pass


    # Enter a parse tree produced by OneParser#expression.
    def enterExpression(self, ctx:OneParser.ExpressionContext):
        pass

    # Exit a parse tree produced by OneParser#expression.
    def exitExpression(self, ctx:OneParser.ExpressionContext):
        pass


    # Enter a parse tree produced by OneParser#equality.
    def enterEquality(self, ctx:OneParser.EqualityContext):
        pass

    # Exit a parse tree produced by OneParser#equality.
    def exitEquality(self, ctx:OneParser.EqualityContext):
        pass


    # Enter a parse tree produced by OneParser#comparison.
    def enterComparison(self, ctx:OneParser.ComparisonContext):
        pass

    # Exit a parse tree produced by OneParser#comparison.
    def exitComparison(self, ctx:OneParser.ComparisonContext):
        pass


    # Enter a parse tree produced by OneParser#addition.
    def enterAddition(self, ctx:OneParser.AdditionContext):
        pass

    # Exit a parse tree produced by OneParser#addition.
    def exitAddition(self, ctx:OneParser.AdditionContext):
        pass


    # Enter a parse tree produced by OneParser#multiplication.
    def enterMultiplication(self, ctx:OneParser.MultiplicationContext):
        pass

    # Exit a parse tree produced by OneParser#multiplication.
    def exitMultiplication(self, ctx:OneParser.MultiplicationContext):
        pass


    # Enter a parse tree produced by OneParser#unary.
    def enterUnary(self, ctx:OneParser.UnaryContext):
        pass

    # Exit a parse tree produced by OneParser#unary.
    def exitUnary(self, ctx:OneParser.UnaryContext):
        pass


    # Enter a parse tree produced by OneParser#primary.
    def enterPrimary(self, ctx:OneParser.PrimaryContext):
        pass

    # Exit a parse tree produced by OneParser#primary.
    def exitPrimary(self, ctx:OneParser.PrimaryContext):
        pass


    # Enter a parse tree produced by OneParser#parameters.
    def enterParameters(self, ctx:OneParser.ParametersContext):
        pass

    # Exit a parse tree produced by OneParser#parameters.
    def exitParameters(self, ctx:OneParser.ParametersContext):
        pass


    # Enter a parse tree produced by OneParser#type.
    def enterType(self, ctx:OneParser.TypeContext):
        pass

    # Exit a parse tree produced by OneParser#type.
    def exitType(self, ctx:OneParser.TypeContext):
        pass


    # Enter a parse tree produced by OneParser#variableName.
    def enterVariableName(self, ctx:OneParser.VariableNameContext):
        pass

    # Exit a parse tree produced by OneParser#variableName.
    def exitVariableName(self, ctx:OneParser.VariableNameContext):
        pass



del OneParser