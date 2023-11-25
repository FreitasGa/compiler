// Generated from C:/Users/SAMSUNG/PycharmProjects/compiler/assets/Teste.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link TesteParser}.
 */
public interface TesteListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link TesteParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(TesteParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link TesteParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(TesteParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link TesteParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(TesteParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link TesteParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(TesteParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link TesteParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(TesteParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link TesteParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(TesteParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link TesteParser#input}.
	 * @param ctx the parse tree
	 */
	void enterInput(TesteParser.InputContext ctx);
	/**
	 * Exit a parse tree produced by {@link TesteParser#input}.
	 * @param ctx the parse tree
	 */
	void exitInput(TesteParser.InputContext ctx);
	/**
	 * Enter a parse tree produced by {@link TesteParser#output}.
	 * @param ctx the parse tree
	 */
	void enterOutput(TesteParser.OutputContext ctx);
	/**
	 * Exit a parse tree produced by {@link TesteParser#output}.
	 * @param ctx the parse tree
	 */
	void exitOutput(TesteParser.OutputContext ctx);
	/**
	 * Enter a parse tree produced by {@link TesteParser#conditional}.
	 * @param ctx the parse tree
	 */
	void enterConditional(TesteParser.ConditionalContext ctx);
	/**
	 * Exit a parse tree produced by {@link TesteParser#conditional}.
	 * @param ctx the parse tree
	 */
	void exitConditional(TesteParser.ConditionalContext ctx);
	/**
	 * Enter a parse tree produced by {@link TesteParser#loop}.
	 * @param ctx the parse tree
	 */
	void enterLoop(TesteParser.LoopContext ctx);
	/**
	 * Exit a parse tree produced by {@link TesteParser#loop}.
	 * @param ctx the parse tree
	 */
	void exitLoop(TesteParser.LoopContext ctx);
	/**
	 * Enter a parse tree produced by {@link TesteParser#function_execution}.
	 * @param ctx the parse tree
	 */
	void enterFunction_execution(TesteParser.Function_executionContext ctx);
	/**
	 * Exit a parse tree produced by {@link TesteParser#function_execution}.
	 * @param ctx the parse tree
	 */
	void exitFunction_execution(TesteParser.Function_executionContext ctx);
	/**
	 * Enter a parse tree produced by {@link TesteParser#return_statement}.
	 * @param ctx the parse tree
	 */
	void enterReturn_statement(TesteParser.Return_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link TesteParser#return_statement}.
	 * @param ctx the parse tree
	 */
	void exitReturn_statement(TesteParser.Return_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link TesteParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(TesteParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link TesteParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(TesteParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link TesteParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(TesteParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link TesteParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(TesteParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link TesteParser#logic_expression}.
	 * @param ctx the parse tree
	 */
	void enterLogic_expression(TesteParser.Logic_expressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link TesteParser#logic_expression}.
	 * @param ctx the parse tree
	 */
	void exitLogic_expression(TesteParser.Logic_expressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link TesteParser#logic_term}.
	 * @param ctx the parse tree
	 */
	void enterLogic_term(TesteParser.Logic_termContext ctx);
	/**
	 * Exit a parse tree produced by {@link TesteParser#logic_term}.
	 * @param ctx the parse tree
	 */
	void exitLogic_term(TesteParser.Logic_termContext ctx);
	/**
	 * Enter a parse tree produced by {@link TesteParser#equality_expression}.
	 * @param ctx the parse tree
	 */
	void enterEquality_expression(TesteParser.Equality_expressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link TesteParser#equality_expression}.
	 * @param ctx the parse tree
	 */
	void exitEquality_expression(TesteParser.Equality_expressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link TesteParser#relational_expression}.
	 * @param ctx the parse tree
	 */
	void enterRelational_expression(TesteParser.Relational_expressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link TesteParser#relational_expression}.
	 * @param ctx the parse tree
	 */
	void exitRelational_expression(TesteParser.Relational_expressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link TesteParser#arithmetic_expression}.
	 * @param ctx the parse tree
	 */
	void enterArithmetic_expression(TesteParser.Arithmetic_expressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link TesteParser#arithmetic_expression}.
	 * @param ctx the parse tree
	 */
	void exitArithmetic_expression(TesteParser.Arithmetic_expressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link TesteParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(TesteParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link TesteParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(TesteParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link TesteParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(TesteParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link TesteParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(TesteParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link TesteParser#unary}.
	 * @param ctx the parse tree
	 */
	void enterUnary(TesteParser.UnaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link TesteParser#unary}.
	 * @param ctx the parse tree
	 */
	void exitUnary(TesteParser.UnaryContext ctx);
	/**
	 * Enter a parse tree produced by {@link TesteParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterPrimary(TesteParser.PrimaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link TesteParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitPrimary(TesteParser.PrimaryContext ctx);
	/**
	 * Enter a parse tree produced by {@link TesteParser#function_parameters}.
	 * @param ctx the parse tree
	 */
	void enterFunction_parameters(TesteParser.Function_parametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link TesteParser#function_parameters}.
	 * @param ctx the parse tree
	 */
	void exitFunction_parameters(TesteParser.Function_parametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link TesteParser#execution_parameters}.
	 * @param ctx the parse tree
	 */
	void enterExecution_parameters(TesteParser.Execution_parametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link TesteParser#execution_parameters}.
	 * @param ctx the parse tree
	 */
	void exitExecution_parameters(TesteParser.Execution_parametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link TesteParser#variable_name}.
	 * @param ctx the parse tree
	 */
	void enterVariable_name(TesteParser.Variable_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link TesteParser#variable_name}.
	 * @param ctx the parse tree
	 */
	void exitVariable_name(TesteParser.Variable_nameContext ctx);
}