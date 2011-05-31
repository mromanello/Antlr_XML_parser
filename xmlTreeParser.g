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
self.is_beta_greek = False
self.NBSP = "&nbsp;"
}

document : element ;

element
    : ^( ELEMENT name=GENERIC_ID 
            {self.current_el = $name.getText()
            }
            ( 
                ^(ATTRIBUTE attrName=GENERIC_ID value=ATTR_VALUE) 
                {
                if($attrName.text.lower()=="notice.num"):
                  self.instance_id=$value.getText()
                elif(self.current_el=="lang" and $attrName.text.lower=="police" and $value=="betagr"):
                  self.is_beta_greek = True
                }
            )*
            (element
            | ^(SPACE_TOKEN token=PCDATA_TOKEN)
                
            | ^(TEXT_TOKEN token=PCDATA_TOKEN)
            {
                if(self.current_el.lower()=="resume"):
                  if($token.token.text.find(self.NBSP)== -1):
	                  self.logger.debug("\%s in \%s #\%s"\% ($token.token, self.current_el,self.instance_id));
	                  #self.logger.debug("\%s"\% (dir($token.token)));
	                  tok = {}
	                  tok["start"]=$token.token.start
	                  tok["end"]=$token.token.stop
	                  tok["otext"]=$token.token.text
	                  from BeautifulSoup import BeautifulStoneSoup
	                  temp=BeautifulStoneSoup(tok["otext"],convertEntities=BeautifulStoneSoup.ALL_ENTITIES)
	                  tok["utext"]=temp.encode("utf-8")
	                  self.tokens.append(tok);
                    # TODO: add a check for self.current_el="lang"
                  elif($token.token.text.find("&nbsp;")!= -1):
                    # 1st token
                    tok1 = {}
                    idx = $token.token.text.find("&nbsp;")
                    tok1["otext"]=$token.token.text[:idx]
                    from BeautifulSoup import BeautifulStoneSoup
                    tok1["utext"]=BeautifulStoneSoup(tok1["otext"],convertEntities=BeautifulStoneSoup.ALL_ENTITIES).encode("utf-8")
                    tok1["start"]=$token.token.start
                    tok1["end"]=$token.token.start + (idx-1)
                    self.tokens.append(tok1);
                    # 2nd token
                    tok2 = {}
                    idx = $token.token.text.find("&nbsp;")
                    tok2["otext"]=$token.token.text[idx+len("&nbsp;"):len($token.token.text)]
                    tok2["utext"]=BeautifulStoneSoup(tok2["otext"],convertEntities=BeautifulStoneSoup.ALL_ENTITIES).encode("utf-8")
                    tok2["start"]=$token.token.start+idx+len("&nbsp;")
                    tok2["end"]=$token.token.stop
                    self.tokens.append(tok2);
                }
            )*
            {
            if(self.current_el.lower()=="resume" and len(self.tokens) > 0):
              self.instances[self.instance_id] = self.tokens
              self.logger.debug("\%s",self.instances)
            self.tokens = []
            }
        )
    ;
