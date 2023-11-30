grammar One;

Assign: '=';
Bang: '!';
And: '&&';
Or: '||';
Comma: ',';
Semicolon: ';';
LeftParen: '(';
RightParen: ')';
LeftBrace: '{';
RightBrace: '}';
If: 'if';
Else: 'else';
Function: 'function';
Return: 'return';
While: 'while';
For: 'for';
Main: 'main';
Dot: '.';

Whitespace: [ \t]+ -> skip;
Newline: ( '\r'? '\n' | '\r' ) -> skip;

Type: 'bool' | 'int' | 'float' | 'string';

EqualityOperation: '==' | '!=';
ComparisonOperation: '>' | '<' | '>=' | '<=';
AdditionOperation: '+' | '-';
MultiplicationOperation: '*' | '/' | '%';

BoolLiteral: 'true' | 'false';
NumberLiteral: Digit+ (Dot Digit+)?;
StringLiteral: '"' (~["\\] | EscapeSequence)* '"';

Identifier: Letter (Letter | Digit)*;
Digit: [0-9];
Letter: [a-zA-Z];

EscapeSequence: '\\' [btnr"\\];


program : statement* EOF;

statement : variable_declaration
          | assignment
          | function_declaration
          | if_statement
          | while_statement
          | for_statement
          | return_statement
          | expression_statement;

variable_declaration : Type Identifier (Assign expression)? Semicolon;

assignment : Identifier Assign expression Semicolon;

function_declaration : Type (Identifier | Main) LeftParen parameters? RightParen LeftBrace statement* RightBrace;

if_statement : If LeftParen expression RightParen block (Else block)?;

while_statement : While LeftParen expression RightParen block;

for_statement : For LeftParen (variable_declaration | assignment) expression Semicolon Identifier Assign expression RightParen block;

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
        | Identifier
        | LeftParen expression RightParen;

parameters : Type Identifier (Comma Type Identifier)*;

