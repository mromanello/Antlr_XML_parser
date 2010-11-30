import codecs,logging,sys
import antlr3
from xmlLexer import xmlLexer
from xmlParser import xmlParser
from xmlTreeParser import xmlTreeParser
from BeautifulSoup import BeautifulStoneSoup

def init_logger():
    logger = logging.getLogger("Main")
    logger.setLevel(logging.DEBUG)
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)
    logger.info("Logger Initialised.")

def run(i_file):
    temp = open(i_file,'r').read()
    char_stream = antlr3.ANTLRStringStream(temp)
    lexer = xmlLexer(char_stream)
    tokens = antlr3.CommonTokenStream(lexer)
    parser = xmlParser(tokens)
    r = parser.document()
    """
    for t in parser.toks:
        res = BeautifulStoneSoup(t.getText(),convertEntities=BeautifulStoneSoup.ALL_ENTITIES)
        print res
    """

    root = r.tree
    #print root.toStringTree()

    nodes = antlr3.tree.CommonTreeNodeStream(root)
    nodes.setTokenStream(tokens)
    tp = xmlTreeParser(nodes)
    tp.document()

if __name__ == "__main__":
    init_logger()
    fname = sys.argv[1]
    run(fname)
