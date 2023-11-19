# Generated from C:/Users/SAMSUNG/PycharmProjects/compiler/One.g4 by ANTLR 4.13.1
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


    # Visit a parse tree produced by OneParser#variableDecl.
    def visitVariableDecl(self, ctx:OneParser.VariableDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#assignment.
    def visitAssignment(self, ctx:OneParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#functionDecl.
    def visitFunctionDecl(self, ctx:OneParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#ifStatement.
    def visitIfStatement(self, ctx:OneParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#whileStatement.
    def visitWhileStatement(self, ctx:OneParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#forStatement.
    def visitForStatement(self, ctx:OneParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#returnStatement.
    def visitReturnStatement(self, ctx:OneParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#expressionStatement.
    def visitExpressionStatement(self, ctx:OneParser.ExpressionStatementContext):
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


    # Visit a parse tree produced by OneParser#type.
    def visitType(self, ctx:OneParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#variableName.
    def visitVariableName(self, ctx:OneParser.VariableNameContext):
        return self.visitChildren(ctx)



del OneParser