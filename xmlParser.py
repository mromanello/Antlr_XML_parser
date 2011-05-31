# $ANTLR 3.1.2 xmlParser.g 2011-06-01 00:09:04

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
TAG_CLOSE=6
LETTER=11
SPACE_TOKEN=20
ATTRIBUTE=18
TAG_END_OPEN=5
TEXT_TOKEN=19
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
    "WS", "PCDATA_SPACE", "ELEMENT", "ATTRIBUTE", "TEXT_TOKEN", "SPACE_TOKEN"
]




class xmlParser(Parser):
    grammarFileName = "xmlParser.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        Parser.__init__(self, input, state)


        self.dfa2 = self.DFA2(
            self, 2,
            eot = self.DFA2_eot,
            eof = self.DFA2_eof,
            min = self.DFA2_min,
            max = self.DFA2_max,
            accept = self.DFA2_accept,
            special = self.DFA2_special,
            transition = self.DFA2_transition
            )



               
        import logging
        self.logger = logging.getLogger("XMLParser")
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
        self.logger.debug("Starting to parse the document")




                
        self._adaptor = CommonTreeAdaptor()


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class document_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "document"
    # xmlParser.g:33:1: document : element ;
    def document(self, ):

        retval = self.document_return()
        retval.start = self.input.LT(1)

        root_0 = None

        element1 = None



        try:
            try:
                # xmlParser.g:33:10: ( element )
                # xmlParser.g:33:12: element
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_element_in_document86)
                element1 = self.element()

                self._state.following.pop()
                self._adaptor.addChild(root_0, element1.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "document"

    class element_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "element"
    # xmlParser.g:35:1: element : (tag= startTag ( element | text )* endTag | emptyElement ) ;
    def element(self, ):

        retval = self.element_return()
        retval.start = self.input.LT(1)

        root_0 = None

        tag = None

        element2 = None

        text3 = None

        endTag4 = None

        emptyElement5 = None



        try:
            try:
                # xmlParser.g:36:5: ( (tag= startTag ( element | text )* endTag | emptyElement ) )
                # xmlParser.g:36:7: (tag= startTag ( element | text )* endTag | emptyElement )
                pass 
                root_0 = self._adaptor.nil()

                # xmlParser.g:36:7: (tag= startTag ( element | text )* endTag | emptyElement )
                alt2 = 2
                alt2 = self.dfa2.predict(self.input)
                if alt2 == 1:
                    # xmlParser.g:36:9: tag= startTag ( element | text )* endTag
                    pass 
                    self._state.following.append(self.FOLLOW_startTag_in_element103)
                    tag = self.startTag()

                    self._state.following.pop()
                    root_0 = self._adaptor.becomeRoot(tag.tree, root_0)
                    # xmlParser.g:37:13: ( element | text )*
                    while True: #loop1
                        alt1 = 3
                        LA1_0 = self.input.LA(1)

                        if (LA1_0 == TAG_START_OPEN) :
                            alt1 = 1
                        elif (LA1_0 == PCDATA_TOKEN or LA1_0 == PCDATA_SPACE) :
                            alt1 = 2


                        if alt1 == 1:
                            # xmlParser.g:37:14: element
                            pass 
                            self._state.following.append(self.FOLLOW_element_in_element119)
                            element2 = self.element()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, element2.tree)


                        elif alt1 == 2:
                            # xmlParser.g:38:15: text
                            pass 
                            self._state.following.append(self.FOLLOW_text_in_element135)
                            text3 = self.text()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, text3.tree)


                        else:
                            break #loop1


                    self._state.following.append(self.FOLLOW_endTag_in_element164)
                    endTag4 = self.endTag()

                    self._state.following.pop()


                elif alt2 == 2:
                    # xmlParser.g:41:11: emptyElement
                    pass 
                    self._state.following.append(self.FOLLOW_emptyElement_in_element177)
                    emptyElement5 = self.emptyElement()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, emptyElement5.tree)






                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "element"

    class text_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "text"
    # xmlParser.g:45:1: text : ( token | space_token )+ ;
    def text(self, ):

        retval = self.text_return()
        retval.start = self.input.LT(1)

        root_0 = None

        token6 = None

        space_token7 = None



        try:
            try:
                # xmlParser.g:45:5: ( ( token | space_token )+ )
                # xmlParser.g:45:7: ( token | space_token )+
                pass 
                root_0 = self._adaptor.nil()

                # xmlParser.g:45:7: ( token | space_token )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 3
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == PCDATA_TOKEN) :
                        alt3 = 1
                    elif (LA3_0 == PCDATA_SPACE) :
                        alt3 = 2


                    if alt3 == 1:
                        # xmlParser.g:45:8: token
                        pass 
                        self._state.following.append(self.FOLLOW_token_in_text202)
                        token6 = self.token()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, token6.tree)


                    elif alt3 == 2:
                        # xmlParser.g:45:16: space_token
                        pass 
                        self._state.following.append(self.FOLLOW_space_token_in_text206)
                        space_token7 = self.space_token()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, space_token7.tree)


                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "text"

    class space_token_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "space_token"
    # xmlParser.g:48:1: space_token : ( PCDATA_SPACE ) -> ^( TEXT_TOKEN PCDATA_TOKEN ) ;
    def space_token(self, ):

        retval = self.space_token_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PCDATA_SPACE8 = None

        PCDATA_SPACE8_tree = None
        stream_PCDATA_SPACE = RewriteRuleTokenStream(self._adaptor, "token PCDATA_SPACE")

        try:
            try:
                # xmlParser.g:48:12: ( ( PCDATA_SPACE ) -> ^( TEXT_TOKEN PCDATA_TOKEN ) )
                # xmlParser.g:48:14: ( PCDATA_SPACE )
                pass 
                # xmlParser.g:48:14: ( PCDATA_SPACE )
                # xmlParser.g:48:15: PCDATA_SPACE
                pass 
                PCDATA_SPACE8=self.match(self.input, PCDATA_SPACE, self.FOLLOW_PCDATA_SPACE_in_space_token217) 
                stream_PCDATA_SPACE.add(PCDATA_SPACE8)




                # AST Rewrite
                # elements: 
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 50:1: -> ^( TEXT_TOKEN PCDATA_TOKEN )
                # xmlParser.g:50:4: ^( TEXT_TOKEN PCDATA_TOKEN )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TEXT_TOKEN, "TEXT_TOKEN"), root_1)

                self._adaptor.addChild(root_1, self._adaptor.createFromType(PCDATA_TOKEN, "PCDATA_TOKEN"))

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "space_token"

    class token_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "token"
    # xmlParser.g:54:1: token : (tok= PCDATA_TOKEN ( PCDATA_SPACE )* ) -> ^( SPACE_TOKEN PCDATA_TOKEN ) ;
    def token(self, ):

        retval = self.token_return()
        retval.start = self.input.LT(1)

        root_0 = None

        tok = None
        PCDATA_SPACE9 = None

        tok_tree = None
        PCDATA_SPACE9_tree = None
        stream_PCDATA_SPACE = RewriteRuleTokenStream(self._adaptor, "token PCDATA_SPACE")
        stream_PCDATA_TOKEN = RewriteRuleTokenStream(self._adaptor, "token PCDATA_TOKEN")

        try:
            try:
                # xmlParser.g:54:6: ( (tok= PCDATA_TOKEN ( PCDATA_SPACE )* ) -> ^( SPACE_TOKEN PCDATA_TOKEN ) )
                # xmlParser.g:54:8: (tok= PCDATA_TOKEN ( PCDATA_SPACE )* )
                pass 
                # xmlParser.g:54:8: (tok= PCDATA_TOKEN ( PCDATA_SPACE )* )
                # xmlParser.g:54:9: tok= PCDATA_TOKEN ( PCDATA_SPACE )*
                pass 
                tok=self.match(self.input, PCDATA_TOKEN, self.FOLLOW_PCDATA_TOKEN_in_token239) 
                stream_PCDATA_TOKEN.add(tok)
                # xmlParser.g:54:26: ( PCDATA_SPACE )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == PCDATA_SPACE) :
                        alt4 = 1


                    if alt4 == 1:
                        # xmlParser.g:54:26: PCDATA_SPACE
                        pass 
                        PCDATA_SPACE9=self.match(self.input, PCDATA_SPACE, self.FOLLOW_PCDATA_SPACE_in_token241) 
                        stream_PCDATA_SPACE.add(PCDATA_SPACE9)


                    else:
                        break #loop4






                # AST Rewrite
                # elements: PCDATA_TOKEN
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 55:1: -> ^( SPACE_TOKEN PCDATA_TOKEN )
                # xmlParser.g:55:4: ^( SPACE_TOKEN PCDATA_TOKEN )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(SPACE_TOKEN, "SPACE_TOKEN"), root_1)

                self._adaptor.addChild(root_1, stream_PCDATA_TOKEN.nextNode())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "token"

    class startTag_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "startTag"
    # xmlParser.g:59:1: startTag : TAG_START_OPEN gid= GENERIC_ID ( attribute )* TAG_CLOSE -> ^( ELEMENT GENERIC_ID ( attribute )* ) ;
    def startTag(self, ):

        retval = self.startTag_return()
        retval.start = self.input.LT(1)

        root_0 = None

        gid = None
        TAG_START_OPEN10 = None
        TAG_CLOSE12 = None
        attribute11 = None


        gid_tree = None
        TAG_START_OPEN10_tree = None
        TAG_CLOSE12_tree = None
        stream_TAG_CLOSE = RewriteRuleTokenStream(self._adaptor, "token TAG_CLOSE")
        stream_TAG_START_OPEN = RewriteRuleTokenStream(self._adaptor, "token TAG_START_OPEN")
        stream_GENERIC_ID = RewriteRuleTokenStream(self._adaptor, "token GENERIC_ID")
        stream_attribute = RewriteRuleSubtreeStream(self._adaptor, "rule attribute")
        try:
            try:
                # xmlParser.g:59:10: ( TAG_START_OPEN gid= GENERIC_ID ( attribute )* TAG_CLOSE -> ^( ELEMENT GENERIC_ID ( attribute )* ) )
                # xmlParser.g:59:12: TAG_START_OPEN gid= GENERIC_ID ( attribute )* TAG_CLOSE
                pass 
                TAG_START_OPEN10=self.match(self.input, TAG_START_OPEN, self.FOLLOW_TAG_START_OPEN_in_startTag261) 
                stream_TAG_START_OPEN.add(TAG_START_OPEN10)
                gid=self.match(self.input, GENERIC_ID, self.FOLLOW_GENERIC_ID_in_startTag265) 
                stream_GENERIC_ID.add(gid)
                # xmlParser.g:59:42: ( attribute )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == GENERIC_ID) :
                        alt5 = 1


                    if alt5 == 1:
                        # xmlParser.g:59:42: attribute
                        pass 
                        self._state.following.append(self.FOLLOW_attribute_in_startTag267)
                        attribute11 = self.attribute()

                        self._state.following.pop()
                        stream_attribute.add(attribute11.tree)


                    else:
                        break #loop5


                TAG_CLOSE12=self.match(self.input, TAG_CLOSE, self.FOLLOW_TAG_CLOSE_in_startTag270) 
                stream_TAG_CLOSE.add(TAG_CLOSE12)
                #action start
                 
                self.current_el = gid.getText();
                self.logger.debug("Found element %s"%self.current_el)

                #action end

                # AST Rewrite
                # elements: attribute, GENERIC_ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 64:9: -> ^( ELEMENT GENERIC_ID ( attribute )* )
                # xmlParser.g:64:12: ^( ELEMENT GENERIC_ID ( attribute )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ELEMENT, "ELEMENT"), root_1)

                self._adaptor.addChild(root_1, stream_GENERIC_ID.nextNode())
                # xmlParser.g:64:33: ( attribute )*
                while stream_attribute.hasNext():
                    self._adaptor.addChild(root_1, stream_attribute.nextTree())


                stream_attribute.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "startTag"

    class attribute_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "attribute"
    # xmlParser.g:67:1: attribute : GENERIC_ID ATTR_EQ ATTR_VALUE -> ^( ATTRIBUTE GENERIC_ID ATTR_VALUE ) ;
    def attribute(self, ):

        retval = self.attribute_return()
        retval.start = self.input.LT(1)

        root_0 = None

        GENERIC_ID13 = None
        ATTR_EQ14 = None
        ATTR_VALUE15 = None

        GENERIC_ID13_tree = None
        ATTR_EQ14_tree = None
        ATTR_VALUE15_tree = None
        stream_ATTR_EQ = RewriteRuleTokenStream(self._adaptor, "token ATTR_EQ")
        stream_ATTR_VALUE = RewriteRuleTokenStream(self._adaptor, "token ATTR_VALUE")
        stream_GENERIC_ID = RewriteRuleTokenStream(self._adaptor, "token GENERIC_ID")

        try:
            try:
                # xmlParser.g:67:11: ( GENERIC_ID ATTR_EQ ATTR_VALUE -> ^( ATTRIBUTE GENERIC_ID ATTR_VALUE ) )
                # xmlParser.g:67:13: GENERIC_ID ATTR_EQ ATTR_VALUE
                pass 
                GENERIC_ID13=self.match(self.input, GENERIC_ID, self.FOLLOW_GENERIC_ID_in_attribute304) 
                stream_GENERIC_ID.add(GENERIC_ID13)
                ATTR_EQ14=self.match(self.input, ATTR_EQ, self.FOLLOW_ATTR_EQ_in_attribute306) 
                stream_ATTR_EQ.add(ATTR_EQ14)
                ATTR_VALUE15=self.match(self.input, ATTR_VALUE, self.FOLLOW_ATTR_VALUE_in_attribute308) 
                stream_ATTR_VALUE.add(ATTR_VALUE15)

                # AST Rewrite
                # elements: ATTR_VALUE, GENERIC_ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 67:43: -> ^( ATTRIBUTE GENERIC_ID ATTR_VALUE )
                # xmlParser.g:67:46: ^( ATTRIBUTE GENERIC_ID ATTR_VALUE )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ATTRIBUTE, "ATTRIBUTE"), root_1)

                self._adaptor.addChild(root_1, stream_GENERIC_ID.nextNode())
                self._adaptor.addChild(root_1, stream_ATTR_VALUE.nextNode())

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "attribute"

    class endTag_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "endTag"
    # xmlParser.g:69:1: endTag : TAG_END_OPEN GENERIC_ID TAG_CLOSE ;
    def endTag(self, ):

        retval = self.endTag_return()
        retval.start = self.input.LT(1)

        root_0 = None

        TAG_END_OPEN16 = None
        GENERIC_ID17 = None
        TAG_CLOSE18 = None

        TAG_END_OPEN16_tree = None
        GENERIC_ID17_tree = None
        TAG_CLOSE18_tree = None

        try:
            try:
                # xmlParser.g:69:9: ( TAG_END_OPEN GENERIC_ID TAG_CLOSE )
                # xmlParser.g:69:11: TAG_END_OPEN GENERIC_ID TAG_CLOSE
                pass 
                root_0 = self._adaptor.nil()

                TAG_END_OPEN16=self.match(self.input, TAG_END_OPEN, self.FOLLOW_TAG_END_OPEN_in_endTag328)

                TAG_END_OPEN16_tree = self._adaptor.createWithPayload(TAG_END_OPEN16)
                self._adaptor.addChild(root_0, TAG_END_OPEN16_tree)

                GENERIC_ID17=self.match(self.input, GENERIC_ID, self.FOLLOW_GENERIC_ID_in_endTag330)

                GENERIC_ID17_tree = self._adaptor.createWithPayload(GENERIC_ID17)
                self._adaptor.addChild(root_0, GENERIC_ID17_tree)

                TAG_CLOSE18=self.match(self.input, TAG_CLOSE, self.FOLLOW_TAG_CLOSE_in_endTag332)

                TAG_CLOSE18_tree = self._adaptor.createWithPayload(TAG_CLOSE18)
                self._adaptor.addChild(root_0, TAG_CLOSE18_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "endTag"

    class emptyElement_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "emptyElement"
    # xmlParser.g:71:1: emptyElement : TAG_START_OPEN GENERIC_ID ( attribute )* TAG_EMPTY_CLOSE -> ^( ELEMENT GENERIC_ID ( attribute )* ) ;
    def emptyElement(self, ):

        retval = self.emptyElement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        TAG_START_OPEN19 = None
        GENERIC_ID20 = None
        TAG_EMPTY_CLOSE22 = None
        attribute21 = None


        TAG_START_OPEN19_tree = None
        GENERIC_ID20_tree = None
        TAG_EMPTY_CLOSE22_tree = None
        stream_TAG_EMPTY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token TAG_EMPTY_CLOSE")
        stream_TAG_START_OPEN = RewriteRuleTokenStream(self._adaptor, "token TAG_START_OPEN")
        stream_GENERIC_ID = RewriteRuleTokenStream(self._adaptor, "token GENERIC_ID")
        stream_attribute = RewriteRuleSubtreeStream(self._adaptor, "rule attribute")
        try:
            try:
                # xmlParser.g:71:14: ( TAG_START_OPEN GENERIC_ID ( attribute )* TAG_EMPTY_CLOSE -> ^( ELEMENT GENERIC_ID ( attribute )* ) )
                # xmlParser.g:71:16: TAG_START_OPEN GENERIC_ID ( attribute )* TAG_EMPTY_CLOSE
                pass 
                TAG_START_OPEN19=self.match(self.input, TAG_START_OPEN, self.FOLLOW_TAG_START_OPEN_in_emptyElement340) 
                stream_TAG_START_OPEN.add(TAG_START_OPEN19)
                GENERIC_ID20=self.match(self.input, GENERIC_ID, self.FOLLOW_GENERIC_ID_in_emptyElement342) 
                stream_GENERIC_ID.add(GENERIC_ID20)
                # xmlParser.g:71:42: ( attribute )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == GENERIC_ID) :
                        alt6 = 1


                    if alt6 == 1:
                        # xmlParser.g:71:42: attribute
                        pass 
                        self._state.following.append(self.FOLLOW_attribute_in_emptyElement344)
                        attribute21 = self.attribute()

                        self._state.following.pop()
                        stream_attribute.add(attribute21.tree)


                    else:
                        break #loop6


                TAG_EMPTY_CLOSE22=self.match(self.input, TAG_EMPTY_CLOSE, self.FOLLOW_TAG_EMPTY_CLOSE_in_emptyElement347) 
                stream_TAG_EMPTY_CLOSE.add(TAG_EMPTY_CLOSE22)

                # AST Rewrite
                # elements: GENERIC_ID, attribute
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 72:9: -> ^( ELEMENT GENERIC_ID ( attribute )* )
                # xmlParser.g:72:12: ^( ELEMENT GENERIC_ID ( attribute )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ELEMENT, "ELEMENT"), root_1)

                self._adaptor.addChild(root_1, stream_GENERIC_ID.nextNode())
                # xmlParser.g:72:33: ( attribute )*
                while stream_attribute.hasNext():
                    self._adaptor.addChild(root_1, stream_attribute.nextTree())


                stream_attribute.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "emptyElement"


    # Delegated rules


    # lookup tables for DFA #2

    DFA2_eot = DFA.unpack(
        u"\10\uffff"
        )

    DFA2_eof = DFA.unpack(
        u"\10\uffff"
        )

    DFA2_min = DFA.unpack(
        u"\1\4\1\15\1\6\1\10\2\uffff\1\11\1\6"
        )

    DFA2_max = DFA.unpack(
        u"\1\4\2\15\1\10\2\uffff\1\11\1\15"
        )

    DFA2_accept = DFA.unpack(
        u"\4\uffff\1\2\1\1\2\uffff"
        )

    DFA2_special = DFA.unpack(
        u"\10\uffff"
        )

            
    DFA2_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2"),
        DFA.unpack(u"\1\5\1\4\5\uffff\1\3"),
        DFA.unpack(u"\1\6"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\7"),
        DFA.unpack(u"\1\5\1\4\5\uffff\1\3")
    ]

    # class definition for DFA #2

    DFA2 = DFA
 

    FOLLOW_element_in_document86 = frozenset([1])
    FOLLOW_startTag_in_element103 = frozenset([4, 5, 10, 16])
    FOLLOW_element_in_element119 = frozenset([4, 5, 10, 16])
    FOLLOW_text_in_element135 = frozenset([4, 5, 10, 16])
    FOLLOW_endTag_in_element164 = frozenset([1])
    FOLLOW_emptyElement_in_element177 = frozenset([1])
    FOLLOW_token_in_text202 = frozenset([1, 4, 10, 16])
    FOLLOW_space_token_in_text206 = frozenset([1, 4, 10, 16])
    FOLLOW_PCDATA_SPACE_in_space_token217 = frozenset([1])
    FOLLOW_PCDATA_TOKEN_in_token239 = frozenset([1, 16])
    FOLLOW_PCDATA_SPACE_in_token241 = frozenset([1, 16])
    FOLLOW_TAG_START_OPEN_in_startTag261 = frozenset([13])
    FOLLOW_GENERIC_ID_in_startTag265 = frozenset([6, 13])
    FOLLOW_attribute_in_startTag267 = frozenset([6, 13])
    FOLLOW_TAG_CLOSE_in_startTag270 = frozenset([1])
    FOLLOW_GENERIC_ID_in_attribute304 = frozenset([8])
    FOLLOW_ATTR_EQ_in_attribute306 = frozenset([9])
    FOLLOW_ATTR_VALUE_in_attribute308 = frozenset([1])
    FOLLOW_TAG_END_OPEN_in_endTag328 = frozenset([13])
    FOLLOW_GENERIC_ID_in_endTag330 = frozenset([6])
    FOLLOW_TAG_CLOSE_in_endTag332 = frozenset([1])
    FOLLOW_TAG_START_OPEN_in_emptyElement340 = frozenset([13])
    FOLLOW_GENERIC_ID_in_emptyElement342 = frozenset([7, 13])
    FOLLOW_attribute_in_emptyElement344 = frozenset([7, 13])
    FOLLOW_TAG_EMPTY_CLOSE_in_emptyElement347 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("xmlParserLexer", xmlParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
