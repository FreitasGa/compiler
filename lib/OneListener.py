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


    # Enter a parse tree produced by OneParser#functionDecl.
    def enterFunctionDecl(self, ctx:OneParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by OneParser#functionDecl.
    def exitFunctionDecl(self, ctx:OneParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by OneParser#params.
    def enterParams(self, ctx:OneParser.ParamsContext):
        pass

    # Exit a parse tree produced by OneParser#params.
    def exitParams(self, ctx:OneParser.ParamsContext):
        pass


    # Enter a parse tree produced by OneParser#param.
    def enterParam(self, ctx:OneParser.ParamContext):
        pass

    # Exit a parse tree produced by OneParser#param.
    def exitParam(self, ctx:OneParser.ParamContext):
        pass


    # Enter a parse tree produced by OneParser#type.
    def enterType(self, ctx:OneParser.TypeContext):
        pass

    # Exit a parse tree produced by OneParser#type.
    def exitType(self, ctx:OneParser.TypeContext):
        pass


    # Enter a parse tree produced by OneParser#varDecl.
    def enterVarDecl(self, ctx:OneParser.VarDeclContext):
        pass

    # Exit a parse tree produced by OneParser#varDecl.
    def exitVarDecl(self, ctx:OneParser.VarDeclContext):
        pass


    # Enter a parse tree produced by OneParser#compoundStmt.
    def enterCompoundStmt(self, ctx:OneParser.CompoundStmtContext):
        pass

    # Exit a parse tree produced by OneParser#compoundStmt.
    def exitCompoundStmt(self, ctx:OneParser.CompoundStmtContext):
        pass


    # Enter a parse tree produced by OneParser#stmt.
    def enterStmt(self, ctx:OneParser.StmtContext):
        pass

    # Exit a parse tree produced by OneParser#stmt.
    def exitStmt(self, ctx:OneParser.StmtContext):
        pass


    # Enter a parse tree produced by OneParser#exprStmt.
    def enterExprStmt(self, ctx:OneParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by OneParser#exprStmt.
    def exitExprStmt(self, ctx:OneParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by OneParser#expr.
    def enterExpr(self, ctx:OneParser.ExprContext):
        pass

    # Exit a parse tree produced by OneParser#expr.
    def exitExpr(self, ctx:OneParser.ExprContext):
        pass


    # Enter a parse tree produced by OneParser#ifStmt.
    def enterIfStmt(self, ctx:OneParser.IfStmtContext):
        pass

    # Exit a parse tree produced by OneParser#ifStmt.
    def exitIfStmt(self, ctx:OneParser.IfStmtContext):
        pass


    # Enter a parse tree produced by OneParser#forStmt.
    def enterForStmt(self, ctx:OneParser.ForStmtContext):
        pass

    # Exit a parse tree produced by OneParser#forStmt.
    def exitForStmt(self, ctx:OneParser.ForStmtContext):
        pass


    # Enter a parse tree produced by OneParser#whileStmt.
    def enterWhileStmt(self, ctx:OneParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by OneParser#whileStmt.
    def exitWhileStmt(self, ctx:OneParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by OneParser#returnStmt.
    def enterReturnStmt(self, ctx:OneParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by OneParser#returnStmt.
    def exitReturnStmt(self, ctx:OneParser.ReturnStmtContext):
        pass



del OneParser