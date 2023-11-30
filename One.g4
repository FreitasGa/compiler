grammar One;

Assign: '=';
Bang: '!';
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
Dot: '.';

Whitespace: [ \t]+ -> skip;
Newline: ( '\r'? '\n' | '\r' ) -> skip;

Types: 'bool' | 'int' | 'float' | 'string';

EqualityOperation: '==' | '!=';
ComparisonOperation: '>' | '<' | '>=' | '<=';
AdditionOperation: '+' | '-';
MultiplicationOperation: '*' | '/' | '%';

BoolLiteral : 'true' | 'false';
NumberLiteral : Digit+ (Dot Digit+)?;
StringLiteral : '"' (~["\\] | EscapeSequence)* '"';

Identifier : Letter (Letter | Digit)*;
Digit : [0-9];
Letter : [a-zA-Z];

EscapeSequence : '\\' [btnr"\\];


program : statement* EOF;

statement : variable_declaration
          | assignment
          | function_declaration
          | if_statement
          | while_statement
          | for_statement
          | return_statement
          | expression_statement;

variable_declaration : Types variable_name (Assign expression)? Semicolon;

assignment : variable_name Assign expression Semicolon;

function_declaration : Types variable_name LeftParen parameters? RightParen block;

if_statement : If LeftParen expression RightParen block (Else block)?;

while_statement : While LeftParen expression RightParen block;

for_statement : For LeftParen (variable_declaration | assignment) expression Semicolon variable_name Assign expression RightParen block;

return_statement : Return expression? Semicolon;

expression_statement : expression Semicolon;

block : LeftBrace statement* RightBrace;

expression : equality;

equality : comparison (EqualityOperation comparison)*;

comparison : addition (ComparisonOperation addition)*;

addition : multiplication (AdditionOperation multiplication)*;

multiplication : unary (MultiplicationOperation unary)*;

unary : (AdditionOperation | Bang) unary | primary;

primary : BoolLiteral
        | NumberLiteral
        | StringLiteral
        | variable_name
        | LeftParen expression RightParen;

parameters : Types variable_name (Comma Types variable_name)*;

variable_name : Identifier;

