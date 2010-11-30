lexer grammar xmlLexer;

options {
  language = Python;
}

@init {
self.tagMode = False
self.channel = 0
import logging
self.logger = logging.getLogger("XMLLexer")
self.logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter("\%(asctime)s - \%(name)s - \%(levelname)s - \%(message)s")
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
self.logger.addHandler(ch)
self.logger.debug("Starting to tokenize the document")
}

TAG_START_OPEN : { not self.tagMode }?=> '<' { self.tagMode = True } ;
TAG_END_OPEN : {  not self.tagMode }?=> '</' { self.tagMode = True } ;
TAG_CLOSE : { self.tagMode }?=> '>' { self.tagMode = False } ;
TAG_EMPTY_CLOSE : { self.tagMode }?=> '/>' { self.tagMode = False } ;

ATTR_EQ : { self.tagMode }?=> '=' ;

// FIXME: Double and single quotes should be stripped from values!
// ! operator does not work for that any more. 
// How to get this done?
ATTR_VALUE : { self.tagMode }?=>
        ( '"' (~'"')* '"'
        | '\'' (~'\'')* '\''
        )
  ;

//PCDATA : { not self.tagMode }?=> (options {greedy=True;} : ~'<')+; 

PCDATA_TOKEN:{ not self.tagMode }?=> (//options {greedy=True;}
 : ~('<'|' '|'\r'|'\t'|'\u000C'|'\n'))+
;

GENERIC_ID 
    : { self.tagMode }?=>
      ( LETTER | '_' | ':') ( options {greedy=True;} : NAMECHAR )*
  ;

fragment NAMECHAR
  : LETTER | DIGIT | '.' | '-' | '_' | ':'
  ;

fragment DIGIT
  : '0'..'9'
  ;

fragment LETTER
  : 'a'..'z' 
  | 'A'..'Z'
  ;

WS  :  { self.tagMode }?=>
       (' '|'\r'|'\t'|'\u000C'|'\n') {$channel=99;}
    ;
    
PCDATA_SPACE:{ not self.tagMode }?=> (//options {greedy=True;}
 : (' '|'\r'|'\t'|'\u000C'|'\n'))+
;
