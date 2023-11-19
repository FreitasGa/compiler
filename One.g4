grammar One;

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
Colon : ' :';
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

Whitespace
    :   [ \t]+ -> channel(HIDDEN)
    ;

Newline
    :   (   '\r' '\n'?
        |   '\n'
        )
        -> channel(HIDDEN)
    ;