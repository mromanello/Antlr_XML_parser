# $ANTLR 3.1.2 /Users/56k/Documents/workspace/24-11/xml_parser/xmlPyParser.g 2010-12-19 17:57:02

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
import stringtemplate3


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
WS=6
INT=5
ID=4
EOF=-1

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "ID", "INT", "WS"
]




class xmlPyParserParser(Parser):
    grammarFileName = "/Users/56k/Documents/workspace/24-11/xml_parser/xmlPyParser.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        Parser.__init__(self, input, state)







                
        self.templateLib = stringtemplate3.StringTemplateGroup(
            'xmlPyParserParserTemplates', lexer='angle-bracket'
            )



        
    def setTemplateLib(self, templateLib):
        self.templateLib = templateLib

    def getTemplateLib(self):
        return self.templateLib



    class a_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.st = None


        def getTemplate(self):
            return self.st

        def toString(self):
            if self.st is not None:
                return self.st.toString()
            return None
        __str__ = toString



    # $ANTLR start "a"
    # /Users/56k/Documents/workspace/24-11/xml_parser/xmlPyParser.g:8:1: a : ID INT -> template(id=$ID.textint=$INT.text) \"id=<id>, int=<int>\";
    def a(self, ):

        retval = self.a_return()
        retval.start = self.input.LT(1)

        ID1 = None
        INT2 = None

        try:
            try:
                # /Users/56k/Documents/workspace/24-11/xml_parser/xmlPyParser.g:8:3: ( ID INT -> template(id=$ID.textint=$INT.text) \"id=<id>, int=<int>\")
                # /Users/56k/Documents/workspace/24-11/xml_parser/xmlPyParser.g:8:5: ID INT
                pass 
                ID1=self.match(self.input, ID, self.FOLLOW_ID_in_a29)
                INT2=self.match(self.input, INT, self.FOLLOW_INT_in_a31)

                # TEMPLATE REWRITE
                # 9:5: -> template(id=$ID.textint=$INT.text) \"id=<id>, int=<int>\"
                retval.st = stringtemplate3.StringTemplate(
                    "id=<id>, int=<int>",
                    group=self.templateLib,
                    attributes={"id": ID1.text, "int": INT2.text}
                    )





                retval.stop = self.input.LT(-1)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end "a"


    # Delegated rules


 

    FOLLOW_ID_in_a29 = frozenset([5])
    FOLLOW_INT_in_a31 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("xmlPyParserLexer", xmlPyParserParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
