grammar One;

Assign: '=';
Plus: '+';
Minus: '-';
Asterisk: '*';
Slash: '/';
Percent: '%';
Bang: '!';
Equal: '==';
NotEqual: '!=';
Less: '<';
Greater: '>';
LessEqual: '<=';
GreaterEqual: '>=';
And: '&&';
Or: '||';
Comma: ',';
Semicolon: ';';
Colon: ':';
LeftParen: '(';
RightParen: ')';
LeftBrace: '{';
RightBrace: '}';
LeftBracket: '[';
RightBracket: ']';
If: 'if';
Else: 'else';
Function: 'function';
Return: 'return';
While: 'while';
For: 'for';
Bool: 'bool';
Int: 'int';
Float: 'float';
String: 'string';
Dot: '.';


Whitespace: [ \t]+ -> skip;
Newline: ( '\r'? '\n' | '\r' ) -> skip;


program : statement* EOF;

statement : variable_declaration
          | assignment
          | function_declaration
          | if_statement
          | while_statement
          | for_statement
          | return_statement
          | expression_statement;

variable_declaration : type variable_name (Assign expression)?;

assignment : variable_name Assign expression;

function_declaration : type variable_name LeftParen parameters? RightParen block;

if_statement : If LeftParen expression RightParen block (Else block)?;

while_statement : While LeftParen expression RightParen block;

for_statement : For LeftParen (variable_declaration | assignment)? Semicolon expression? Semicolon assignment? RightParen block;

return_statement : Return expression?;

expression_statement : expression;

block : LeftBrace statement* RightBrace;

expression : equality;

equality : comparison ((Equal | NotEqual) comparison)*;

comparison : addition ((Greater | Less | GreaterEqual | LessEqual) addition)*;

addition : multiplication ((Plus | Minus) multiplication)*;

multiplication : unary ((Asterisk | Slash | Percent) unary)*;

unary : (Plus | Minus | Bang) unary | primary;

primary : BoolLiteral
        | NumberLiteral
        | StringLiteral
        | variable_name
        | LeftParen expression RightParen;

parameters : type variable_name (Comma type variable_name)*;

type : Bool | Int | Float | String;

variable_name : Identifier;

BoolLiteral : 'true' | 'false';
NumberLiteral : Digit+ (Dot Digit+)?;
StringLiteral : '"' (~["\\] | EscapeSequence)* '"';

Identifier : Letter (Letter | Digit)*;
Digit : [0-9];
Letter : [a-zA-Z];

EscapeSequence : '\\' [btnr"\\];
