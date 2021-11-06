import trabFinalLib as tLib


def main():
    tr = tLib.trie()   
    f = open("players.csv","r")
    lines = f.readlines()

    for line in lines:        
        chunks = line.split(',')
        tr.insert(chunks[1])
        
    
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
            
    HashTable = [[]for _ in range(6000)]    
    
    for rating in ratingsMatrix:
        if(rating):
            tLib.insertHash(HashTable,m,index,rating[0],rating[1])            
        
if __name__ == "__main__":
    main()
   
    