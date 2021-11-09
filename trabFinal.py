import trabFinalLib as tLib
import time

def searchPlayer(name,hashTable,m,tr):#Função searchPlayer. Executa a busca do nome na trie. Assim que obtém uma lista de resultas, consulta cada nome completo e seu id para resgatar demais informações.
    result = tr.search(name)
    
    for answer in result:
        hashResult = tLib.searchHash(int(answer[1]),hashTable,m)        
        if(hashResult):            
            print("ID:",answer[1],"|Nome:",answer[0],"|Posições:",answer[2],"|Rating:"+str(hashResult[0][1])+"|Contagem:"+str(hashResult[0][2]))  
        else:
            print("ID:",answer[1],"|Nome:",answer[0],"|Posições:",answer[2]) 

def main():#Função main. Executada ao iniciar.
    start_time = time.time()#Mecanimo de cálculo para tempo.

    tr = tLib.trie()#Mecanismo de Leitura e Inserção na Trie   
    f = open("players.csv","r")
    lines = f.readlines()

    for line in lines[1:]:       
        tr.insert(line)
    
    t = open("rating.csv","r")#Mecanismo de Leitura dos ratings. Inserção na Hash.
    lines = t.readlines()

    ratingsMatrix = [[]for _ in range(300000)]#Tabela para meta-processamento das ratings.

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
            
    m = 18880
    HashTable = [[]for _ in range(m)]#Tabela Hash utilizada.    
    index = 0
    for rating in ratingsMatrix:
        if(rating):
            tLib.insertHash(HashTable,m,index,rating[0],rating[1])   
        index = index + 1
    
    f.close()
    t.close()#Término das leituras.
    end_time = time.time()   

    searchPlayer("Fer",HashTable,m,tr)#Caso teste     
    total_time = end_time - start_time
    print("Tempo(s): ", total_time)

if __name__ == "__main__":
    main()
   
    