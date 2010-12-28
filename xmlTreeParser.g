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
self.current_lang = ""
self.instance_id=""
self.tokens = []
self.instances = {}
}

document : element ;

element
    : ^( ELEMENT name=GENERIC_ID 
            {self.current_el = $name.getText()
            }
            ( 
                ^(ATTRIBUTE attrName=GENERIC_ID value=ATTR_VALUE) 
                {
                if($attrName.text=="notice.num"):
                  self.instance_id=$value.getText()
                  
                }
            )*
            (element
            | ^(SPACE_TOKEN token=PCDATA_TOKEN)
                
            | ^(TEXT_TOKEN token=PCDATA_TOKEN)
            {
                if(self.current_el.lower()=="resume"):
                  self.logger.debug("\%s in \%s #\%s"\% ($token.token, self.current_el,self.instance_id));
                  self.tokens.append(token.token);
                }
            )*
            {
            if(self.current_el=="resume"):
              self.instances[self.instance_id] = self.tokens
              self.tokens = []
              self.logger.debug("\%s",self.instances)
            }
        )
    ;
