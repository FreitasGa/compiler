grammar One;

// Regras Léxicas
TYPE_VAR: 'int' | 'float' | 'char' | 'void';
IF: 'if';
ELSE: 'else';
FOR: 'for';
WHILE: 'while';
RETURN: 'return';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUM_INT: [0-9]+;
NUM_FLOAT: [0-9]+'.'[0-9]*;
STRING: '"' ( ~["\\] | '\\' . )* '"';
SEMI: ';';
ASSIGN: '=';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
COMMA: ',';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
GT: '>';
LT: '<';
EQ: '==';
NEQ: '!=';
WS: [ \t\r\n]+ -> skip;

// Regras Sintáticas
program: (functionDecl | varDecl)*;

functionDecl: type ID LPAREN params? RPAREN compoundStmt;

params: param (COMMA param)*;
param: type ID;

type: TYPE_VAR;

varDecl: type ID (ASSIGN expr)? SEMI;

compoundStmt: LBRACE stmt* RBRACE;

stmt: exprStmt
    | ifStmt
    | forStmt
    | whileStmt
    | returnStmt
    | compoundStmt;

exprStmt: expr SEMI;
expr: expr (ADD | SUB | MUL | DIV) expr
    | ID ASSIGN expr
    | NUM_INT
    | NUM_FLOAT
    | STRING
    | ID
    | LPAREN expr RPAREN;

ifStmt: IF LPAREN expr RPAREN stmt (ELSE stmt)?;

forStmt: FOR LPAREN exprStmt? expr? SEMI expr? RPAREN stmt;

whileStmt: WHILE LPAREN expr RPAREN stmt;

returnStmt: RETURN expr? SEMI;
