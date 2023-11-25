// Generated from C:/Users/SAMSUNG/PycharmProjects/compiler/assets/One2.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link One2Parser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface One2Visitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link One2Parser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(One2Parser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link One2Parser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatement(One2Parser.StatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link One2Parser#variable_declaration}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariable_declaration(One2Parser.Variable_declarationContext ctx);
	/**
	 * Visit a parse tree produced by {@link One2Parser#assignment}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignment(One2Parser.AssignmentContext ctx);
	/**
	 * Visit a parse tree produced by {@link One2Parser#function_declaration}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunction_declaration(One2Parser.Function_declarationContext ctx);
	/**
	 * Visit a parse tree produced by {@link One2Parser#if_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIf_statement(One2Parser.If_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link One2Parser#while_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhile_statement(One2Parser.While_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link One2Parser#for_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFor_statement(One2Parser.For_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link One2Parser#return_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReturn_statement(One2Parser.Return_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link One2Parser#expression_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression_statement(One2Parser.Expression_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link One2Parser#block}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBlock(One2Parser.BlockContext ctx);
	/**
	 * Visit a parse tree produced by {@link One2Parser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(One2Parser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link One2Parser#equality}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEquality(One2Parser.EqualityContext ctx);
	/**
	 * Visit a parse tree produced by {@link One2Parser#comparison}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitComparison(One2Parser.ComparisonContext ctx);
	/**
	 * Visit a parse tree produced by {@link One2Parser#addition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAddition(One2Parser.AdditionContext ctx);
	/**
	 * Visit a parse tree produced by {@link One2Parser#multiplication}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMultiplication(One2Parser.MultiplicationContext ctx);
	/**
	 * Visit a parse tree produced by {@link One2Parser#unary}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnary(One2Parser.UnaryContext ctx);
	/**
	 * Visit a parse tree produced by {@link One2Parser#primary}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrimary(One2Parser.PrimaryContext ctx);
	/**
	 * Visit a parse tree produced by {@link One2Parser#parameters}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParameters(One2Parser.ParametersContext ctx);
	/**
	 * Visit a parse tree produced by {@link One2Parser#type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitType(One2Parser.TypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link One2Parser#variable_name}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariable_name(One2Parser.Variable_nameContext ctx);
}