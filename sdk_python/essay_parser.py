from essay_structures import *

f = open('essay.txt','r')
#essay_tree = essay( f.read() )
essay_tree = essay( "" )
for paragraph in f:
    essay_tree.add_child(1,paragraph)
    
f.close()
print essay_tree

