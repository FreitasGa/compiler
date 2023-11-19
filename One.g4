grammar One;

// Definição dos tokens
Assign : '=';
Plus : '+';
Minus : '-';
Asterisk : '*';
Slash : '/';
Percent : '%';
Bang : '!';
Equal : '==';
NotEqual : '!=';
Less : '<';
Greater : '>';
LessEqual : '<=';
GreaterEqual : '>=';
And : '&&';
Or : '||';
Comma : ',';
Semicolon : ';';
Colon : ':';
LeftParen : '(';
RightParen : ')';
LeftBrace : '{';
RightBrace : '}';
LeftBracket : '[';
RightBracket : ']';
If : 'if';
Else : 'else';
Function : 'function';
Return : 'return';
While : 'while';
For : 'for';
Bool : 'bool';
Int : 'int';
Float : 'float';
String : 'string';
Dot : '.';


// Ignorar espaços e quebras de linha
Whitespace : [ \t]+ -> skip;
Newline : ( '\r'? '\n' | '\r' ) -> skip;

// Regras de análise sintática

// Programa
program : statement* EOF;

// Comandos
statement : variableDecl
          | assignment
          | functionDecl
          | ifStatement
          | whileStatement
          | forStatement
          | returnStatement
          | expressionStatement;

variableDecl : type variableName (Assign expression)? Semicolon;

assignment : variableName Assign expression Semicolon;

functionDecl : Function type variableName LeftParen parameters? RightParen block;

ifStatement : If LeftParen expression RightParen block (Else block)?;

whileStatement : While LeftParen expression RightParen block;

forStatement : For LeftParen (variableDecl | assignment)? Semicolon expression? Semicolon assignment? RightParen block;

returnStatement : Return expression? Semicolon;

expressionStatement : expression Semicolon;

block : LeftBrace statement* RightBrace;

// Expressões
expression : equality;

equality : comparison ((Equal | NotEqual) comparison)*;

comparison : addition ((Greater | Less | GreaterEqual | LessEqual) addition)*;

addition : multiplication ((Plus | Minus) multiplication)*;

multiplication : unary ((Asterisk | Slash | Percent) unary)*;

unary : (Plus | Minus | Bang) unary | primary;

primary : Number
        | BoolLiteral
        | variableName
        | LeftParen expression RightParen;

// Parâmetros e argumentos
parameters : type variableName (Comma type variableName)*;

// Tipos de variáveis
type : Bool | Int | Float | String;

// Nomes de variáveis
variableName : Identifier;

// Literais
BoolLiteral : 'true' | 'false';
Number : Digit+ (Dot Digit+)?;
StringLiteral : '"' (~["\\] | EscapeSequence)* '"';

Identifier : Letter (Letter | Digit)*;
Digit : [0-9];
Letter : [a-zA-Z];

// Sequências de escape
EscapeSequence : '\\' [btnr"\\];
