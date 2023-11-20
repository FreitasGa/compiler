# Generated from C:/Users/gafre/Documents/Coding/python/compiler/One.g4 by ANTLR 4.13.1
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


    # Enter a parse tree produced by OneParser#variable_declaration.
    def enterVariable_declaration(self, ctx:OneParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by OneParser#variable_declaration.
    def exitVariable_declaration(self, ctx:OneParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by OneParser#assignment.
    def enterAssignment(self, ctx:OneParser.AssignmentContext):
        pass

    # Exit a parse tree produced by OneParser#assignment.
    def exitAssignment(self, ctx:OneParser.AssignmentContext):
        pass


    # Enter a parse tree produced by OneParser#function_declaration.
    def enterFunction_declaration(self, ctx:OneParser.Function_declarationContext):
        pass

    # Exit a parse tree produced by OneParser#function_declaration.
    def exitFunction_declaration(self, ctx:OneParser.Function_declarationContext):
        pass


    # Enter a parse tree produced by OneParser#if_statement.
    def enterIf_statement(self, ctx:OneParser.If_statementContext):
        pass

    # Exit a parse tree produced by OneParser#if_statement.
    def exitIf_statement(self, ctx:OneParser.If_statementContext):
        pass


    # Enter a parse tree produced by OneParser#while_statement.
    def enterWhile_statement(self, ctx:OneParser.While_statementContext):
        pass

    # Exit a parse tree produced by OneParser#while_statement.
    def exitWhile_statement(self, ctx:OneParser.While_statementContext):
        pass


    # Enter a parse tree produced by OneParser#for_statement.
    def enterFor_statement(self, ctx:OneParser.For_statementContext):
        pass

    # Exit a parse tree produced by OneParser#for_statement.
    def exitFor_statement(self, ctx:OneParser.For_statementContext):
        pass


    # Enter a parse tree produced by OneParser#return_statement.
    def enterReturn_statement(self, ctx:OneParser.Return_statementContext):
        pass

    # Exit a parse tree produced by OneParser#return_statement.
    def exitReturn_statement(self, ctx:OneParser.Return_statementContext):
        pass


    # Enter a parse tree produced by OneParser#expression_statement.
    def enterExpression_statement(self, ctx:OneParser.Expression_statementContext):
        pass

    # Exit a parse tree produced by OneParser#expression_statement.
    def exitExpression_statement(self, ctx:OneParser.Expression_statementContext):
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


    # Enter a parse tree produced by OneParser#variable_name.
    def enterVariable_name(self, ctx:OneParser.Variable_nameContext):
        pass

    # Exit a parse tree produced by OneParser#variable_name.
    def exitVariable_name(self, ctx:OneParser.Variable_nameContext):
        pass



del OneParser