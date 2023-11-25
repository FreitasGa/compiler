// Generated from C:/Users/SAMSUNG/PycharmProjects/compiler/assets/Teste.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class TesteLexer extends Lexer {
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
		EscapeSequence=36;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "ASSIGN", "COLON", "LEFT_PAREN", "RIGHT_PAREN", 
			"KEYWORD_ASSIGN", "KEYWORD_READ", "KEYWORD_PRINT", "KEYWORD_WHILE", "KEYWORD_DECLARATIONS", 
			"KEYWORD_FUNCTIONS", "KEYWORD_RETURN", "KEYWORD_IF", "KEYWORD_ELSE", 
			"TYPE", "LOGIC_OP", "INT", "REAL", "VARIABLE", "FUNCTION", "STRING", 
			"COMMENT", "REL_OP", "ARITH_OP1", "ARITH_OP2", "ARITH_OP3", "ARITH_OP_REL", 
			"Whitespace", "Newline", "Identifier", "Digit", "Letter", "EscapeSequence"
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
			"Whitespace", "Newline", "Identifier", "Digit", "Letter", "EscapeSequence"
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


	public TesteLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Teste.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000$\u012d\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002"+
		"\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002"+
		"\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002"+
		"\u001b\u0007\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002"+
		"\u001e\u0007\u001e\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007"+
		"!\u0002\"\u0007\"\u0002#\u0007#\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001"+
		"\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t"+
		"\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f"+
		"\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0003\u0011\u00a5\b\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0003\u0012\u00ad\b\u0012\u0001\u0013\u0003"+
		"\u0013\u00b0\b\u0013\u0001\u0013\u0004\u0013\u00b3\b\u0013\u000b\u0013"+
		"\f\u0013\u00b4\u0001\u0014\u0003\u0014\u00b8\b\u0014\u0001\u0014\u0004"+
		"\u0014\u00bb\b\u0014\u000b\u0014\f\u0014\u00bc\u0001\u0014\u0001\u0014"+
		"\u0004\u0014\u00c1\b\u0014\u000b\u0014\f\u0014\u00c2\u0003\u0014\u00c5"+
		"\b\u0014\u0001\u0015\u0001\u0015\u0005\u0015\u00c9\b\u0015\n\u0015\f\u0015"+
		"\u00cc\t\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0003\u0016\u00d9\b\u0016\u0001\u0016\u0001\u0016\u0005\u0016\u00dd\b"+
		"\u0016\n\u0016\f\u0016\u00e0\t\u0016\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0005\u0017\u00e5\b\u0017\n\u0017\f\u0017\u00e8\t\u0017\u0001\u0017\u0001"+
		"\u0017\u0001\u0018\u0001\u0018\u0005\u0018\u00ee\b\u0018\n\u0018\f\u0018"+
		"\u00f1\t\u0018\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019"+
		"\u0003\u0019\u00fe\b\u0019\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b"+
		"\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001d"+
		"\u0001\u001d\u0001\u001d\u0001\u001d\u0003\u001d\u010d\b\u001d\u0001\u001e"+
		"\u0004\u001e\u0110\b\u001e\u000b\u001e\f\u001e\u0111\u0001\u001e\u0001"+
		"\u001e\u0001\u001f\u0003\u001f\u0117\b\u001f\u0001\u001f\u0001\u001f\u0003"+
		"\u001f\u011b\b\u001f\u0001\u001f\u0001\u001f\u0001 \u0001 \u0001 \u0005"+
		" \u0122\b \n \f \u0125\t \u0001!\u0001!\u0001\"\u0001\"\u0001#\u0001#"+
		"\u0001#\u0000\u0000$\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t"+
		"\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f"+
		"\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014"+
		")\u0015+\u0016-\u0017/\u00181\u00193\u001a5\u001b7\u001c9\u001d;\u001e"+
		"=\u001f? A!C\"E#G$\u0001\u0000\t\u0002\u0000++--\u0002\u0000AZaz\u0003"+
		"\u000009AZaz\u0002\u0000\'\'\\\\\u0002\u0000\n\n\r\r\u0002\u0000**//\u0002"+
		"\u0000\t\t  \u0001\u000009\u0006\u0000\"\"\\\\bbnnrrtt\u0149\u0000\u0001"+
		"\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005"+
		"\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001"+
		"\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000"+
		"\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000"+
		"\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000"+
		"\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000"+
		"\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000"+
		"\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000"+
		"\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000"+
		"\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000\u0000+\u0001"+
		"\u0000\u0000\u0000\u0000-\u0001\u0000\u0000\u0000\u0000/\u0001\u0000\u0000"+
		"\u0000\u00001\u0001\u0000\u0000\u0000\u00003\u0001\u0000\u0000\u0000\u0000"+
		"5\u0001\u0000\u0000\u0000\u00007\u0001\u0000\u0000\u0000\u00009\u0001"+
		"\u0000\u0000\u0000\u0000;\u0001\u0000\u0000\u0000\u0000=\u0001\u0000\u0000"+
		"\u0000\u0000?\u0001\u0000\u0000\u0000\u0000A\u0001\u0000\u0000\u0000\u0000"+
		"C\u0001\u0000\u0000\u0000\u0000E\u0001\u0000\u0000\u0000\u0000G\u0001"+
		"\u0000\u0000\u0000\u0001I\u0001\u0000\u0000\u0000\u0003Q\u0001\u0000\u0000"+
		"\u0000\u0005W\u0001\u0000\u0000\u0000\u0007[\u0001\u0000\u0000\u0000\t"+
		"]\u0001\u0000\u0000\u0000\u000b_\u0001\u0000\u0000\u0000\ra\u0001\u0000"+
		"\u0000\u0000\u000fc\u0001\u0000\u0000\u0000\u0011e\u0001\u0000\u0000\u0000"+
		"\u0013i\u0001\u0000\u0000\u0000\u0015n\u0001\u0000\u0000\u0000\u0017t"+
		"\u0001\u0000\u0000\u0000\u0019z\u0001\u0000\u0000\u0000\u001b~\u0001\u0000"+
		"\u0000\u0000\u001d\u0087\u0001\u0000\u0000\u0000\u001f\u008e\u0001\u0000"+
		"\u0000\u0000!\u0091\u0001\u0000\u0000\u0000#\u00a4\u0001\u0000\u0000\u0000"+
		"%\u00ac\u0001\u0000\u0000\u0000\'\u00af\u0001\u0000\u0000\u0000)\u00b7"+
		"\u0001\u0000\u0000\u0000+\u00c6\u0001\u0000\u0000\u0000-\u00cd\u0001\u0000"+
		"\u0000\u0000/\u00e1\u0001\u0000\u0000\u00001\u00eb\u0001\u0000\u0000\u0000"+
		"3\u00fd\u0001\u0000\u0000\u00005\u00ff\u0001\u0000\u0000\u00007\u0101"+
		"\u0001\u0000\u0000\u00009\u0103\u0001\u0000\u0000\u0000;\u010c\u0001\u0000"+
		"\u0000\u0000=\u010f\u0001\u0000\u0000\u0000?\u011a\u0001\u0000\u0000\u0000"+
		"A\u011e\u0001\u0000\u0000\u0000C\u0126\u0001\u0000\u0000\u0000E\u0128"+
		"\u0001\u0000\u0000\u0000G\u012a\u0001\u0000\u0000\u0000IJ\u0005E\u0000"+
		"\u0000JK\u0005X\u0000\u0000KL\u0005E\u0000\u0000LM\u0005C\u0000\u0000"+
		"MN\u0005U\u0000\u0000NO\u0005T\u0000\u0000OP\u0005E\u0000\u0000P\u0002"+
		"\u0001\u0000\u0000\u0000QR\u0005B\u0000\u0000RS\u0005E\u0000\u0000ST\u0005"+
		"G\u0000\u0000TU\u0005I\u0000\u0000UV\u0005N\u0000\u0000V\u0004\u0001\u0000"+
		"\u0000\u0000WX\u0005E\u0000\u0000XY\u0005N\u0000\u0000YZ\u0005D\u0000"+
		"\u0000Z\u0006\u0001\u0000\u0000\u0000[\\\u0005,\u0000\u0000\\\b\u0001"+
		"\u0000\u0000\u0000]^\u0005=\u0000\u0000^\n\u0001\u0000\u0000\u0000_`\u0005"+
		":\u0000\u0000`\f\u0001\u0000\u0000\u0000ab\u0005(\u0000\u0000b\u000e\u0001"+
		"\u0000\u0000\u0000cd\u0005)\u0000\u0000d\u0010\u0001\u0000\u0000\u0000"+
		"ef\u0005v\u0000\u0000fg\u0005a\u0000\u0000gh\u0005r\u0000\u0000h\u0012"+
		"\u0001\u0000\u0000\u0000ij\u0005r\u0000\u0000jk\u0005e\u0000\u0000kl\u0005"+
		"a\u0000\u0000lm\u0005d\u0000\u0000m\u0014\u0001\u0000\u0000\u0000no\u0005"+
		"p\u0000\u0000op\u0005r\u0000\u0000pq\u0005i\u0000\u0000qr\u0005n\u0000"+
		"\u0000rs\u0005t\u0000\u0000s\u0016\u0001\u0000\u0000\u0000tu\u0005w\u0000"+
		"\u0000uv\u0005h\u0000\u0000vw\u0005i\u0000\u0000wx\u0005l\u0000\u0000"+
		"xy\u0005e\u0000\u0000y\u0018\u0001\u0000\u0000\u0000z{\u0005v\u0000\u0000"+
		"{|\u0005a\u0000\u0000|}\u0005r\u0000\u0000}\u001a\u0001\u0000\u0000\u0000"+
		"~\u007f\u0005f\u0000\u0000\u007f\u0080\u0005u\u0000\u0000\u0080\u0081"+
		"\u0005n\u0000\u0000\u0081\u0082\u0005c\u0000\u0000\u0082\u0083\u0005t"+
		"\u0000\u0000\u0083\u0084\u0005i\u0000\u0000\u0084\u0085\u0005o\u0000\u0000"+
		"\u0085\u0086\u0005n\u0000\u0000\u0086\u001c\u0001\u0000\u0000\u0000\u0087"+
		"\u0088\u0005r\u0000\u0000\u0088\u0089\u0005e\u0000\u0000\u0089\u008a\u0005"+
		"t\u0000\u0000\u008a\u008b\u0005u\u0000\u0000\u008b\u008c\u0005r\u0000"+
		"\u0000\u008c\u008d\u0005n\u0000\u0000\u008d\u001e\u0001\u0000\u0000\u0000"+
		"\u008e\u008f\u0005i\u0000\u0000\u008f\u0090\u0005f\u0000\u0000\u0090 "+
		"\u0001\u0000\u0000\u0000\u0091\u0092\u0005e\u0000\u0000\u0092\u0093\u0005"+
		"l\u0000\u0000\u0093\u0094\u0005s\u0000\u0000\u0094\u0095\u0005e\u0000"+
		"\u0000\u0095\"\u0001\u0000\u0000\u0000\u0096\u0097\u0005i\u0000\u0000"+
		"\u0097\u0098\u0005n\u0000\u0000\u0098\u00a5\u0005t\u0000\u0000\u0099\u009a"+
		"\u0005f\u0000\u0000\u009a\u009b\u0005l\u0000\u0000\u009b\u009c\u0005o"+
		"\u0000\u0000\u009c\u009d\u0005a\u0000\u0000\u009d\u00a5\u0005t\u0000\u0000"+
		"\u009e\u009f\u0005s\u0000\u0000\u009f\u00a0\u0005t\u0000\u0000\u00a0\u00a1"+
		"\u0005r\u0000\u0000\u00a1\u00a2\u0005i\u0000\u0000\u00a2\u00a3\u0005n"+
		"\u0000\u0000\u00a3\u00a5\u0005g\u0000\u0000\u00a4\u0096\u0001\u0000\u0000"+
		"\u0000\u00a4\u0099\u0001\u0000\u0000\u0000\u00a4\u009e\u0001\u0000\u0000"+
		"\u0000\u00a5$\u0001\u0000\u0000\u0000\u00a6\u00a7\u0005&\u0000\u0000\u00a7"+
		"\u00ad\u0005&\u0000\u0000\u00a8\u00a9\u0005|\u0000\u0000\u00a9\u00ad\u0005"+
		"|\u0000\u0000\u00aa\u00ab\u0005!\u0000\u0000\u00ab\u00ad\u0005=\u0000"+
		"\u0000\u00ac\u00a6\u0001\u0000\u0000\u0000\u00ac\u00a8\u0001\u0000\u0000"+
		"\u0000\u00ac\u00aa\u0001\u0000\u0000\u0000\u00ad&\u0001\u0000\u0000\u0000"+
		"\u00ae\u00b0\u0007\u0000\u0000\u0000\u00af\u00ae\u0001\u0000\u0000\u0000"+
		"\u00af\u00b0\u0001\u0000\u0000\u0000\u00b0\u00b2\u0001\u0000\u0000\u0000"+
		"\u00b1\u00b3\u000209\u0000\u00b2\u00b1\u0001\u0000\u0000\u0000\u00b3\u00b4"+
		"\u0001\u0000\u0000\u0000\u00b4\u00b2\u0001\u0000\u0000\u0000\u00b4\u00b5"+
		"\u0001\u0000\u0000\u0000\u00b5(\u0001\u0000\u0000\u0000\u00b6\u00b8\u0007"+
		"\u0000\u0000\u0000\u00b7\u00b6\u0001\u0000\u0000\u0000\u00b7\u00b8\u0001"+
		"\u0000\u0000\u0000\u00b8\u00ba\u0001\u0000\u0000\u0000\u00b9\u00bb\u0002"+
		"09\u0000\u00ba\u00b9\u0001\u0000\u0000\u0000\u00bb\u00bc\u0001\u0000\u0000"+
		"\u0000\u00bc\u00ba\u0001\u0000\u0000\u0000\u00bc\u00bd\u0001\u0000\u0000"+
		"\u0000\u00bd\u00c4\u0001\u0000\u0000\u0000\u00be\u00c0\u0005.\u0000\u0000"+
		"\u00bf\u00c1\u000209\u0000\u00c0\u00bf\u0001\u0000\u0000\u0000\u00c1\u00c2"+
		"\u0001\u0000\u0000\u0000\u00c2\u00c0\u0001\u0000\u0000\u0000\u00c2\u00c3"+
		"\u0001\u0000\u0000\u0000\u00c3\u00c5\u0001\u0000\u0000\u0000\u00c4\u00be"+
		"\u0001\u0000\u0000\u0000\u00c4\u00c5\u0001\u0000\u0000\u0000\u00c5*\u0001"+
		"\u0000\u0000\u0000\u00c6\u00ca\u0007\u0001\u0000\u0000\u00c7\u00c9\u0007"+
		"\u0002\u0000\u0000\u00c8\u00c7\u0001\u0000\u0000\u0000\u00c9\u00cc\u0001"+
		"\u0000\u0000\u0000\u00ca\u00c8\u0001\u0000\u0000\u0000\u00ca\u00cb\u0001"+
		"\u0000\u0000\u0000\u00cb,\u0001\u0000\u0000\u0000\u00cc\u00ca\u0001\u0000"+
		"\u0000\u0000\u00cd\u00ce\u0005f\u0000\u0000\u00ce\u00cf\u0005u\u0000\u0000"+
		"\u00cf\u00d0\u0005n\u0000\u0000\u00d0\u00d1\u0005c\u0000\u0000\u00d1\u00d2"+
		"\u0005t\u0000\u0000\u00d2\u00d3\u0005i\u0000\u0000\u00d3\u00d4\u0005o"+
		"\u0000\u0000\u00d4\u00d5\u0005n\u0000\u0000\u00d5\u00d8\u0001\u0000\u0000"+
		"\u0000\u00d6\u00d9\u0003E\"\u0000\u00d7\u00d9\u0003C!\u0000\u00d8\u00d6"+
		"\u0001\u0000\u0000\u0000\u00d8\u00d7\u0001\u0000\u0000\u0000\u00d9\u00de"+
		"\u0001\u0000\u0000\u0000\u00da\u00dd\u0003E\"\u0000\u00db\u00dd\u0003"+
		"C!\u0000\u00dc\u00da\u0001\u0000\u0000\u0000\u00dc\u00db\u0001\u0000\u0000"+
		"\u0000\u00dd\u00e0\u0001\u0000\u0000\u0000\u00de\u00dc\u0001\u0000\u0000"+
		"\u0000\u00de\u00df\u0001\u0000\u0000\u0000\u00df.\u0001\u0000\u0000\u0000"+
		"\u00e0\u00de\u0001\u0000\u0000\u0000\u00e1\u00e6\u0005\'\u0000\u0000\u00e2"+
		"\u00e5\b\u0003\u0000\u0000\u00e3\u00e5\u0003G#\u0000\u00e4\u00e2\u0001"+
		"\u0000\u0000\u0000\u00e4\u00e3\u0001\u0000\u0000\u0000\u00e5\u00e8\u0001"+
		"\u0000\u0000\u0000\u00e6\u00e4\u0001\u0000\u0000\u0000\u00e6\u00e7\u0001"+
		"\u0000\u0000\u0000\u00e7\u00e9\u0001\u0000\u0000\u0000\u00e8\u00e6\u0001"+
		"\u0000\u0000\u0000\u00e9\u00ea\u0005\'\u0000\u0000\u00ea0\u0001\u0000"+
		"\u0000\u0000\u00eb\u00ef\u0005%\u0000\u0000\u00ec\u00ee\b\u0004\u0000"+
		"\u0000\u00ed\u00ec\u0001\u0000\u0000\u0000\u00ee\u00f1\u0001\u0000\u0000"+
		"\u0000\u00ef\u00ed\u0001\u0000\u0000\u0000\u00ef\u00f0\u0001\u0000\u0000"+
		"\u0000\u00f0\u00f2\u0001\u0000\u0000\u0000\u00f1\u00ef\u0001\u0000\u0000"+
		"\u0000\u00f2\u00f3\u0006\u0018\u0000\u0000\u00f32\u0001\u0000\u0000\u0000"+
		"\u00f4\u00fe\u0005>\u0000\u0000\u00f5\u00f6\u0005>\u0000\u0000\u00f6\u00fe"+
		"\u0005=\u0000\u0000\u00f7\u00fe\u0005<\u0000\u0000\u00f8\u00f9\u0005<"+
		"\u0000\u0000\u00f9\u00fe\u0005=\u0000\u0000\u00fa\u00fb\u0005<\u0000\u0000"+
		"\u00fb\u00fe\u0005>\u0000\u0000\u00fc\u00fe\u0005=\u0000\u0000\u00fd\u00f4"+
		"\u0001\u0000\u0000\u0000\u00fd\u00f5\u0001\u0000\u0000\u0000\u00fd\u00f7"+
		"\u0001\u0000\u0000\u0000\u00fd\u00f8\u0001\u0000\u0000\u0000\u00fd\u00fa"+
		"\u0001\u0000\u0000\u0000\u00fd\u00fc\u0001\u0000\u0000\u0000\u00fe4\u0001"+
		"\u0000\u0000\u0000\u00ff\u0100\u0007\u0000\u0000\u0000\u01006\u0001\u0000"+
		"\u0000\u0000\u0101\u0102\u0007\u0005\u0000\u0000\u01028\u0001\u0000\u0000"+
		"\u0000\u0103\u0104\u0005*\u0000\u0000\u0104\u0105\u0005*\u0000\u0000\u0105"+
		":\u0001\u0000\u0000\u0000\u0106\u0107\u0005+\u0000\u0000\u0107\u010d\u0005"+
		"=\u0000\u0000\u0108\u0109\u0005-\u0000\u0000\u0109\u010d\u0005=\u0000"+
		"\u0000\u010a\u010b\u0005*\u0000\u0000\u010b\u010d\u0005=\u0000\u0000\u010c"+
		"\u0106\u0001\u0000\u0000\u0000\u010c\u0108\u0001\u0000\u0000\u0000\u010c"+
		"\u010a\u0001\u0000\u0000\u0000\u010d<\u0001\u0000\u0000\u0000\u010e\u0110"+
		"\u0007\u0006\u0000\u0000\u010f\u010e\u0001\u0000\u0000\u0000\u0110\u0111"+
		"\u0001\u0000\u0000\u0000\u0111\u010f\u0001\u0000\u0000\u0000\u0111\u0112"+
		"\u0001\u0000\u0000\u0000\u0112\u0113\u0001\u0000\u0000\u0000\u0113\u0114"+
		"\u0006\u001e\u0000\u0000\u0114>\u0001\u0000\u0000\u0000\u0115\u0117\u0005"+
		"\r\u0000\u0000\u0116\u0115\u0001\u0000\u0000\u0000\u0116\u0117\u0001\u0000"+
		"\u0000\u0000\u0117\u0118\u0001\u0000\u0000\u0000\u0118\u011b\u0005\n\u0000"+
		"\u0000\u0119\u011b\u0005\r\u0000\u0000\u011a\u0116\u0001\u0000\u0000\u0000"+
		"\u011a\u0119\u0001\u0000\u0000\u0000\u011b\u011c\u0001\u0000\u0000\u0000"+
		"\u011c\u011d\u0006\u001f\u0000\u0000\u011d@\u0001\u0000\u0000\u0000\u011e"+
		"\u0123\u0003E\"\u0000\u011f\u0122\u0003E\"\u0000\u0120\u0122\u0003C!\u0000"+
		"\u0121\u011f\u0001\u0000\u0000\u0000\u0121\u0120\u0001\u0000\u0000\u0000"+
		"\u0122\u0125\u0001\u0000\u0000\u0000\u0123\u0121\u0001\u0000\u0000\u0000"+
		"\u0123\u0124\u0001\u0000\u0000\u0000\u0124B\u0001\u0000\u0000\u0000\u0125"+
		"\u0123\u0001\u0000\u0000\u0000\u0126\u0127\u0007\u0007\u0000\u0000\u0127"+
		"D\u0001\u0000\u0000\u0000\u0128\u0129\u0007\u0001\u0000\u0000\u0129F\u0001"+
		"\u0000\u0000\u0000\u012a\u012b\u0005\\\u0000\u0000\u012b\u012c\u0007\b"+
		"\u0000\u0000\u012cH\u0001\u0000\u0000\u0000\u0017\u0000\u00a4\u00ac\u00af"+
		"\u00b4\u00b7\u00bc\u00c2\u00c4\u00ca\u00d8\u00dc\u00de\u00e4\u00e6\u00ef"+
		"\u00fd\u010c\u0111\u0116\u011a\u0121\u0123\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}