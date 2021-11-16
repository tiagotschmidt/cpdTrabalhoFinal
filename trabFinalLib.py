class trieNode: #Objeto Nó da Árvore Trie. Contém o chararactere(s), se é fim de palavra e seus filhos.
    def __init__(self,char):
        self.char = char
        self.isEnd = False
        self.soFifaId = None
        self.positions = []
        self.children = {}
        
class trie(object):#Objeto da Árvore Trie, em si. 
    def __init__(self):
        self.root = trieNode("")
        
    def insert(self,line,nameHashTable,mNames):
        node = self.root
        chunks = line.split(',')
        word = chunks[1]
        soFifaId = int(chunks[0])       
        insertHashName(nameHashTable,mNames,soFifaId,word)
        
        for char in word:
            if  char in node.children:
                node = node.children[char]
            else:
                newNode = trieNode(char)
                node.children[char] = newNode
                node = newNode

        for chunk in chunks[2:]:
            if(chunk[-1] == "\n"):
                chunk = chunk[:-1]  
            node.positions.append(chunk)
        
        node.isEnd = True 
        node.soFifaId = soFifaId   
        
    def depthFirstSearch(self, node, prefixWord):
        if node.isEnd:
            self.output.append([(prefixWord + node.char),node.soFifaId,node.positions])
            
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
        
def hashing(soFifaId,m):
    return (soFifaId % m)

def insertHashUser(Hashtable,m, uid, rating):
    value = hashing(uid,m)
    Hashtable[value].append(rating)

def insertHashName(Hashtable,m,soFifaId, name):
    value = hashing(soFifaId,m)
    Hashtable[value].append([soFifaId,name])

def insertHash(Hashtable,m,soFifaId,averageRating, totalRating):
    value = hashing(soFifaId,m)
    Hashtable[value].append([soFifaId,averageRating,totalRating])
    
def searchHash(index,Hashtable,m):
    returnValue = -1
    searchKey = hashing(index,m)
    for j in range(len(Hashtable[searchKey])):
        if(index == Hashtable[searchKey][j][0]):
            return [Hashtable[searchKey][j]]

def searchHashUser(index,Hashtable,m):
    returnList = []
    searchKey = hashing(index,m)    
    for j in range(len(Hashtable[searchKey])):         
        chunks = Hashtable[searchKey][j].split(',') 
        if(int(chunks[0]) == index):           
            returnList.append([chunks[1],float(chunks[2])]) 
    return returnList
        

def partition(RatingsArray, start, end):
    pivot = RatingsArray[start][1]
    low = start + 1
    high = end

    while True:
        while(low <= high and RatingsArray[high][1] >= pivot):
            high = high - 1
        while(low <= high and RatingsArray[low][1] <= pivot):
            low = low + 1

        if low <= high:
            RatingsArray[low][1], RatingsArray[high][1] = RatingsArray[high][1], RatingsArray[low][1]
        else:
            break


    RatingsArray[start][1], RatingsArray[high][1] = RatingsArray[high][1], RatingsArray[start][1]
    return high

def quickSort(RatingsArray, start, end):
    if start >= end:
        return 

    p = partition(RatingsArray, start, end)
    quickSort(RatingsArray, start, p-1)
    quickSort(RatingsArray, p+1, end)