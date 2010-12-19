tree grammar xmlTreeParser;
options {
    tokenVocab=xmlLexer;
    language = Python;
    ASTLabelType = Tree;
}

@init {
import logging
self.logger = logging.getLogger("XMLTreeParser")
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
self.current_el = ""
self.current_lang = "";
self.tokens = []
}

document : element ;

element
    : ^( ELEMENT name=GENERIC_ID 
            {self.current_el = $name.getText()
            }
            ( 
                ^(ATTRIBUTE attrName=GENERIC_ID value=ATTR_VALUE) 
                {#self.logger.debug(" "+$attrName.text+"="+$value.getText())
                }
            )*
            (element
            | ^(SPACE_TOKEN token=PCDATA_TOKEN)
                
            | ^(TEXT_TOKEN token=PCDATA_TOKEN)
            {
                if(self.current_el=="resume"):
                  self.logger.debug("\%s in \%s"\% ($token.token, self.current_el));
                  self.tokens.append(token.token);
                }
            )*
            { 
            #System.out.println("</"+$name.text+">"); 
            }
        )
    ;
