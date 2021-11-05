class trieNode: #Objeto Nó da Árvore Trie. Contém o chararactere(s), se é fim de palavra e seus filhos.
    def __init__(self,char):
        self.char = char
        self.isEnd = False
        self.children = {}
        
class trie(object):#Objeto da Árvore Trie, em si. 
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