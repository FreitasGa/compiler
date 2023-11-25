// Generated from C:/Users/SAMSUNG/PycharmProjects/compiler/assets/Teste.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link TesteParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface TesteVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link TesteParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(TesteParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link TesteParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatement(TesteParser.StatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link TesteParser#assignment}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignment(TesteParser.AssignmentContext ctx);
	/**
	 * Visit a parse tree produced by {@link TesteParser#input}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInput(TesteParser.InputContext ctx);
	/**
	 * Visit a parse tree produced by {@link TesteParser#output}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOutput(TesteParser.OutputContext ctx);
	/**
	 * Visit a parse tree produced by {@link TesteParser#conditional}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConditional(TesteParser.ConditionalContext ctx);
	/**
	 * Visit a parse tree produced by {@link TesteParser#loop}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLoop(TesteParser.LoopContext ctx);
	/**
	 * Visit a parse tree produced by {@link TesteParser#function_execution}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunction_execution(TesteParser.Function_executionContext ctx);
	/**
	 * Visit a parse tree produced by {@link TesteParser#return_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReturn_statement(TesteParser.Return_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link TesteParser#block}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBlock(TesteParser.BlockContext ctx);
	/**
	 * Visit a parse tree produced by {@link TesteParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(TesteParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link TesteParser#logic_expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLogic_expression(TesteParser.Logic_expressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link TesteParser#logic_term}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLogic_term(TesteParser.Logic_termContext ctx);
	/**
	 * Visit a parse tree produced by {@link TesteParser#equality_expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEquality_expression(TesteParser.Equality_expressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link TesteParser#relational_expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRelational_expression(TesteParser.Relational_expressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link TesteParser#arithmetic_expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArithmetic_expression(TesteParser.Arithmetic_expressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link TesteParser#term}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTerm(TesteParser.TermContext ctx);
	/**
	 * Visit a parse tree produced by {@link TesteParser#factor}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFactor(TesteParser.FactorContext ctx);
	/**
	 * Visit a parse tree produced by {@link TesteParser#unary}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnary(TesteParser.UnaryContext ctx);
	/**
	 * Visit a parse tree produced by {@link TesteParser#primary}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrimary(TesteParser.PrimaryContext ctx);
	/**
	 * Visit a parse tree produced by {@link TesteParser#function_parameters}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunction_parameters(TesteParser.Function_parametersContext ctx);
	/**
	 * Visit a parse tree produced by {@link TesteParser#execution_parameters}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExecution_parameters(TesteParser.Execution_parametersContext ctx);
	/**
	 * Visit a parse tree produced by {@link TesteParser#variable_name}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariable_name(TesteParser.Variable_nameContext ctx);
}