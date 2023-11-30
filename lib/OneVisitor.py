# Generated from C:/Users/gafre/Documents/Coding/python/compiler/One.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .OneParser import OneParser
else:
    from OneParser import OneParser

# This class defines a complete generic visitor for a parse tree produced by OneParser.

class OneVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by OneParser#program.
    def visitProgram(self, ctx:OneParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#statement.
    def visitStatement(self, ctx:OneParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#variable_declaration.
    def visitVariable_declaration(self, ctx:OneParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#assignment.
    def visitAssignment(self, ctx:OneParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#function_declaration.
    def visitFunction_declaration(self, ctx:OneParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#if_statement.
    def visitIf_statement(self, ctx:OneParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#while_statement.
    def visitWhile_statement(self, ctx:OneParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#for_statement.
    def visitFor_statement(self, ctx:OneParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#return_statement.
    def visitReturn_statement(self, ctx:OneParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#expression_statement.
    def visitExpression_statement(self, ctx:OneParser.Expression_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#block.
    def visitBlock(self, ctx:OneParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#expression.
    def visitExpression(self, ctx:OneParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#equality.
    def visitEquality(self, ctx:OneParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#comparison.
    def visitComparison(self, ctx:OneParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#addition.
    def visitAddition(self, ctx:OneParser.AdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#multiplication.
    def visitMultiplication(self, ctx:OneParser.MultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#unary.
    def visitUnary(self, ctx:OneParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#primary.
    def visitPrimary(self, ctx:OneParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#parameters.
    def visitParameters(self, ctx:OneParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#variable_name.
    def visitVariable_name(self, ctx:OneParser.Variable_nameContext):
        return self.visitChildren(ctx)



del OneParser