import pandas as pd
    
def getValue(string):#Função getValue. Recebe um string com finalidade de gerar um valor.
    values = [ord(character) for character in string]#Cria um vetor com os valores de cada caractere da palavra.
    totalValue = 0
    for value in values:#Soma todos os valores dos caracteres da string.
        totalValue = totalValue + value
    return totalValue#Retorna o valor.

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

#players_df = pd.read_csv("players.csv")
#print(players_df)

#rating_df = pd.read_csv("minirating.csv")
#print(rating_df)

#tags_df = pd.read_csv("tags.csv")
#print(tags_df)

tr = trie()

#tr.insert("here")
#tr.insert("hear")
#tr.insert("he")
#tr.insert("hello")
#tr.insert("how ")
#tr.insert("her")

#print(tr.search("he"))
#print(tr.search("her"))

#f = open("players.csv","r")
#lines = f.readlines()

#totalPlayers = 0

#for line in lines:
    #totalPlayers =+ 1
    #chunks = line.split(',')
    #tr.insert(chunks[1])
    
#print(tr.search("João"))

f = open("minirating.csv","r")
lines = f.readlines()

ratingsMatrix = [[]for _ in range(300000)] 

for line in lines[1:]:
    chunks = line.split(',')    
    value = chunks[2]
    value = value[:-1]      
    ratingsMatrix[int(chunks[1])].append(value)     

for rating in ratingsMatrix:
    if(rating):
        print(rating)
        totalSum = 0
        totalTimes = 0
        for son in rating:            
            print(son)
            totalSum = totalSum + float(son)
            totalTimes = totalTimes + 1      
        rating.clear()
        totalSum = totalSum / totalTimes;
        rating.append(totalSum)
        rating.append(totalTimes)        

index = 0
for rating in ratingsMatrix:    
    if(rating):
        print(rating)  
        print(index) 
    index = index + 1    
    