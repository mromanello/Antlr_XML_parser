import codecs,logging,sys,pickle,pprint
import antlr3
import json
from xmlLexer import xmlLexer
from xmlParser import xmlParser
from xmlTreeParser import xmlTreeParser
from BeautifulSoup import BeautifulStoneSoup

def init_logger():
    global logger
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

def run(i_file,o_file):
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
    """
    out = open(o_file,'wb')
    pickle.dump(tp.instances,out)
    out.close()
    logger.info("Pickled data written to file %s"%o_file)
    """
    fout = open(o_file,'w')
    fout.write(json.dumps(tp.instances).decode("UTF-8"))
    fout.close()
    #print(json.dumps(tp.instances))
    pprint.pprint(tp.instances)
    temp = open(i_file,'r')
    for inst in tp.instances:
		for tok in tp.instances[inst]:
			temp.seek(tok["start"])
			print "\"%s\" == \"%s\""%(tok["utext"], temp.read(tok["end"]-tok["start"]+1))
    

if __name__ == "__main__":
    init_logger()
    fname = sys.argv[1]
    oname = sys.argv[2]
    run(fname,oname)
