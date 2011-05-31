# $ANTLR 3.1.2 xmlLexer.g 2011-06-01 01:31:01

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
TAG_EMPTY_CLOSE=7
WS=15
TAG_CLOSE=6
LETTER=11
GENERIC_ID=13
ATTR_EQ=8
ATTR_VALUE=9
TAG_END_OPEN=5
DIGIT=14
PCDATA_SPACE=16
EOF=-1
PCDATA_TOKEN=10
TAG_START_OPEN=4
NAMECHAR=12


class xmlLexer(Lexer):

    grammarFileName = "xmlLexer.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)

        self.dfa7 = self.DFA7(
            self, 7,
            eot = self.DFA7_eot,
            eof = self.DFA7_eof,
            min = self.DFA7_min,
            max = self.DFA7_max,
            accept = self.DFA7_accept,
            special = self.DFA7_special,
            transition = self.DFA7_transition
            )


               
        self.tagMode = False
        self.channel = 0
        import logging
        self.logger = logging.getLogger("XMLLexer")
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
        self.logger.debug("Starting to tokenize the document")





    # $ANTLR start "TAG_START_OPEN"
    def mTAG_START_OPEN(self, ):

        try:
            _type = TAG_START_OPEN
            _channel = DEFAULT_CHANNEL

            # xmlLexer.g:25:16: ({...}? => '<' )
            # xmlLexer.g:25:18: {...}? => '<'
            pass 
            if not ((not self.tagMode )):
                raise FailedPredicateException(self.input, "TAG_START_OPEN", " not self.tagMode ")

            self.match(60)
            #action start
            self.tagMode = True 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TAG_START_OPEN"



    # $ANTLR start "TAG_END_OPEN"
    def mTAG_END_OPEN(self, ):

        try:
            _type = TAG_END_OPEN
            _channel = DEFAULT_CHANNEL

            # xmlLexer.g:26:14: ({...}? => '</' )
            # xmlLexer.g:26:16: {...}? => '</'
            pass 
            if not ((not self.tagMode )):
                raise FailedPredicateException(self.input, "TAG_END_OPEN", "  not self.tagMode ")

            self.match("</")
            #action start
            self.tagMode = True 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TAG_END_OPEN"



    # $ANTLR start "TAG_CLOSE"
    def mTAG_CLOSE(self, ):

        try:
            _type = TAG_CLOSE
            _channel = DEFAULT_CHANNEL

            # xmlLexer.g:27:11: ({...}? => '>' )
            # xmlLexer.g:27:13: {...}? => '>'
            pass 
            if not ((self.tagMode )):
                raise FailedPredicateException(self.input, "TAG_CLOSE", " self.tagMode ")

            self.match(62)
            #action start
            self.tagMode = False 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TAG_CLOSE"



    # $ANTLR start "TAG_EMPTY_CLOSE"
    def mTAG_EMPTY_CLOSE(self, ):

        try:
            _type = TAG_EMPTY_CLOSE
            _channel = DEFAULT_CHANNEL

            # xmlLexer.g:28:17: ({...}? => '/>' )
            # xmlLexer.g:28:19: {...}? => '/>'
            pass 
            if not ((self.tagMode )):
                raise FailedPredicateException(self.input, "TAG_EMPTY_CLOSE", " self.tagMode ")

            self.match("/>")
            #action start
            self.tagMode = False 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TAG_EMPTY_CLOSE"



    # $ANTLR start "ATTR_EQ"
    def mATTR_EQ(self, ):

        try:
            _type = ATTR_EQ
            _channel = DEFAULT_CHANNEL

            # xmlLexer.g:30:9: ({...}? => '=' )
            # xmlLexer.g:30:11: {...}? => '='
            pass 
            if not ((self.tagMode )):
                raise FailedPredicateException(self.input, "ATTR_EQ", " self.tagMode ")

            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ATTR_EQ"



    # $ANTLR start "ATTR_VALUE"
    def mATTR_VALUE(self, ):

        try:
            _type = ATTR_VALUE
            _channel = DEFAULT_CHANNEL

            # xmlLexer.g:35:12: ({...}? => ( '\"' (~ '\"' )* '\"' | '\\'' (~ '\\'' )* '\\'' ) )
            # xmlLexer.g:35:14: {...}? => ( '\"' (~ '\"' )* '\"' | '\\'' (~ '\\'' )* '\\'' )
            pass 
            if not ((self.tagMode )):
                raise FailedPredicateException(self.input, "ATTR_VALUE", " self.tagMode ")

            # xmlLexer.g:36:9: ( '\"' (~ '\"' )* '\"' | '\\'' (~ '\\'' )* '\\'' )
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == 34) :
                alt3 = 1
            elif (LA3_0 == 39) :
                alt3 = 2
            else:
                nvae = NoViableAltException("", 3, 0, self.input)

                raise nvae

            if alt3 == 1:
                # xmlLexer.g:36:11: '\"' (~ '\"' )* '\"'
                pass 
                self.match(34)
                # xmlLexer.g:36:15: (~ '\"' )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((0 <= LA1_0 <= 33) or (35 <= LA1_0 <= 65535)) :
                        alt1 = 1


                    if alt1 == 1:
                        # xmlLexer.g:36:16: ~ '\"'
                        pass 
                        if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop1


                self.match(34)


            elif alt3 == 2:
                # xmlLexer.g:37:11: '\\'' (~ '\\'' )* '\\''
                pass 
                self.match(39)
                # xmlLexer.g:37:16: (~ '\\'' )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((0 <= LA2_0 <= 38) or (40 <= LA2_0 <= 65535)) :
                        alt2 = 1


                    if alt2 == 1:
                        # xmlLexer.g:37:17: ~ '\\''
                        pass 
                        if (0 <= self.input.LA(1) <= 38) or (40 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop2


                self.match(39)






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ATTR_VALUE"



    # $ANTLR start "PCDATA_TOKEN"
    def mPCDATA_TOKEN(self, ):

        try:
            _type = PCDATA_TOKEN
            _channel = DEFAULT_CHANNEL

            # xmlLexer.g:43:13: ({...}? => (~ ( '<' | ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' ) )+ )
            # xmlLexer.g:43:14: {...}? => (~ ( '<' | ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' ) )+
            pass 
            if not ((not self.tagMode )):
                raise FailedPredicateException(self.input, "PCDATA_TOKEN", " not self.tagMode ")

            # xmlLexer.g:43:38: (~ ( '<' | ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' ) )+
            cnt4 = 0
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((0 <= LA4_0 <= 8) or LA4_0 == 11 or (14 <= LA4_0 <= 31) or (33 <= LA4_0 <= 59) or (61 <= LA4_0 <= 65535)) :
                    alt4 = 1


                if alt4 == 1:
                    # xmlLexer.g:44:4: ~ ( '<' | ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' )
                    pass 
                    if (0 <= self.input.LA(1) <= 8) or self.input.LA(1) == 11 or (14 <= self.input.LA(1) <= 31) or (33 <= self.input.LA(1) <= 59) or (61 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt4 >= 1:
                        break #loop4

                    eee = EarlyExitException(4, self.input)
                    raise eee

                cnt4 += 1





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PCDATA_TOKEN"



    # $ANTLR start "GENERIC_ID"
    def mGENERIC_ID(self, ):

        try:
            _type = GENERIC_ID
            _channel = DEFAULT_CHANNEL

            # xmlLexer.g:48:5: ({...}? => ( LETTER | '_' | ':' ) ( options {greedy=True; } : NAMECHAR )* )
            # xmlLexer.g:48:7: {...}? => ( LETTER | '_' | ':' ) ( options {greedy=True; } : NAMECHAR )*
            pass 
            if not ((self.tagMode )):
                raise FailedPredicateException(self.input, "GENERIC_ID", " self.tagMode ")

            if self.input.LA(1) == 58 or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # xmlLexer.g:49:29: ( options {greedy=True; } : NAMECHAR )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((45 <= LA5_0 <= 46) or (48 <= LA5_0 <= 58) or (65 <= LA5_0 <= 90) or LA5_0 == 95 or (97 <= LA5_0 <= 122)) :
                    alt5 = 1


                if alt5 == 1:
                    # xmlLexer.g:49:56: NAMECHAR
                    pass 
                    self.mNAMECHAR()


                else:
                    break #loop5





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GENERIC_ID"



    # $ANTLR start "NAMECHAR"
    def mNAMECHAR(self, ):

        try:
            # xmlLexer.g:53:3: ( LETTER | DIGIT | '.' | '-' | '_' | ':' )
            # xmlLexer.g:
            pass 
            if (45 <= self.input.LA(1) <= 46) or (48 <= self.input.LA(1) <= 58) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "NAMECHAR"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):

        try:
            # xmlLexer.g:57:3: ( '0' .. '9' )
            # xmlLexer.g:57:5: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    # $ANTLR start "LETTER"
    def mLETTER(self, ):

        try:
            # xmlLexer.g:61:3: ( 'a' .. 'z' | 'A' .. 'Z' )
            # xmlLexer.g:
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "LETTER"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # xmlLexer.g:65:5: ({...}? => ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' ) )
            # xmlLexer.g:65:8: {...}? => ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' )
            pass 
            if not ((self.tagMode )):
                raise FailedPredicateException(self.input, "WS", " self.tagMode ")

            if (9 <= self.input.LA(1) <= 10) or (12 <= self.input.LA(1) <= 13) or self.input.LA(1) == 32:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            #action start
            _channel=99;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    # $ANTLR start "PCDATA_SPACE"
    def mPCDATA_SPACE(self, ):

        try:
            _type = PCDATA_SPACE
            _channel = DEFAULT_CHANNEL

            # xmlLexer.g:69:13: ({...}? => ( ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' ) )+ )
            # xmlLexer.g:69:14: {...}? => ( ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' ) )+
            pass 
            if not ((not self.tagMode )):
                raise FailedPredicateException(self.input, "PCDATA_SPACE", " not self.tagMode ")

            # xmlLexer.g:69:38: ( ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' ) )+
            cnt6 = 0
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((9 <= LA6_0 <= 10) or (12 <= LA6_0 <= 13) or LA6_0 == 32) :
                    alt6 = 1


                if alt6 == 1:
                    # xmlLexer.g:70:4: ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' )
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or (12 <= self.input.LA(1) <= 13) or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt6 >= 1:
                        break #loop6

                    eee = EarlyExitException(6, self.input)
                    raise eee

                cnt6 += 1





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PCDATA_SPACE"



    def mTokens(self):
        # xmlLexer.g:1:8: ( TAG_START_OPEN | TAG_END_OPEN | TAG_CLOSE | TAG_EMPTY_CLOSE | ATTR_EQ | ATTR_VALUE | PCDATA_TOKEN | GENERIC_ID | WS | PCDATA_SPACE )
        alt7 = 10
        alt7 = self.dfa7.predict(self.input)
        if alt7 == 1:
            # xmlLexer.g:1:10: TAG_START_OPEN
            pass 
            self.mTAG_START_OPEN()


        elif alt7 == 2:
            # xmlLexer.g:1:25: TAG_END_OPEN
            pass 
            self.mTAG_END_OPEN()


        elif alt7 == 3:
            # xmlLexer.g:1:38: TAG_CLOSE
            pass 
            self.mTAG_CLOSE()


        elif alt7 == 4:
            # xmlLexer.g:1:48: TAG_EMPTY_CLOSE
            pass 
            self.mTAG_EMPTY_CLOSE()


        elif alt7 == 5:
            # xmlLexer.g:1:64: ATTR_EQ
            pass 
            self.mATTR_EQ()


        elif alt7 == 6:
            # xmlLexer.g:1:72: ATTR_VALUE
            pass 
            self.mATTR_VALUE()


        elif alt7 == 7:
            # xmlLexer.g:1:83: PCDATA_TOKEN
            pass 
            self.mPCDATA_TOKEN()


        elif alt7 == 8:
            # xmlLexer.g:1:96: GENERIC_ID
            pass 
            self.mGENERIC_ID()


        elif alt7 == 9:
            # xmlLexer.g:1:107: WS
            pass 
            self.mWS()


        elif alt7 == 10:
            # xmlLexer.g:1:110: PCDATA_SPACE
            pass 
            self.mPCDATA_SPACE()







    # lookup tables for DFA #7

    DFA7_eot = DFA.unpack(
        u"\1\uffff\1\13\1\14\1\10\1\16\2\10\1\25\1\uffff\1\26\3\uffff\1\31"
        u"\1\uffff\1\10\1\33\1\uffff\1\10\1\33\1\25\12\uffff"
        )

    DFA7_eof = DFA.unpack(
        u"\37\uffff"
        )

    DFA7_min = DFA.unpack(
        u"\1\0\1\57\1\0\1\76\4\0\1\uffff\1\11\2\uffff\5\0\1\uffff\5\0\2\uffff"
        u"\1\0\1\uffff\1\0\3\uffff"
        )

    DFA7_max = DFA.unpack(
        u"\1\uffff\1\57\1\uffff\1\76\4\uffff\1\uffff\1\40\2\uffff\1\0\1\uffff"
        u"\1\0\2\uffff\1\uffff\3\uffff\2\0\2\uffff\1\0\1\uffff\1\0\3\uffff"
        )

    DFA7_accept = DFA.unpack(
        u"\10\uffff\1\7\1\uffff\1\2\1\1\5\uffff\1\6\5\uffff\1\12\1\3\1\uffff"
        u"\1\5\1\uffff\1\10\1\11\1\4"
        )

    DFA7_special = DFA.unpack(
        u"\1\16\1\14\1\23\1\15\1\12\1\1\1\4\1\21\1\uffff\1\7\2\uffff\1\17"
        u"\1\3\1\10\1\24\1\0\1\uffff\1\2\1\22\1\13\1\11\1\5\2\uffff\1\20"
        u"\1\uffff\1\6\3\uffff"
        )

            
    DFA7_transition = [
        DFA.unpack(u"\11\10\2\11\1\10\2\11\22\10\1\11\1\10\1\5\4\10\1\6\7"
        u"\10\1\3\12\10\1\7\1\10\1\1\1\4\1\2\2\10\32\7\4\10\1\7\1\10\32\7"
        u"\uff85\10"),
        DFA.unpack(u"\1\12"),
        DFA.unpack(u"\11\10\2\uffff\1\10\2\uffff\22\10\1\uffff\33\10\1\uffff"
        u"\uffc3\10"),
        DFA.unpack(u"\1\15"),
        DFA.unpack(u"\11\10\2\uffff\1\10\2\uffff\22\10\1\uffff\33\10\1\uffff"
        u"\uffc3\10"),
        DFA.unpack(u"\11\17\2\21\1\17\2\21\22\17\1\21\1\17\1\20\31\17\1"
        u"\21\uffc3\17"),
        DFA.unpack(u"\11\22\2\21\1\22\2\21\22\22\1\21\6\22\1\23\24\22\1"
        u"\21\uffc3\22"),
        DFA.unpack(u"\11\10\2\uffff\1\10\2\uffff\22\10\1\uffff\14\10\2\24"
        u"\1\10\13\24\1\10\1\uffff\4\10\32\24\4\10\1\24\1\10\32\24\uff85"
        u"\10"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\1\uffff\2\27\22\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\11\10\2\uffff\1\10\2\uffff\22\10\1\uffff\33\10\1\uffff"
        u"\uffc3\10"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\11\17\2\21\1\17\2\21\22\17\1\21\1\17\1\20\31\17\1"
        u"\21\uffc3\17"),
        DFA.unpack(u"\11\10\2\uffff\1\10\2\uffff\22\10\1\uffff\33\10\1\uffff"
        u"\uffc3\10"),
        DFA.unpack(u""),
        DFA.unpack(u"\11\22\2\21\1\22\2\21\22\22\1\21\6\22\1\23\24\22\1"
        u"\21\uffc3\22"),
        DFA.unpack(u"\11\10\2\uffff\1\10\2\uffff\22\10\1\uffff\33\10\1\uffff"
        u"\uffc3\10"),
        DFA.unpack(u"\11\10\2\uffff\1\10\2\uffff\22\10\1\uffff\14\10\2\24"
        u"\1\10\13\24\1\10\1\uffff\4\10\32\24\4\10\1\24\1\10\32\24\uff85"
        u"\10"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #7

    class DFA7(DFA):
        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA7_16 = input.LA(1)

                 
                index7_16 = input.index()
                input.rewind()
                s = -1
                if ((0 <= LA7_16 <= 8) or LA7_16 == 11 or (14 <= LA7_16 <= 31) or (33 <= LA7_16 <= 59) or (61 <= LA7_16 <= 65535)) and ((not self.tagMode )):
                    s = 8

                else:
                    s = 27

                 
                input.seek(index7_16)
                if s >= 0:
                    return s
            elif s == 1: 
                LA7_5 = input.LA(1)

                 
                index7_5 = input.index()
                input.rewind()
                s = -1
                if ((0 <= LA7_5 <= 8) or LA7_5 == 11 or (14 <= LA7_5 <= 31) or LA7_5 == 33 or (35 <= LA7_5 <= 59) or (61 <= LA7_5 <= 65535)) and (((self.tagMode ) or (not self.tagMode ))):
                    s = 15

                elif (LA7_5 == 34) and (((self.tagMode ) or (not self.tagMode ))):
                    s = 16

                elif ((9 <= LA7_5 <= 10) or (12 <= LA7_5 <= 13) or LA7_5 == 32 or LA7_5 == 60) and ((self.tagMode )):
                    s = 17

                else:
                    s = 8

                 
                input.seek(index7_5)
                if s >= 0:
                    return s
            elif s == 2: 
                LA7_18 = input.LA(1)

                 
                index7_18 = input.index()
                input.rewind()
                s = -1
                if (LA7_18 == 39) and (((self.tagMode ) or (not self.tagMode ))):
                    s = 19

                elif ((0 <= LA7_18 <= 8) or LA7_18 == 11 or (14 <= LA7_18 <= 31) or (33 <= LA7_18 <= 38) or (40 <= LA7_18 <= 59) or (61 <= LA7_18 <= 65535)) and (((self.tagMode ) or (not self.tagMode ))):
                    s = 18

                elif ((9 <= LA7_18 <= 10) or (12 <= LA7_18 <= 13) or LA7_18 == 32 or LA7_18 == 60) and ((self.tagMode )):
                    s = 17

                else:
                    s = 8

                 
                input.seek(index7_18)
                if s >= 0:
                    return s
            elif s == 3: 
                LA7_13 = input.LA(1)

                 
                index7_13 = input.index()
                input.rewind()
                s = -1
                if ((0 <= LA7_13 <= 8) or LA7_13 == 11 or (14 <= LA7_13 <= 31) or (33 <= LA7_13 <= 59) or (61 <= LA7_13 <= 65535)) and ((not self.tagMode )):
                    s = 8

                else:
                    s = 25

                 
                input.seek(index7_13)
                if s >= 0:
                    return s
            elif s == 4: 
                LA7_6 = input.LA(1)

                 
                index7_6 = input.index()
                input.rewind()
                s = -1
                if ((0 <= LA7_6 <= 8) or LA7_6 == 11 or (14 <= LA7_6 <= 31) or (33 <= LA7_6 <= 38) or (40 <= LA7_6 <= 59) or (61 <= LA7_6 <= 65535)) and (((self.tagMode ) or (not self.tagMode ))):
                    s = 18

                elif (LA7_6 == 39) and (((self.tagMode ) or (not self.tagMode ))):
                    s = 19

                elif ((9 <= LA7_6 <= 10) or (12 <= LA7_6 <= 13) or LA7_6 == 32 or LA7_6 == 60) and ((self.tagMode )):
                    s = 17

                else:
                    s = 8

                 
                input.seek(index7_6)
                if s >= 0:
                    return s
            elif s == 5: 
                LA7_22 = input.LA(1)

                 
                index7_22 = input.index()
                input.rewind()
                s = -1
                if ((self.tagMode )):
                    s = 29

                elif ((not self.tagMode )):
                    s = 23

                 
                input.seek(index7_22)
                if s >= 0:
                    return s
            elif s == 6: 
                LA7_27 = input.LA(1)

                 
                index7_27 = input.index()
                input.rewind()
                s = -1
                if ((self.tagMode )):
                    s = 17

                elif ((not self.tagMode )):
                    s = 8

                 
                input.seek(index7_27)
                if s >= 0:
                    return s
            elif s == 7: 
                LA7_9 = input.LA(1)

                 
                index7_9 = input.index()
                input.rewind()
                s = -1
                if ((9 <= LA7_9 <= 10) or (12 <= LA7_9 <= 13) or LA7_9 == 32) and ((not self.tagMode )):
                    s = 23

                else:
                    s = 22

                 
                input.seek(index7_9)
                if s >= 0:
                    return s
            elif s == 8: 
                LA7_14 = input.LA(1)

                 
                index7_14 = input.index()
                input.rewind()
                s = -1
                if ((self.tagMode )):
                    s = 26

                elif ((not self.tagMode )):
                    s = 8

                 
                input.seek(index7_14)
                if s >= 0:
                    return s
            elif s == 9: 
                LA7_21 = input.LA(1)

                 
                index7_21 = input.index()
                input.rewind()
                s = -1
                if ((not self.tagMode )):
                    s = 8

                elif ((self.tagMode )):
                    s = 28

                 
                input.seek(index7_21)
                if s >= 0:
                    return s
            elif s == 10: 
                LA7_4 = input.LA(1)

                 
                index7_4 = input.index()
                input.rewind()
                s = -1
                if ((0 <= LA7_4 <= 8) or LA7_4 == 11 or (14 <= LA7_4 <= 31) or (33 <= LA7_4 <= 59) or (61 <= LA7_4 <= 65535)) and ((not self.tagMode )):
                    s = 8

                else:
                    s = 14

                 
                input.seek(index7_4)
                if s >= 0:
                    return s
            elif s == 11: 
                LA7_20 = input.LA(1)

                 
                index7_20 = input.index()
                input.rewind()
                s = -1
                if ((45 <= LA7_20 <= 46) or (48 <= LA7_20 <= 58) or (65 <= LA7_20 <= 90) or LA7_20 == 95 or (97 <= LA7_20 <= 122)) and (((self.tagMode ) or (not self.tagMode ))):
                    s = 20

                elif ((0 <= LA7_20 <= 8) or LA7_20 == 11 or (14 <= LA7_20 <= 31) or (33 <= LA7_20 <= 44) or LA7_20 == 47 or LA7_20 == 59 or (61 <= LA7_20 <= 64) or (91 <= LA7_20 <= 94) or LA7_20 == 96 or (123 <= LA7_20 <= 65535)) and ((not self.tagMode )):
                    s = 8

                else:
                    s = 21

                 
                input.seek(index7_20)
                if s >= 0:
                    return s
            elif s == 12: 
                LA7_1 = input.LA(1)

                 
                index7_1 = input.index()
                input.rewind()
                s = -1
                if (LA7_1 == 47) and ((not self.tagMode )):
                    s = 10

                else:
                    s = 11

                 
                input.seek(index7_1)
                if s >= 0:
                    return s
            elif s == 13: 
                LA7_3 = input.LA(1)

                 
                index7_3 = input.index()
                input.rewind()
                s = -1
                if (LA7_3 == 62) and (((self.tagMode ) or (not self.tagMode ))):
                    s = 13

                else:
                    s = 8

                 
                input.seek(index7_3)
                if s >= 0:
                    return s
            elif s == 14: 
                LA7_0 = input.LA(1)

                 
                index7_0 = input.index()
                input.rewind()
                s = -1
                if (LA7_0 == 60) and (((not self.tagMode ) or (not self.tagMode ))):
                    s = 1

                elif (LA7_0 == 62) and (((self.tagMode ) or (not self.tagMode ))):
                    s = 2

                elif (LA7_0 == 47) and (((self.tagMode ) or (not self.tagMode ))):
                    s = 3

                elif (LA7_0 == 61) and (((self.tagMode ) or (not self.tagMode ))):
                    s = 4

                elif (LA7_0 == 34) and (((self.tagMode ) or (not self.tagMode ))):
                    s = 5

                elif (LA7_0 == 39) and (((self.tagMode ) or (not self.tagMode ))):
                    s = 6

                elif (LA7_0 == 58 or (65 <= LA7_0 <= 90) or LA7_0 == 95 or (97 <= LA7_0 <= 122)) and (((self.tagMode ) or (not self.tagMode ))):
                    s = 7

                elif ((0 <= LA7_0 <= 8) or LA7_0 == 11 or (14 <= LA7_0 <= 31) or LA7_0 == 33 or (35 <= LA7_0 <= 38) or (40 <= LA7_0 <= 46) or (48 <= LA7_0 <= 57) or LA7_0 == 59 or (63 <= LA7_0 <= 64) or (91 <= LA7_0 <= 94) or LA7_0 == 96 or (123 <= LA7_0 <= 65535)) and ((not self.tagMode )):
                    s = 8

                elif ((9 <= LA7_0 <= 10) or (12 <= LA7_0 <= 13) or LA7_0 == 32) and (((self.tagMode ) or (not self.tagMode ))):
                    s = 9

                 
                input.seek(index7_0)
                if s >= 0:
                    return s
            elif s == 15: 
                LA7_12 = input.LA(1)

                 
                index7_12 = input.index()
                input.rewind()
                s = -1
                if ((self.tagMode )):
                    s = 24

                elif ((not self.tagMode )):
                    s = 8

                 
                input.seek(index7_12)
                if s >= 0:
                    return s
            elif s == 16: 
                LA7_25 = input.LA(1)

                 
                index7_25 = input.index()
                input.rewind()
                s = -1
                if ((self.tagMode )):
                    s = 30

                elif ((not self.tagMode )):
                    s = 8

                 
                input.seek(index7_25)
                if s >= 0:
                    return s
            elif s == 17: 
                LA7_7 = input.LA(1)

                 
                index7_7 = input.index()
                input.rewind()
                s = -1
                if ((45 <= LA7_7 <= 46) or (48 <= LA7_7 <= 58) or (65 <= LA7_7 <= 90) or LA7_7 == 95 or (97 <= LA7_7 <= 122)) and (((self.tagMode ) or (not self.tagMode ))):
                    s = 20

                elif ((0 <= LA7_7 <= 8) or LA7_7 == 11 or (14 <= LA7_7 <= 31) or (33 <= LA7_7 <= 44) or LA7_7 == 47 or LA7_7 == 59 or (61 <= LA7_7 <= 64) or (91 <= LA7_7 <= 94) or LA7_7 == 96 or (123 <= LA7_7 <= 65535)) and ((not self.tagMode )):
                    s = 8

                else:
                    s = 21

                 
                input.seek(index7_7)
                if s >= 0:
                    return s
            elif s == 18: 
                LA7_19 = input.LA(1)

                 
                index7_19 = input.index()
                input.rewind()
                s = -1
                if ((0 <= LA7_19 <= 8) or LA7_19 == 11 or (14 <= LA7_19 <= 31) or (33 <= LA7_19 <= 59) or (61 <= LA7_19 <= 65535)) and ((not self.tagMode )):
                    s = 8

                else:
                    s = 27

                 
                input.seek(index7_19)
                if s >= 0:
                    return s
            elif s == 19: 
                LA7_2 = input.LA(1)

                 
                index7_2 = input.index()
                input.rewind()
                s = -1
                if ((0 <= LA7_2 <= 8) or LA7_2 == 11 or (14 <= LA7_2 <= 31) or (33 <= LA7_2 <= 59) or (61 <= LA7_2 <= 65535)) and ((not self.tagMode )):
                    s = 8

                else:
                    s = 12

                 
                input.seek(index7_2)
                if s >= 0:
                    return s
            elif s == 20: 
                LA7_15 = input.LA(1)

                 
                index7_15 = input.index()
                input.rewind()
                s = -1
                if (LA7_15 == 34) and (((self.tagMode ) or (not self.tagMode ))):
                    s = 16

                elif ((0 <= LA7_15 <= 8) or LA7_15 == 11 or (14 <= LA7_15 <= 31) or LA7_15 == 33 or (35 <= LA7_15 <= 59) or (61 <= LA7_15 <= 65535)) and (((self.tagMode ) or (not self.tagMode ))):
                    s = 15

                elif ((9 <= LA7_15 <= 10) or (12 <= LA7_15 <= 13) or LA7_15 == 32 or LA7_15 == 60) and ((self.tagMode )):
                    s = 17

                else:
                    s = 8

                 
                input.seek(index7_15)
                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 7, _s, input)
            self_.error(nvae)
            raise nvae
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(xmlLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
