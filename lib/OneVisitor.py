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


    # Visit a parse tree produced by OneParser#functionDecl.
    def visitFunctionDecl(self, ctx:OneParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#params.
    def visitParams(self, ctx:OneParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#param.
    def visitParam(self, ctx:OneParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#type.
    def visitType(self, ctx:OneParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#varDecl.
    def visitVarDecl(self, ctx:OneParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#compoundStmt.
    def visitCompoundStmt(self, ctx:OneParser.CompoundStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#stmt.
    def visitStmt(self, ctx:OneParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#exprStmt.
    def visitExprStmt(self, ctx:OneParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#expr.
    def visitExpr(self, ctx:OneParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#ifStmt.
    def visitIfStmt(self, ctx:OneParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#forStmt.
    def visitForStmt(self, ctx:OneParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#whileStmt.
    def visitWhileStmt(self, ctx:OneParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OneParser#returnStmt.
    def visitReturnStmt(self, ctx:OneParser.ReturnStmtContext):
        return self.visitChildren(ctx)



del OneParser