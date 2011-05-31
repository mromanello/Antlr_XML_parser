# $ANTLR 3.1.2 xmlTreeParser.g 2011-05-31 22:54:24

import sys
from antlr3 import *
from antlr3.tree import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
TAG_CLOSE=6
LETTER=11
SPACE_TOKEN=19
ATTRIBUTE=18
TAG_END_OPEN=5
TEXT_TOKEN=20
PCDATA_SPACE=16
EOF=-1
PCDATA_TOKEN=10
NAMECHAR=12
TAG_EMPTY_CLOSE=7
WS=15
GENERIC_ID=13
ELEMENT=17
ATTR_EQ=8
ATTR_VALUE=9
DIGIT=14
TAG_START_OPEN=4

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "TAG_START_OPEN", "TAG_END_OPEN", "TAG_CLOSE", "TAG_EMPTY_CLOSE", "ATTR_EQ", 
    "ATTR_VALUE", "PCDATA_TOKEN", "LETTER", "NAMECHAR", "GENERIC_ID", "DIGIT", 
    "WS", "PCDATA_SPACE", "ELEMENT", "ATTRIBUTE", "SPACE_TOKEN", "TEXT_TOKEN"
]




class xmlTreeParser(TreeParser):
    grammarFileName = "xmlTreeParser.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        TreeParser.__init__(self, input, state)




               
        import logging
        self.logger = logging.getLogger("XMLTreeParser")
        self.logger.setLevel(logging.DEBUG)
        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # create formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
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




                


        



    # $ANTLR start "document"
    # xmlTreeParser.g:30:1: document : element ;
    def document(self, ):

        try:
            try:
                # xmlTreeParser.g:30:10: ( element )
                # xmlTreeParser.g:30:12: element
                pass 
                self._state.following.append(self.FOLLOW_element_in_document53)
                self.element()

                self._state.following.pop()




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "document"


    # $ANTLR start "element"
    # xmlTreeParser.g:32:1: element : ^( ELEMENT name= GENERIC_ID ( ^( ATTRIBUTE attrName= GENERIC_ID value= ATTR_VALUE ) )* ( element | ^( SPACE_TOKEN token= PCDATA_TOKEN ) | ^( TEXT_TOKEN token= PCDATA_TOKEN ) )* ) ;
    def element(self, ):

        name = None
        attrName = None
        value = None
        token = None

        try:
            try:
                # xmlTreeParser.g:33:5: ( ^( ELEMENT name= GENERIC_ID ( ^( ATTRIBUTE attrName= GENERIC_ID value= ATTR_VALUE ) )* ( element | ^( SPACE_TOKEN token= PCDATA_TOKEN ) | ^( TEXT_TOKEN token= PCDATA_TOKEN ) )* ) )
                # xmlTreeParser.g:33:7: ^( ELEMENT name= GENERIC_ID ( ^( ATTRIBUTE attrName= GENERIC_ID value= ATTR_VALUE ) )* ( element | ^( SPACE_TOKEN token= PCDATA_TOKEN ) | ^( TEXT_TOKEN token= PCDATA_TOKEN ) )* )
                pass 
                self.match(self.input, ELEMENT, self.FOLLOW_ELEMENT_in_element68)

                self.match(self.input, DOWN, None)
                name=self.match(self.input, GENERIC_ID, self.FOLLOW_GENERIC_ID_in_element72)
                #action start
                self.current_el = name.getText()
                            
                #action end
                # xmlTreeParser.g:36:13: ( ^( ATTRIBUTE attrName= GENERIC_ID value= ATTR_VALUE ) )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == ATTRIBUTE) :
                        alt1 = 1


                    if alt1 == 1:
                        # xmlTreeParser.g:37:17: ^( ATTRIBUTE attrName= GENERIC_ID value= ATTR_VALUE )
                        pass 
                        self.match(self.input, ATTRIBUTE, self.FOLLOW_ATTRIBUTE_in_element121)

                        self.match(self.input, DOWN, None)
                        attrName=self.match(self.input, GENERIC_ID, self.FOLLOW_GENERIC_ID_in_element125)
                        value=self.match(self.input, ATTR_VALUE, self.FOLLOW_ATTR_VALUE_in_element129)

                        self.match(self.input, UP, None)
                        #action start
                                         
                        if(attrName.text.lower()=="notice.num"):
                          self.instance_id=value.getText()
                        elif(self.current_el=="lang" and attrName.text.lower=="police" and value=="betagr"):
                          self.is_beta_greek = True
                                        
                        #action end


                    else:
                        break #loop1


                # xmlTreeParser.g:45:13: ( element | ^( SPACE_TOKEN token= PCDATA_TOKEN ) | ^( TEXT_TOKEN token= PCDATA_TOKEN ) )*
                while True: #loop2
                    alt2 = 4
                    LA2 = self.input.LA(1)
                    if LA2 == ELEMENT:
                        alt2 = 1
                    elif LA2 == SPACE_TOKEN:
                        alt2 = 2
                    elif LA2 == TEXT_TOKEN:
                        alt2 = 3

                    if alt2 == 1:
                        # xmlTreeParser.g:45:14: element
                        pass 
                        self._state.following.append(self.FOLLOW_element_in_element179)
                        self.element()

                        self._state.following.pop()


                    elif alt2 == 2:
                        # xmlTreeParser.g:46:15: ^( SPACE_TOKEN token= PCDATA_TOKEN )
                        pass 
                        self.match(self.input, SPACE_TOKEN, self.FOLLOW_SPACE_TOKEN_in_element196)

                        self.match(self.input, DOWN, None)
                        token=self.match(self.input, PCDATA_TOKEN, self.FOLLOW_PCDATA_TOKEN_in_element200)

                        self.match(self.input, UP, None)


                    elif alt2 == 3:
                        # xmlTreeParser.g:48:15: ^( TEXT_TOKEN token= PCDATA_TOKEN )
                        pass 
                        self.match(self.input, TEXT_TOKEN, self.FOLLOW_TEXT_TOKEN_in_element235)

                        self.match(self.input, DOWN, None)
                        token=self.match(self.input, PCDATA_TOKEN, self.FOLLOW_PCDATA_TOKEN_in_element239)

                        self.match(self.input, UP, None)
                        #action start
                                     
                        if(self.current_el.lower()=="resume"):
                          if(token.token.text.find(self.NBSP)== -1):
                           self.logger.debug("%s in %s #%s"% (token.token, self.current_el,self.instance_id));
                           #self.logger.debug("%s"% (dir(token.token)));
                           tok = {}
                           tok["start"]=token.token.start
                           tok["end"]=token.token.stop
                           tok["otext"]=token.token.text
                           from BeautifulSoup import BeautifulStoneSoup
                           tok["utext"]=BeautifulStoneSoup(tok["otext"],convertEntities=BeautifulStoneSoup.ALL_ENTITIES).encode("utf-8")
                           self.tokens.append(tok);
                            # TODO: add a check for self.current_el="lang"
                          elif(token.token.text.find("&nbsp;")!= -1):
                            # 1st token
                            tok1 = {}
                            idx = token.token.text.find("&nbsp;")
                            tok1["otext"]=token.token.text[:idx]
                            tok1["utext"]=BeautifulStoneSoup(tok1["otext"],convertEntities=BeautifulStoneSoup.ALL_ENTITIES).encode("utf-8")
                            tok1["start"]=token.token.start
                            tok1["end"]=token.token.start + (idx-1)
                            self.tokens.append(tok1);
                            # 2nd token
                            tok2 = {}
                            idx = token.token.text.find("&nbsp;")
                            tok2["otext"]=token.token.text[idx+len("&nbsp;"):len(token.token.text)]
                            tok2["utext"]=BeautifulStoneSoup(tok2["otext"],convertEntities=BeautifulStoneSoup.ALL_ENTITIES).encode("utf-8")
                            tok2["start"]=token.token.start+idx+len("&nbsp;")
                            tok2["end"]=token.token.stop
                            self.tokens.append(tok2);
                                        
                        #action end


                    else:
                        break #loop2


                #action start
                             
                if(self.current_el.lower()=="resume" and len(self.tokens) > 0):
                  self.instances[self.instance_id] = self.tokens
                  self.logger.debug("%s",self.instances)
                self.tokens = []
                            
                #action end

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "element"


    # Delegated rules


 

    FOLLOW_element_in_document53 = frozenset([1])
    FOLLOW_ELEMENT_in_element68 = frozenset([2])
    FOLLOW_GENERIC_ID_in_element72 = frozenset([3, 17, 18, 19, 20])
    FOLLOW_ATTRIBUTE_in_element121 = frozenset([2])
    FOLLOW_GENERIC_ID_in_element125 = frozenset([9])
    FOLLOW_ATTR_VALUE_in_element129 = frozenset([3])
    FOLLOW_element_in_element179 = frozenset([3, 17, 19, 20])
    FOLLOW_SPACE_TOKEN_in_element196 = frozenset([2])
    FOLLOW_PCDATA_TOKEN_in_element200 = frozenset([3])
    FOLLOW_TEXT_TOKEN_in_element235 = frozenset([2])
    FOLLOW_PCDATA_TOKEN_in_element239 = frozenset([3])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(xmlTreeParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
