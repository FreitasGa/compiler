// Generated from C:/Users/SAMSUNG/PycharmProjects/compiler/assets/One2.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link One2Parser}.
 */
public interface One2Listener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link One2Parser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(One2Parser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link One2Parser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(One2Parser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link One2Parser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(One2Parser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link One2Parser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(One2Parser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link One2Parser#variable_declaration}.
	 * @param ctx the parse tree
	 */
	void enterVariable_declaration(One2Parser.Variable_declarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link One2Parser#variable_declaration}.
	 * @param ctx the parse tree
	 */
	void exitVariable_declaration(One2Parser.Variable_declarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link One2Parser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(One2Parser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link One2Parser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(One2Parser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link One2Parser#function_declaration}.
	 * @param ctx the parse tree
	 */
	void enterFunction_declaration(One2Parser.Function_declarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link One2Parser#function_declaration}.
	 * @param ctx the parse tree
	 */
	void exitFunction_declaration(One2Parser.Function_declarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link One2Parser#if_statement}.
	 * @param ctx the parse tree
	 */
	void enterIf_statement(One2Parser.If_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link One2Parser#if_statement}.
	 * @param ctx the parse tree
	 */
	void exitIf_statement(One2Parser.If_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link One2Parser#while_statement}.
	 * @param ctx the parse tree
	 */
	void enterWhile_statement(One2Parser.While_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link One2Parser#while_statement}.
	 * @param ctx the parse tree
	 */
	void exitWhile_statement(One2Parser.While_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link One2Parser#for_statement}.
	 * @param ctx the parse tree
	 */
	void enterFor_statement(One2Parser.For_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link One2Parser#for_statement}.
	 * @param ctx the parse tree
	 */
	void exitFor_statement(One2Parser.For_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link One2Parser#return_statement}.
	 * @param ctx the parse tree
	 */
	void enterReturn_statement(One2Parser.Return_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link One2Parser#return_statement}.
	 * @param ctx the parse tree
	 */
	void exitReturn_statement(One2Parser.Return_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link One2Parser#expression_statement}.
	 * @param ctx the parse tree
	 */
	void enterExpression_statement(One2Parser.Expression_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link One2Parser#expression_statement}.
	 * @param ctx the parse tree
	 */
	void exitExpression_statement(One2Parser.Expression_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link One2Parser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(One2Parser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link One2Parser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(One2Parser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link One2Parser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(One2Parser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link One2Parser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(One2Parser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link One2Parser#equality}.
	 * @param ctx the parse tree
	 */
	void enterEquality(One2Parser.EqualityContext ctx);
	/**
	 * Exit a parse tree produced by {@link One2Parser#equality}.
	 * @param ctx the parse tree
	 */
	void exitEquality(One2Parser.EqualityContext ctx);
	/**
	 * Enter a parse tree produced by {@link One2Parser#comparison}.
	 * @param ctx the parse tree
	 */
	void enterComparison(One2Parser.ComparisonContext ctx);
	/**
	 * Exit a parse tree produced by {@link One2Parser#comparison}.
	 * @param ctx the parse tree
	 */
	void exitComparison(One2Parser.ComparisonContext ctx);
	/**
	 * Enter a parse tree produced by {@link One2Parser#addition}.
	 * @param ctx the parse tree
	 */
	void enterAddition(One2Parser.AdditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link One2Parser#addition}.
	 * @param ctx the parse tree
	 */
	void exitAddition(One2Parser.AdditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link One2Parser#multiplication}.
	 * @param ctx the parse tree
	 */
	void enterMultiplication(One2Parser.MultiplicationContext ctx);
	/**
	 * Exit a parse tree produced by {@link One2Parser#multiplication}.
	 * @param ctx the parse tree
	 */
	void exitMultiplication(One2Parser.MultiplicationContext ctx);
	/**
	 * Enter a parse tree produced by {@link One2Parser#unary}.
	 * @param ctx the parse tree
	 */
	void enterUnary(One2Parser.UnaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link One2Parser#unary}.
	 * @param ctx the parse tree
	 */
	void exitUnary(One2Parser.UnaryContext ctx);
	/**
	 * Enter a parse tree produced by {@link One2Parser#primary}.
	 * @param ctx the parse tree
	 */
	void enterPrimary(One2Parser.PrimaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link One2Parser#primary}.
	 * @param ctx the parse tree
	 */
	void exitPrimary(One2Parser.PrimaryContext ctx);
	/**
	 * Enter a parse tree produced by {@link One2Parser#parameters}.
	 * @param ctx the parse tree
	 */
	void enterParameters(One2Parser.ParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link One2Parser#parameters}.
	 * @param ctx the parse tree
	 */
	void exitParameters(One2Parser.ParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link One2Parser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(One2Parser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link One2Parser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(One2Parser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link One2Parser#variable_name}.
	 * @param ctx the parse tree
	 */
	void enterVariable_name(One2Parser.Variable_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link One2Parser#variable_name}.
	 * @param ctx the parse tree
	 */
	void exitVariable_name(One2Parser.Variable_nameContext ctx);
}