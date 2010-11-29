import codecs,logging
import antlr3
from xmlLexer import xmlLexer
from xmlParser import xmlParser
from xmlTreeParser import xmlTreeParser

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

from BeautifulSoup import BeautifulStoneSoup

out_file='/56k/phd/code/aph_sample.txt'
#out_file='/56k/phd/code/aph_vol75_all.sgm.orig'
"""
orig_file='/56k/phd/code/aph_vol75_all.sgm.orig'
temp = open(orig_file,'r').read()
f = codecs.open(out_file, encoding='utf-8', mode='w')
f.write(BeautifulStoneSoup(temp,convertEntities=BeautifulStoneSoup.ALL_ENTITIES).prettify().decode('utf-8'))
f.close()
"""
input = codecs.open(out_file, encoding='utf-8').read()
char_stream = antlr3.ANTLRStringStream(input)

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
