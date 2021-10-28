import pandas as pd

class trieNode:
    def __init__(self,char):
        self.char = char
        self.isEnd = False
        self.children = {}
        
class trie(object):
    def __init__(self):
        self.root = trieNode("")
        
    def insert(self,word):
        node = self.root
        
        for char in word:
            if  char in node.children:
                node = node.children[char]
            else:
                newNode = trieNode(char)
                node.children[char] = newNode
                node = newNode
        
        node.isEnd = True    
        
    def depthFirstSearch(self, node, prefixWord):
        if node.isEnd:
            self.output.append((prefixWord + node.char))
            
        for child in node.children.values():
            self.depthFirstSearch(child,prefixWord + node.char)
            
    def search(self,word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return[]
                
        self.output = []
        self.depthFirstSearch(node,word[:-1])
        
        return self.output

#players_df = pd.read_csv("players.csv")
#print(players_df)

#rating_df = pd.read_csv("minirating.csv")
#print(rating_df)

#tags_df = pd.read_csv("tags.csv")
#print(tags_df)

tr = trie()
tr.insert("here")
tr.insert("hear")
tr.insert("he")
tr.insert("hello")
tr.insert("how ")
tr.insert("her")

print(tr.search("he"))
print(tr.search("her"))