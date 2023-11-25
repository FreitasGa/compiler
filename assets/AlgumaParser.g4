grammar AlgumaParser;

WS  :   ( ' '
        | '\t'
        | '\r'
        | '\n'
        ) -> skip
    ;
DELIM	:	':'
	;
ABREPAR :	'('
	;
FECHAPAR:	')'
	;
PALAVRA_CHAVE_ATRIBUICAO
	:	'ATRIBUIR'
	;
PALAVRA_CHAVE_ENTRADA_LER
    :   'LER'
    ;
PALAVRA_CHAVE_ENTRADA_IMPRIMIR
    :   'IMPRIMIR'
    ;
PALAVRA_CHAVE_LOOP_ENQUANTO
	:  'ENQUANTO'
	;
PALAVRA_CHAVE_BLOCO_CODIGO_DECLARACOES
	:	'DECLARACOES'
	;
PALAVRA_CHAVE_BLOCO_CODIGO_FUNCOES
	:	'FUNCOES'
	;
PALAVRA_CHAVE_BLOCO_CODIGO_RETORNAR
	:	'RETORNAR'
	;
PALAVRA_CHAVE_BLOCO_CODIGO_ALGORITMO
	:	'ALGORITMO'
	;
PALAVRA_CHAVE_CONDICIONAL_SE
	:	'SE'
	;
PALAVRA_CHAVE_CONDICIONAL_ENTAO
    :   'ENTAO'
    ;
PALAVRA_CHAVE_CONDICIONAL_SENAO
    :   'SENAO'
    ;
TIPO_VAR
	:	'INTEIRO' | 'REAL' | 'CARACTERES'
	;
OP_BOOL
	:	'E' | 'OU' | 'NAO'
	;
NUMINT	: ('+'|'-')?('0'..'9')+
	;
NUMREAL	: ('+'|'-')?('0'..'9')+ ('.' ('0'..'9')+)?
	;
VARIAVEL : ('a'..'z'|'A'..'Z') ('a'..'z'|'A'..'Z'|'0'..'9')*
	 ;
FUNCAO : ('_') ('a'..'z'|'A'..'Z'|'0'..'9') ('a'..'z'|'A'..'Z'|'0'..'9')*
	 ;
CADEIA 	: '\'' ( ESC_SEQ | ~('\''|'\\') )* '\''
	;
fragment
ESC_SEQ	: '\\\'';
COMENTARIO
    :   '%' ~('\n'|'\r')* '\r'? '\n' -> skip
    ;
OP_REL	:	'>' | '>=' | '<' | '<=' | '<>' | '='
	;
OP_ARIT1	:	'+' | '-'
	;
OP_ARIT2    :	'*' | '/'
	;
OP_ARIT3    :	'**'
	;
OP_ARIT_REL :	'+=' | '-=' | '*='
	;

programaAlguma
	:	DELIM PALAVRA_CHAVE_BLOCO_CODIGO_DECLARACOES listaDeclaracoes
	    DELIM PALAVRA_CHAVE_BLOCO_CODIGO_FUNCOES listaFuncoes
	    DELIM PALAVRA_CHAVE_BLOCO_CODIGO_ALGORITMO listaComandos EOF
	;
listaDeclaracoes
	:	declaracao listaDeclaracoes | declaracao
	;
declaracao
	:	VARIAVEL DELIM TIPO_VAR
	;
expressaoAritmetica
	:	expressaoAritmetica OP_ARIT1 termoAritmeticoUm
	|	termoAritmeticoUm
	;
termoAritmeticoUm
	:	termoAritmeticoUm OP_ARIT2 termoAritmeticoDois
	|	termoAritmeticoDois
	;
termoAritmeticoDois
	:	termoAritmeticoDois OP_ARIT3 fatorAritmetico
	|	fatorAritmetico
	;
fatorAritmetico
	:	NUMINT
	|	NUMREAL
	|	VARIAVEL
	|	'(' expressaoAritmetica ')'
	;
expressaoRelacional
	:	expressaoRelacional OP_BOOL termoRelacional
	|	termoRelacional
	;
termoRelacional
	:	expressaoAritmetica OP_REL expressaoAritmetica
	|	'(' expressaoRelacional ')'
	;

listaFuncoes
	:	funcoes listaFuncoes | funcoes
	;
funcoes
	:	TIPO_VAR DELIM FUNCAO '(' parametrosFuncoesDeclaracao ')' 'EXECUTAR' comando
	;
listaComandos
	:	comando listaComandos
	|	comando
	;
comando
	:	comandoAtribuicao
	|	comandoEntrada
	|	comandoSaida
	|	comandoCondicao
	|	comandoRepeticao
    |	comandoFuncoesExecucao
    |   comandoRetorno
	|	subAlgoritmo
	;

parametrosFuncoesDeclaracao
    :  TIPO_VAR VARIAVEL ',' parametrosFuncoesDeclaracao
    |  TIPO_VAR VARIAVEL
    |
    ;
parametrosFuncoesExecucao
    :  (VARIAVEL | NUMINT) ',' parametrosFuncoesExecucao
    |  (VARIAVEL | NUMINT)
    |
    ;

comandoAtribuicao
	:	PALAVRA_CHAVE_ATRIBUICAO (expressaoAritmetica | comandoFuncoesExecucao) 'A' VARIAVEL
	;
comandoRetorno
	:	PALAVRA_CHAVE_BLOCO_CODIGO_RETORNAR (expressaoAritmetica | comandoFuncoesExecucao)
	;
comandoEntrada
	:	PALAVRA_CHAVE_ENTRADA_LER VARIAVEL
	;
comandoSaida
	:	PALAVRA_CHAVE_ENTRADA_IMPRIMIR (VARIAVEL | CADEIA)
	;
comandoCondicao
	:	PALAVRA_CHAVE_CONDICIONAL_SE expressaoRelacional PALAVRA_CHAVE_CONDICIONAL_ENTAO comando
	|	PALAVRA_CHAVE_CONDICIONAL_SE expressaoRelacional PALAVRA_CHAVE_CONDICIONAL_ENTAO comando PALAVRA_CHAVE_CONDICIONAL_SENAO comando
	;
comandoRepeticao
	:	PALAVRA_CHAVE_LOOP_ENQUANTO expressaoRelacional 'EXECUTE' comando
	;
comandoFuncoesExecucao
	:	FUNCAO '(' parametrosFuncoesExecucao ')'
	;
subAlgoritmo
	: 'INICIO' listaComandos 'FIM'
	;