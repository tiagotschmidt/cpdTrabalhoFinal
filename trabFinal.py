import trabFinalLib as tLib

def searchPlayer(name,hashTable,m,tr):
    result = tr.search(name)
    
    for answer in result:
        hashResult = tLib.searchHash(int(answer[1]),hashTable,m)        
        if(hashResult):            
            print("Nome:",answer[0]+". Rating médio:"+str(hashResult[0][1])+". Total de avaliações:"+str(hashResult[0][2]))  
        else:
            print("Nome:",answer[0]) 

def main():
    tr = tLib.trie()   
    f = open("players.csv","r")
    lines = f.readlines()

    for line in lines:        
        chunks = line.split(',')
        tr.insert(chunks[1],chunks[0])       
    
    f = open("minirating.csv","r")#-----------Mecanismo de Leitura dos Ratings----------------------------------------------
    lines = f.readlines()

    ratingsMatrix = [[]for _ in range(300000)] 

    for line in lines[1:]:
        chunks = line.split(',')    
        value = chunks[2]
        value = value[:-1]      
        ratingsMatrix[int(chunks[1])].append(value)     

    for rating in ratingsMatrix:
        if(rating):            
            totalSum = 0
            totalTimes = 0
            for son in rating:          
                totalSum = totalSum + float(son)
                totalTimes = totalTimes + 1      
            rating.clear()
            totalSum = totalSum / totalTimes;
            rating.append(totalSum)
            rating.append(totalTimes)
            
    m = 6000
    HashTable = [[]for _ in range(m)]    
    index = 0
    for rating in ratingsMatrix:
        if(rating):
            tLib.insertHash(HashTable,m,index,rating[0],rating[1])   
        index = index + 1   
        
    searchPlayer("João",HashTable,m,tr)      
        
if __name__ == "__main__":
    main()
   
    