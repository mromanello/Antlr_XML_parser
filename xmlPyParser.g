grammar xmlPyParser;

options {
  language=Python;
  output=template;
}

a : ID INT
    -> template(id={$ID.text}, int={$INT.text})
       "id=<id>, int=<int>"
  ;

ID : 'a'..'z'+;
INT : '0'..'9'+;
WS : (' '|'\n') {$channel=HIDDEN;} ;
