// Generated from C:/Users/SAMSUNG/PycharmProjects/compiler/assets/Teste.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class TesteParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, ASSIGN=5, COLON=6, LEFT_PAREN=7, RIGHT_PAREN=8, 
		KEYWORD_ASSIGN=9, KEYWORD_READ=10, KEYWORD_PRINT=11, KEYWORD_WHILE=12, 
		KEYWORD_DECLARATIONS=13, KEYWORD_FUNCTIONS=14, KEYWORD_RETURN=15, KEYWORD_IF=16, 
		KEYWORD_ELSE=17, TYPE=18, LOGIC_OP=19, INT=20, REAL=21, VARIABLE=22, FUNCTION=23, 
		STRING=24, COMMENT=25, REL_OP=26, ARITH_OP1=27, ARITH_OP2=28, ARITH_OP3=29, 
		ARITH_OP_REL=30, Whitespace=31, Newline=32, Identifier=33, Digit=34, Letter=35, 
		EscapeSequence=36, Assign=37, KEYWORD_THEN=38, OP_ARIT_REL=39, Plus=40, 
		Minus=41;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_assignment = 2, RULE_input = 3, 
		RULE_output = 4, RULE_conditional = 5, RULE_loop = 6, RULE_function_execution = 7, 
		RULE_return_statement = 8, RULE_block = 9, RULE_expression = 10, RULE_logic_expression = 11, 
		RULE_logic_term = 12, RULE_equality_expression = 13, RULE_relational_expression = 14, 
		RULE_arithmetic_expression = 15, RULE_term = 16, RULE_factor = 17, RULE_unary = 18, 
		RULE_primary = 19, RULE_function_parameters = 20, RULE_execution_parameters = 21, 
		RULE_variable_name = 22;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "assignment", "input", "output", "conditional", 
			"loop", "function_execution", "return_statement", "block", "expression", 
			"logic_expression", "logic_term", "equality_expression", "relational_expression", 
			"arithmetic_expression", "term", "factor", "unary", "primary", "function_parameters", 
			"execution_parameters", "variable_name"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'EXECUTE'", "'BEGIN'", "'END'", "','", "'='", "':'", "'('", "')'", 
			null, "'read'", "'print'", "'while'", null, "'function'", "'return'", 
			"'if'", "'else'", null, null, null, null, null, null, null, null, null, 
			null, null, "'**'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, "ASSIGN", "COLON", "LEFT_PAREN", "RIGHT_PAREN", 
			"KEYWORD_ASSIGN", "KEYWORD_READ", "KEYWORD_PRINT", "KEYWORD_WHILE", "KEYWORD_DECLARATIONS", 
			"KEYWORD_FUNCTIONS", "KEYWORD_RETURN", "KEYWORD_IF", "KEYWORD_ELSE", 
			"TYPE", "LOGIC_OP", "INT", "REAL", "VARIABLE", "FUNCTION", "STRING", 
			"COMMENT", "REL_OP", "ARITH_OP1", "ARITH_OP2", "ARITH_OP3", "ARITH_OP_REL", 
			"Whitespace", "Newline", "Identifier", "Digit", "Letter", "EscapeSequence", 
			"Assign", "KEYWORD_THEN", "OP_ARIT_REL", "Plus", "Minus"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Teste.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public TesteParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(TesteParser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).exitProgram(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TesteVisitor ) return ((TesteVisitor<? extends T>)visitor).visitProgram(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(49);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8494596L) != 0)) {
				{
				{
				setState(46);
				statement();
				}
				}
				setState(51);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(52);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public InputContext input() {
			return getRuleContext(InputContext.class,0);
		}
		public OutputContext output() {
			return getRuleContext(OutputContext.class,0);
		}
		public ConditionalContext conditional() {
			return getRuleContext(ConditionalContext.class,0);
		}
		public LoopContext loop() {
			return getRuleContext(LoopContext.class,0);
		}
		public Function_executionContext function_execution() {
			return getRuleContext(Function_executionContext.class,0);
		}
		public Return_statementContext return_statement() {
			return getRuleContext(Return_statementContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).exitStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TesteVisitor ) return ((TesteVisitor<? extends T>)visitor).visitStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(62);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KEYWORD_ASSIGN:
				enterOuterAlt(_localctx, 1);
				{
				setState(54);
				assignment();
				}
				break;
			case KEYWORD_READ:
				enterOuterAlt(_localctx, 2);
				{
				setState(55);
				input();
				}
				break;
			case KEYWORD_PRINT:
				enterOuterAlt(_localctx, 3);
				{
				setState(56);
				output();
				}
				break;
			case KEYWORD_IF:
				enterOuterAlt(_localctx, 4);
				{
				setState(57);
				conditional();
				}
				break;
			case KEYWORD_WHILE:
				enterOuterAlt(_localctx, 5);
				{
				setState(58);
				loop();
				}
				break;
			case FUNCTION:
				enterOuterAlt(_localctx, 6);
				{
				setState(59);
				function_execution();
				}
				break;
			case KEYWORD_RETURN:
				enterOuterAlt(_localctx, 7);
				{
				setState(60);
				return_statement();
				}
				break;
			case T__1:
				enterOuterAlt(_localctx, 8);
				{
				setState(61);
				block();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode KEYWORD_ASSIGN() { return getToken(TesteParser.KEYWORD_ASSIGN, 0); }
		public Variable_nameContext variable_name() {
			return getRuleContext(Variable_nameContext.class,0);
		}
		public TerminalNode Assign() { return getToken(TesteParser.Assign, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).enterAssignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).exitAssignment(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TesteVisitor ) return ((TesteVisitor<? extends T>)visitor).visitAssignment(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_assignment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			match(KEYWORD_ASSIGN);
			setState(65);
			variable_name();
			setState(68);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Assign) {
				{
				setState(66);
				match(Assign);
				setState(67);
				expression();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InputContext extends ParserRuleContext {
		public TerminalNode KEYWORD_READ() { return getToken(TesteParser.KEYWORD_READ, 0); }
		public TerminalNode VARIABLE() { return getToken(TesteParser.VARIABLE, 0); }
		public InputContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_input; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).enterInput(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).exitInput(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TesteVisitor ) return ((TesteVisitor<? extends T>)visitor).visitInput(this);
			else return visitor.visitChildren(this);
		}
	}

	public final InputContext input() throws RecognitionException {
		InputContext _localctx = new InputContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_input);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			match(KEYWORD_READ);
			setState(71);
			match(VARIABLE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OutputContext extends ParserRuleContext {
		public TerminalNode KEYWORD_PRINT() { return getToken(TesteParser.KEYWORD_PRINT, 0); }
		public TerminalNode VARIABLE() { return getToken(TesteParser.VARIABLE, 0); }
		public TerminalNode STRING() { return getToken(TesteParser.STRING, 0); }
		public OutputContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_output; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).enterOutput(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).exitOutput(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TesteVisitor ) return ((TesteVisitor<? extends T>)visitor).visitOutput(this);
			else return visitor.visitChildren(this);
		}
	}

	public final OutputContext output() throws RecognitionException {
		OutputContext _localctx = new OutputContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_output);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(73);
			match(KEYWORD_PRINT);
			setState(74);
			_la = _input.LA(1);
			if ( !(_la==VARIABLE || _la==STRING) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionalContext extends ParserRuleContext {
		public TerminalNode KEYWORD_IF() { return getToken(TesteParser.KEYWORD_IF, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode KEYWORD_THEN() { return getToken(TesteParser.KEYWORD_THEN, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public TerminalNode KEYWORD_ELSE() { return getToken(TesteParser.KEYWORD_ELSE, 0); }
		public ConditionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditional; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).enterConditional(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).exitConditional(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TesteVisitor ) return ((TesteVisitor<? extends T>)visitor).visitConditional(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ConditionalContext conditional() throws RecognitionException {
		ConditionalContext _localctx = new ConditionalContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_conditional);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			match(KEYWORD_IF);
			setState(77);
			expression();
			setState(78);
			match(KEYWORD_THEN);
			setState(79);
			statement();
			setState(82);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(80);
				match(KEYWORD_ELSE);
				setState(81);
				statement();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LoopContext extends ParserRuleContext {
		public TerminalNode KEYWORD_WHILE() { return getToken(TesteParser.KEYWORD_WHILE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public LoopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_loop; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).enterLoop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).exitLoop(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TesteVisitor ) return ((TesteVisitor<? extends T>)visitor).visitLoop(this);
			else return visitor.visitChildren(this);
		}
	}

	public final LoopContext loop() throws RecognitionException {
		LoopContext _localctx = new LoopContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_loop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			match(KEYWORD_WHILE);
			setState(85);
			expression();
			setState(86);
			match(T__0);
			setState(87);
			statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Function_executionContext extends ParserRuleContext {
		public TerminalNode FUNCTION() { return getToken(TesteParser.FUNCTION, 0); }
		public TerminalNode LEFT_PAREN() { return getToken(TesteParser.LEFT_PAREN, 0); }
		public TerminalNode RIGHT_PAREN() { return getToken(TesteParser.RIGHT_PAREN, 0); }
		public Execution_parametersContext execution_parameters() {
			return getRuleContext(Execution_parametersContext.class,0);
		}
		public Function_executionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_execution; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).enterFunction_execution(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).exitFunction_execution(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TesteVisitor ) return ((TesteVisitor<? extends T>)visitor).visitFunction_execution(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Function_executionContext function_execution() throws RecognitionException {
		Function_executionContext _localctx = new Function_executionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_function_execution);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			match(FUNCTION);
			setState(90);
			match(LEFT_PAREN);
			setState(92);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 7340032L) != 0)) {
				{
				setState(91);
				execution_parameters();
				}
			}

			setState(94);
			match(RIGHT_PAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Return_statementContext extends ParserRuleContext {
		public TerminalNode KEYWORD_RETURN() { return getToken(TesteParser.KEYWORD_RETURN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Return_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).enterReturn_statement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).exitReturn_statement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TesteVisitor ) return ((TesteVisitor<? extends T>)visitor).visitReturn_statement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Return_statementContext return_statement() throws RecognitionException {
		Return_statementContext _localctx = new Return_statementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_return_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(96);
			match(KEYWORD_RETURN);
			setState(97);
			expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).enterBlock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).exitBlock(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TesteVisitor ) return ((TesteVisitor<? extends T>)visitor).visitBlock(this);
			else return visitor.visitChildren(this);
		}
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			match(T__1);
			setState(103);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8494596L) != 0)) {
				{
				{
				setState(100);
				statement();
				}
				}
				setState(105);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(106);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public Logic_expressionContext logic_expression() {
			return getRuleContext(Logic_expressionContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).exitExpression(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TesteVisitor ) return ((TesteVisitor<? extends T>)visitor).visitExpression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			logic_expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Logic_expressionContext extends ParserRuleContext {
		public List<Logic_termContext> logic_term() {
			return getRuleContexts(Logic_termContext.class);
		}
		public Logic_termContext logic_term(int i) {
			return getRuleContext(Logic_termContext.class,i);
		}
		public List<TerminalNode> LOGIC_OP() { return getTokens(TesteParser.LOGIC_OP); }
		public TerminalNode LOGIC_OP(int i) {
			return getToken(TesteParser.LOGIC_OP, i);
		}
		public Logic_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logic_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).enterLogic_expression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).exitLogic_expression(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TesteVisitor ) return ((TesteVisitor<? extends T>)visitor).visitLogic_expression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Logic_expressionContext logic_expression() throws RecognitionException {
		Logic_expressionContext _localctx = new Logic_expressionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_logic_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(110);
			logic_term();
			setState(115);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LOGIC_OP) {
				{
				{
				setState(111);
				match(LOGIC_OP);
				setState(112);
				logic_term();
				}
				}
				setState(117);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Logic_termContext extends ParserRuleContext {
		public List<Equality_expressionContext> equality_expression() {
			return getRuleContexts(Equality_expressionContext.class);
		}
		public Equality_expressionContext equality_expression(int i) {
			return getRuleContext(Equality_expressionContext.class,i);
		}
		public List<TerminalNode> REL_OP() { return getTokens(TesteParser.REL_OP); }
		public TerminalNode REL_OP(int i) {
			return getToken(TesteParser.REL_OP, i);
		}
		public List<TerminalNode> OP_ARIT_REL() { return getTokens(TesteParser.OP_ARIT_REL); }
		public TerminalNode OP_ARIT_REL(int i) {
			return getToken(TesteParser.OP_ARIT_REL, i);
		}
		public Logic_termContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logic_term; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).enterLogic_term(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).exitLogic_term(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TesteVisitor ) return ((TesteVisitor<? extends T>)visitor).visitLogic_term(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Logic_termContext logic_term() throws RecognitionException {
		Logic_termContext _localctx = new Logic_termContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_logic_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			equality_expression();
			setState(123);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==REL_OP || _la==OP_ARIT_REL) {
				{
				{
				setState(119);
				_la = _input.LA(1);
				if ( !(_la==REL_OP || _la==OP_ARIT_REL) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(120);
				equality_expression();
				}
				}
				setState(125);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Equality_expressionContext extends ParserRuleContext {
		public List<Relational_expressionContext> relational_expression() {
			return getRuleContexts(Relational_expressionContext.class);
		}
		public Relational_expressionContext relational_expression(int i) {
			return getRuleContext(Relational_expressionContext.class,i);
		}
		public List<TerminalNode> REL_OP() { return getTokens(TesteParser.REL_OP); }
		public TerminalNode REL_OP(int i) {
			return getToken(TesteParser.REL_OP, i);
		}
		public List<TerminalNode> OP_ARIT_REL() { return getTokens(TesteParser.OP_ARIT_REL); }
		public TerminalNode OP_ARIT_REL(int i) {
			return getToken(TesteParser.OP_ARIT_REL, i);
		}
		public Equality_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_equality_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).enterEquality_expression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).exitEquality_expression(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TesteVisitor ) return ((TesteVisitor<? extends T>)visitor).visitEquality_expression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Equality_expressionContext equality_expression() throws RecognitionException {
		Equality_expressionContext _localctx = new Equality_expressionContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_equality_expression);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			relational_expression();
			setState(131);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(127);
					_la = _input.LA(1);
					if ( !(_la==REL_OP || _la==OP_ARIT_REL) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(128);
					relational_expression();
					}
					} 
				}
				setState(133);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Relational_expressionContext extends ParserRuleContext {
		public List<Arithmetic_expressionContext> arithmetic_expression() {
			return getRuleContexts(Arithmetic_expressionContext.class);
		}
		public Arithmetic_expressionContext arithmetic_expression(int i) {
			return getRuleContext(Arithmetic_expressionContext.class,i);
		}
		public List<TerminalNode> REL_OP() { return getTokens(TesteParser.REL_OP); }
		public TerminalNode REL_OP(int i) {
			return getToken(TesteParser.REL_OP, i);
		}
		public List<TerminalNode> OP_ARIT_REL() { return getTokens(TesteParser.OP_ARIT_REL); }
		public TerminalNode OP_ARIT_REL(int i) {
			return getToken(TesteParser.OP_ARIT_REL, i);
		}
		public Relational_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relational_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).enterRelational_expression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).exitRelational_expression(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TesteVisitor ) return ((TesteVisitor<? extends T>)visitor).visitRelational_expression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Relational_expressionContext relational_expression() throws RecognitionException {
		Relational_expressionContext _localctx = new Relational_expressionContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_relational_expression);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(134);
			arithmetic_expression();
			setState(139);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(135);
					_la = _input.LA(1);
					if ( !(_la==REL_OP || _la==OP_ARIT_REL) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(136);
					arithmetic_expression();
					}
					} 
				}
				setState(141);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Arithmetic_expressionContext extends ParserRuleContext {
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public List<TerminalNode> ARITH_OP1() { return getTokens(TesteParser.ARITH_OP1); }
		public TerminalNode ARITH_OP1(int i) {
			return getToken(TesteParser.ARITH_OP1, i);
		}
		public Arithmetic_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arithmetic_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).enterArithmetic_expression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).exitArithmetic_expression(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TesteVisitor ) return ((TesteVisitor<? extends T>)visitor).visitArithmetic_expression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Arithmetic_expressionContext arithmetic_expression() throws RecognitionException {
		Arithmetic_expressionContext _localctx = new Arithmetic_expressionContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_arithmetic_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(142);
			term();
			setState(147);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ARITH_OP1) {
				{
				{
				setState(143);
				match(ARITH_OP1);
				setState(144);
				term();
				}
				}
				setState(149);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TermContext extends ParserRuleContext {
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public List<TerminalNode> ARITH_OP2() { return getTokens(TesteParser.ARITH_OP2); }
		public TerminalNode ARITH_OP2(int i) {
			return getToken(TesteParser.ARITH_OP2, i);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).enterTerm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).exitTerm(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TesteVisitor ) return ((TesteVisitor<? extends T>)visitor).visitTerm(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(150);
			factor();
			setState(155);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ARITH_OP2) {
				{
				{
				setState(151);
				match(ARITH_OP2);
				setState(152);
				factor();
				}
				}
				setState(157);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public List<UnaryContext> unary() {
			return getRuleContexts(UnaryContext.class);
		}
		public UnaryContext unary(int i) {
			return getRuleContext(UnaryContext.class,i);
		}
		public List<TerminalNode> ARITH_OP3() { return getTokens(TesteParser.ARITH_OP3); }
		public TerminalNode ARITH_OP3(int i) {
			return getToken(TesteParser.ARITH_OP3, i);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).enterFactor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).exitFactor(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TesteVisitor ) return ((TesteVisitor<? extends T>)visitor).visitFactor(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_factor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(158);
			unary();
			setState(163);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ARITH_OP3) {
				{
				{
				setState(159);
				match(ARITH_OP3);
				setState(160);
				unary();
				}
				}
				setState(165);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnaryContext extends ParserRuleContext {
		public UnaryContext unary() {
			return getRuleContext(UnaryContext.class,0);
		}
		public TerminalNode Plus() { return getToken(TesteParser.Plus, 0); }
		public TerminalNode Minus() { return getToken(TesteParser.Minus, 0); }
		public PrimaryContext primary() {
			return getRuleContext(PrimaryContext.class,0);
		}
		public UnaryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unary; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).enterUnary(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).exitUnary(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TesteVisitor ) return ((TesteVisitor<? extends T>)visitor).visitUnary(this);
			else return visitor.visitChildren(this);
		}
	}

	public final UnaryContext unary() throws RecognitionException {
		UnaryContext _localctx = new UnaryContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_unary);
		int _la;
		try {
			setState(169);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Plus:
			case Minus:
				enterOuterAlt(_localctx, 1);
				{
				setState(166);
				_la = _input.LA(1);
				if ( !(_la==Plus || _la==Minus) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(167);
				unary();
				}
				break;
			case LEFT_PAREN:
			case INT:
			case REAL:
			case VARIABLE:
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(168);
				primary();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(TesteParser.INT, 0); }
		public TerminalNode REAL() { return getToken(TesteParser.REAL, 0); }
		public TerminalNode VARIABLE() { return getToken(TesteParser.VARIABLE, 0); }
		public TerminalNode STRING() { return getToken(TesteParser.STRING, 0); }
		public TerminalNode LEFT_PAREN() { return getToken(TesteParser.LEFT_PAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RIGHT_PAREN() { return getToken(TesteParser.RIGHT_PAREN, 0); }
		public PrimaryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primary; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).enterPrimary(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).exitPrimary(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TesteVisitor ) return ((TesteVisitor<? extends T>)visitor).visitPrimary(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PrimaryContext primary() throws RecognitionException {
		PrimaryContext _localctx = new PrimaryContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_primary);
		try {
			setState(179);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				enterOuterAlt(_localctx, 1);
				{
				setState(171);
				match(INT);
				}
				break;
			case REAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(172);
				match(REAL);
				}
				break;
			case VARIABLE:
				enterOuterAlt(_localctx, 3);
				{
				setState(173);
				match(VARIABLE);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 4);
				{
				setState(174);
				match(STRING);
				}
				break;
			case LEFT_PAREN:
				enterOuterAlt(_localctx, 5);
				{
				setState(175);
				match(LEFT_PAREN);
				setState(176);
				expression();
				setState(177);
				match(RIGHT_PAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Function_parametersContext extends ParserRuleContext {
		public List<TerminalNode> TYPE() { return getTokens(TesteParser.TYPE); }
		public TerminalNode TYPE(int i) {
			return getToken(TesteParser.TYPE, i);
		}
		public List<TerminalNode> VARIABLE() { return getTokens(TesteParser.VARIABLE); }
		public TerminalNode VARIABLE(int i) {
			return getToken(TesteParser.VARIABLE, i);
		}
		public Function_parametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_parameters; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).enterFunction_parameters(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).exitFunction_parameters(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TesteVisitor ) return ((TesteVisitor<? extends T>)visitor).visitFunction_parameters(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Function_parametersContext function_parameters() throws RecognitionException {
		Function_parametersContext _localctx = new Function_parametersContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_function_parameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(181);
			match(TYPE);
			setState(182);
			match(VARIABLE);
			setState(188);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__3) {
				{
				{
				setState(183);
				match(T__3);
				setState(184);
				match(TYPE);
				setState(185);
				match(VARIABLE);
				}
				}
				setState(190);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Execution_parametersContext extends ParserRuleContext {
		public List<TerminalNode> VARIABLE() { return getTokens(TesteParser.VARIABLE); }
		public TerminalNode VARIABLE(int i) {
			return getToken(TesteParser.VARIABLE, i);
		}
		public List<TerminalNode> INT() { return getTokens(TesteParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(TesteParser.INT, i);
		}
		public List<TerminalNode> REAL() { return getTokens(TesteParser.REAL); }
		public TerminalNode REAL(int i) {
			return getToken(TesteParser.REAL, i);
		}
		public Execution_parametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_execution_parameters; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).enterExecution_parameters(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).exitExecution_parameters(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TesteVisitor ) return ((TesteVisitor<? extends T>)visitor).visitExecution_parameters(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Execution_parametersContext execution_parameters() throws RecognitionException {
		Execution_parametersContext _localctx = new Execution_parametersContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_execution_parameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(191);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 7340032L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(196);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__3) {
				{
				{
				setState(192);
				match(T__3);
				setState(193);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 7340032L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(198);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Variable_nameContext extends ParserRuleContext {
		public TerminalNode Identifier() { return getToken(TesteParser.Identifier, 0); }
		public Variable_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_name; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).enterVariable_name(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TesteListener ) ((TesteListener)listener).exitVariable_name(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TesteVisitor ) return ((TesteVisitor<? extends T>)visitor).visitVariable_name(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Variable_nameContext variable_name() throws RecognitionException {
		Variable_nameContext _localctx = new Variable_nameContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_variable_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(199);
			match(Identifier);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001)\u00ca\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0001\u0000\u0005\u00000\b\u0000\n\u0000\f\u0000"+
		"3\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001"+
		"?\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002"+
		"E\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0003\u0005S\b\u0005\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007"+
		"]\b\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\t\u0001"+
		"\t\u0005\tf\b\t\n\t\f\ti\t\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0005\u000br\b\u000b\n\u000b\f\u000bu\t\u000b"+
		"\u0001\f\u0001\f\u0001\f\u0005\fz\b\f\n\f\f\f}\t\f\u0001\r\u0001\r\u0001"+
		"\r\u0005\r\u0082\b\r\n\r\f\r\u0085\t\r\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0005\u000e\u008a\b\u000e\n\u000e\f\u000e\u008d\t\u000e\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0005\u000f\u0092\b\u000f\n\u000f\f\u000f\u0095\t\u000f"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0005\u0010\u009a\b\u0010\n\u0010"+
		"\f\u0010\u009d\t\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0005\u0011"+
		"\u00a2\b\u0011\n\u0011\f\u0011\u00a5\t\u0011\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0003\u0012\u00aa\b\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001"+
		"\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0003\u0013\u00b4"+
		"\b\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0005"+
		"\u0014\u00bb\b\u0014\n\u0014\f\u0014\u00be\t\u0014\u0001\u0015\u0001\u0015"+
		"\u0001\u0015\u0005\u0015\u00c3\b\u0015\n\u0015\f\u0015\u00c6\t\u0015\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0000\u0000\u0017\u0000\u0002\u0004\u0006"+
		"\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,\u0000"+
		"\u0004\u0002\u0000\u0016\u0016\u0018\u0018\u0002\u0000\u001a\u001a\'\'"+
		"\u0001\u0000()\u0001\u0000\u0014\u0016\u00cc\u00001\u0001\u0000\u0000"+
		"\u0000\u0002>\u0001\u0000\u0000\u0000\u0004@\u0001\u0000\u0000\u0000\u0006"+
		"F\u0001\u0000\u0000\u0000\bI\u0001\u0000\u0000\u0000\nL\u0001\u0000\u0000"+
		"\u0000\fT\u0001\u0000\u0000\u0000\u000eY\u0001\u0000\u0000\u0000\u0010"+
		"`\u0001\u0000\u0000\u0000\u0012c\u0001\u0000\u0000\u0000\u0014l\u0001"+
		"\u0000\u0000\u0000\u0016n\u0001\u0000\u0000\u0000\u0018v\u0001\u0000\u0000"+
		"\u0000\u001a~\u0001\u0000\u0000\u0000\u001c\u0086\u0001\u0000\u0000\u0000"+
		"\u001e\u008e\u0001\u0000\u0000\u0000 \u0096\u0001\u0000\u0000\u0000\""+
		"\u009e\u0001\u0000\u0000\u0000$\u00a9\u0001\u0000\u0000\u0000&\u00b3\u0001"+
		"\u0000\u0000\u0000(\u00b5\u0001\u0000\u0000\u0000*\u00bf\u0001\u0000\u0000"+
		"\u0000,\u00c7\u0001\u0000\u0000\u0000.0\u0003\u0002\u0001\u0000/.\u0001"+
		"\u0000\u0000\u000003\u0001\u0000\u0000\u00001/\u0001\u0000\u0000\u0000"+
		"12\u0001\u0000\u0000\u000024\u0001\u0000\u0000\u000031\u0001\u0000\u0000"+
		"\u000045\u0005\u0000\u0000\u00015\u0001\u0001\u0000\u0000\u00006?\u0003"+
		"\u0004\u0002\u00007?\u0003\u0006\u0003\u00008?\u0003\b\u0004\u00009?\u0003"+
		"\n\u0005\u0000:?\u0003\f\u0006\u0000;?\u0003\u000e\u0007\u0000<?\u0003"+
		"\u0010\b\u0000=?\u0003\u0012\t\u0000>6\u0001\u0000\u0000\u0000>7\u0001"+
		"\u0000\u0000\u0000>8\u0001\u0000\u0000\u0000>9\u0001\u0000\u0000\u0000"+
		">:\u0001\u0000\u0000\u0000>;\u0001\u0000\u0000\u0000><\u0001\u0000\u0000"+
		"\u0000>=\u0001\u0000\u0000\u0000?\u0003\u0001\u0000\u0000\u0000@A\u0005"+
		"\t\u0000\u0000AD\u0003,\u0016\u0000BC\u0005%\u0000\u0000CE\u0003\u0014"+
		"\n\u0000DB\u0001\u0000\u0000\u0000DE\u0001\u0000\u0000\u0000E\u0005\u0001"+
		"\u0000\u0000\u0000FG\u0005\n\u0000\u0000GH\u0005\u0016\u0000\u0000H\u0007"+
		"\u0001\u0000\u0000\u0000IJ\u0005\u000b\u0000\u0000JK\u0007\u0000\u0000"+
		"\u0000K\t\u0001\u0000\u0000\u0000LM\u0005\u0010\u0000\u0000MN\u0003\u0014"+
		"\n\u0000NO\u0005&\u0000\u0000OR\u0003\u0002\u0001\u0000PQ\u0005\u0011"+
		"\u0000\u0000QS\u0003\u0002\u0001\u0000RP\u0001\u0000\u0000\u0000RS\u0001"+
		"\u0000\u0000\u0000S\u000b\u0001\u0000\u0000\u0000TU\u0005\f\u0000\u0000"+
		"UV\u0003\u0014\n\u0000VW\u0005\u0001\u0000\u0000WX\u0003\u0002\u0001\u0000"+
		"X\r\u0001\u0000\u0000\u0000YZ\u0005\u0017\u0000\u0000Z\\\u0005\u0007\u0000"+
		"\u0000[]\u0003*\u0015\u0000\\[\u0001\u0000\u0000\u0000\\]\u0001\u0000"+
		"\u0000\u0000]^\u0001\u0000\u0000\u0000^_\u0005\b\u0000\u0000_\u000f\u0001"+
		"\u0000\u0000\u0000`a\u0005\u000f\u0000\u0000ab\u0003\u0014\n\u0000b\u0011"+
		"\u0001\u0000\u0000\u0000cg\u0005\u0002\u0000\u0000df\u0003\u0002\u0001"+
		"\u0000ed\u0001\u0000\u0000\u0000fi\u0001\u0000\u0000\u0000ge\u0001\u0000"+
		"\u0000\u0000gh\u0001\u0000\u0000\u0000hj\u0001\u0000\u0000\u0000ig\u0001"+
		"\u0000\u0000\u0000jk\u0005\u0003\u0000\u0000k\u0013\u0001\u0000\u0000"+
		"\u0000lm\u0003\u0016\u000b\u0000m\u0015\u0001\u0000\u0000\u0000ns\u0003"+
		"\u0018\f\u0000op\u0005\u0013\u0000\u0000pr\u0003\u0018\f\u0000qo\u0001"+
		"\u0000\u0000\u0000ru\u0001\u0000\u0000\u0000sq\u0001\u0000\u0000\u0000"+
		"st\u0001\u0000\u0000\u0000t\u0017\u0001\u0000\u0000\u0000us\u0001\u0000"+
		"\u0000\u0000v{\u0003\u001a\r\u0000wx\u0007\u0001\u0000\u0000xz\u0003\u001a"+
		"\r\u0000yw\u0001\u0000\u0000\u0000z}\u0001\u0000\u0000\u0000{y\u0001\u0000"+
		"\u0000\u0000{|\u0001\u0000\u0000\u0000|\u0019\u0001\u0000\u0000\u0000"+
		"}{\u0001\u0000\u0000\u0000~\u0083\u0003\u001c\u000e\u0000\u007f\u0080"+
		"\u0007\u0001\u0000\u0000\u0080\u0082\u0003\u001c\u000e\u0000\u0081\u007f"+
		"\u0001\u0000\u0000\u0000\u0082\u0085\u0001\u0000\u0000\u0000\u0083\u0081"+
		"\u0001\u0000\u0000\u0000\u0083\u0084\u0001\u0000\u0000\u0000\u0084\u001b"+
		"\u0001\u0000\u0000\u0000\u0085\u0083\u0001\u0000\u0000\u0000\u0086\u008b"+
		"\u0003\u001e\u000f\u0000\u0087\u0088\u0007\u0001\u0000\u0000\u0088\u008a"+
		"\u0003\u001e\u000f\u0000\u0089\u0087\u0001\u0000\u0000\u0000\u008a\u008d"+
		"\u0001\u0000\u0000\u0000\u008b\u0089\u0001\u0000\u0000\u0000\u008b\u008c"+
		"\u0001\u0000\u0000\u0000\u008c\u001d\u0001\u0000\u0000\u0000\u008d\u008b"+
		"\u0001\u0000\u0000\u0000\u008e\u0093\u0003 \u0010\u0000\u008f\u0090\u0005"+
		"\u001b\u0000\u0000\u0090\u0092\u0003 \u0010\u0000\u0091\u008f\u0001\u0000"+
		"\u0000\u0000\u0092\u0095\u0001\u0000\u0000\u0000\u0093\u0091\u0001\u0000"+
		"\u0000\u0000\u0093\u0094\u0001\u0000\u0000\u0000\u0094\u001f\u0001\u0000"+
		"\u0000\u0000\u0095\u0093\u0001\u0000\u0000\u0000\u0096\u009b\u0003\"\u0011"+
		"\u0000\u0097\u0098\u0005\u001c\u0000\u0000\u0098\u009a\u0003\"\u0011\u0000"+
		"\u0099\u0097\u0001\u0000\u0000\u0000\u009a\u009d\u0001\u0000\u0000\u0000"+
		"\u009b\u0099\u0001\u0000\u0000\u0000\u009b\u009c\u0001\u0000\u0000\u0000"+
		"\u009c!\u0001\u0000\u0000\u0000\u009d\u009b\u0001\u0000\u0000\u0000\u009e"+
		"\u00a3\u0003$\u0012\u0000\u009f\u00a0\u0005\u001d\u0000\u0000\u00a0\u00a2"+
		"\u0003$\u0012\u0000\u00a1\u009f\u0001\u0000\u0000\u0000\u00a2\u00a5\u0001"+
		"\u0000\u0000\u0000\u00a3\u00a1\u0001\u0000\u0000\u0000\u00a3\u00a4\u0001"+
		"\u0000\u0000\u0000\u00a4#\u0001\u0000\u0000\u0000\u00a5\u00a3\u0001\u0000"+
		"\u0000\u0000\u00a6\u00a7\u0007\u0002\u0000\u0000\u00a7\u00aa\u0003$\u0012"+
		"\u0000\u00a8\u00aa\u0003&\u0013\u0000\u00a9\u00a6\u0001\u0000\u0000\u0000"+
		"\u00a9\u00a8\u0001\u0000\u0000\u0000\u00aa%\u0001\u0000\u0000\u0000\u00ab"+
		"\u00b4\u0005\u0014\u0000\u0000\u00ac\u00b4\u0005\u0015\u0000\u0000\u00ad"+
		"\u00b4\u0005\u0016\u0000\u0000\u00ae\u00b4\u0005\u0018\u0000\u0000\u00af"+
		"\u00b0\u0005\u0007\u0000\u0000\u00b0\u00b1\u0003\u0014\n\u0000\u00b1\u00b2"+
		"\u0005\b\u0000\u0000\u00b2\u00b4\u0001\u0000\u0000\u0000\u00b3\u00ab\u0001"+
		"\u0000\u0000\u0000\u00b3\u00ac\u0001\u0000\u0000\u0000\u00b3\u00ad\u0001"+
		"\u0000\u0000\u0000\u00b3\u00ae\u0001\u0000\u0000\u0000\u00b3\u00af\u0001"+
		"\u0000\u0000\u0000\u00b4\'\u0001\u0000\u0000\u0000\u00b5\u00b6\u0005\u0012"+
		"\u0000\u0000\u00b6\u00bc\u0005\u0016\u0000\u0000\u00b7\u00b8\u0005\u0004"+
		"\u0000\u0000\u00b8\u00b9\u0005\u0012\u0000\u0000\u00b9\u00bb\u0005\u0016"+
		"\u0000\u0000\u00ba\u00b7\u0001\u0000\u0000\u0000\u00bb\u00be\u0001\u0000"+
		"\u0000\u0000\u00bc\u00ba\u0001\u0000\u0000\u0000\u00bc\u00bd\u0001\u0000"+
		"\u0000\u0000\u00bd)\u0001\u0000\u0000\u0000\u00be\u00bc\u0001\u0000\u0000"+
		"\u0000\u00bf\u00c4\u0007\u0003\u0000\u0000\u00c0\u00c1\u0005\u0004\u0000"+
		"\u0000\u00c1\u00c3\u0007\u0003\u0000\u0000\u00c2\u00c0\u0001\u0000\u0000"+
		"\u0000\u00c3\u00c6\u0001\u0000\u0000\u0000\u00c4\u00c2\u0001\u0000\u0000"+
		"\u0000\u00c4\u00c5\u0001\u0000\u0000\u0000\u00c5+\u0001\u0000\u0000\u0000"+
		"\u00c6\u00c4\u0001\u0000\u0000\u0000\u00c7\u00c8\u0005!\u0000\u0000\u00c8"+
		"-\u0001\u0000\u0000\u0000\u00111>DR\\gs{\u0083\u008b\u0093\u009b\u00a3"+
		"\u00a9\u00b3\u00bc\u00c4";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}