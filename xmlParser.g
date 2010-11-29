parser grammar xmlParser;

options {
    language = Python;
    tokenVocab=xmlLexer;
    output=AST;
}

tokens {
    ELEMENT;
    ATTRIBUTE;
    TEXT_TOKEN;
    SPACE_TOKEN;
}

@init {
import logging
self.logger = logging.getLogger("XMLParser")
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
self.logger.debug("Starting to parse the document")
}


document : element ;

element
    : ( tag=startTag^
            (element
            | text
            )*
            endTag!
        | emptyElement
        )
    ;
  
text: (token | space_token)+
;

space_token: (PCDATA_SPACE)
// for debug
-> ^(TEXT_TOKEN PCDATA_TOKEN)

;

token: (tok=PCDATA_TOKEN PCDATA_SPACE*)
-> ^(SPACE_TOKEN PCDATA_TOKEN)

;

startTag : TAG_START_OPEN gid=GENERIC_ID attribute* TAG_CLOSE
{
self.current_el = $gid.getText();
self.logger.debug("Found element \%s"\%self.current_el)
}
        -> ^(ELEMENT GENERIC_ID attribute*)
    ;

attribute : GENERIC_ID ATTR_EQ ATTR_VALUE -> ^(ATTRIBUTE GENERIC_ID ATTR_VALUE) ;

endTag! : TAG_END_OPEN GENERIC_ID TAG_CLOSE;

emptyElement : TAG_START_OPEN GENERIC_ID attribute* TAG_EMPTY_CLOSE
        -> ^(ELEMENT GENERIC_ID attribute*)
    ;

