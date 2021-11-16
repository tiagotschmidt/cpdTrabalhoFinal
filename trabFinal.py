import trabFinalLib as tLib
import time
import random

def searchUser(uid,hashTableUser,mUsers,hashTableName,mNames,hashTableRatings,mRatings):#Função searchPlayer. Executa a busca do nome na trie. Assim que obtém uma lista de resultas, consulta cada nome completo e seu id para resgatar demais informações.
    result = tLib.searchHashUser(uid,hashTableUser,mUsers)    
    tLib.quickSort(result,0,len(result) - 1)   
    isDone = 0
    
    for rating in reversed(result):  
        if(isDone > 20):
            break         
        soFifaId = int(rating[0])
        name = tLib.searchHash(soFifaId,hashTableName,mNames)[0][1]
        globalRatings = tLib.searchHash(soFifaId,hashTableRatings,mRatings)   
        print("SOFIFA_ID:",rating[0],". Name:",name,". Global Rating:"+str(globalRatings[0][1])+". Count:"+str(globalRatings[0][2]),". Rating:",rating[1])   
        isDone = isDone + 1

def searchPosition(maxSearch,pos,trPos,hashTableRatings,mRatings,hashTableName,mNames,trNames):#Função searchPlayer. Executa a busca do nome na trie. Assim que obtém uma lista de resultas, consulta cada nome completo e seu id para resgatar demais informações.
    result = trPos.search(pos)

    playersList = result[0][1]
    answerList = []
    for player in playersList:
        ratingInfo = tLib.searchHash(player,hashTableRatings,mRatings)            
        if(ratingInfo and int(ratingInfo[0][2]) > 1000):
            answerList.append([player,float(ratingInfo[0][1]),int(ratingInfo[0][2])])          

    tLib.quickSort(answerList,0,len(answerList) - 1) 

    isDone = 0

    for answer in reversed(answerList):
        if(isDone > maxSearch):
            break
        name = tLib.searchHash(answer[0],hashTableName,mNames)[0][1]
        trieNameR = trNames.search(name)        
        print("SOFIFA_ID:",answer[0],". Name:",name,". Player_positions:",trieNameR[0][2],". Rating:"+str(answer[1])+". Count:"+str(answer[2])) 
        isDone = isDone + 1

def searchPlayer(name,hashTable,m,tr):#Função searchPlayer. Executa a busca do nome na trie. Assim que obtém uma lista de resultas, consulta cada nome completo e seu id para resgatar demais informações.
    result = tr.search(name)
    
    for answer in result:
        hashResult = tLib.searchHash(int(answer[1]),hashTable,m)        
        if(hashResult):            
            print("SOFIFA_ID:",answer[1],". Name:",answer[0],". Player_positions:",answer[2],". Rating:"+str(hashResult[0][1])+". Count:"+str(hashResult[0][2]))  
        else:
            print("SOFIFA_ID:",answer[1],". Name:",answer[0],". Player_positions:",answer[2]) 

def main():#Função main. Executada ao iniciar.
    start_time = time.time()#Mecanimo de cálculo para tempo.

    mNames = 18880
    nameHashTable = [[]for _ in range(mNames)]#Tabela Hash para identicação do nome, através do id.

    trNames = tLib.trieNames()#Mecanismo de Leitura e Inserção na Trie e na Hash do nome.   
    trPos = tLib.triePositions()#Mecanismo de Leitura e Inserção na Trie e na Hash do nome.   
    f = open("players.csv","r")
    lines = f.readlines()

    #Leitura do arquivo de jogadores.
    for line in lines[1:]:      
        trNames.insert(line,nameHashTable,mNames) 
        trPos.insert(line) 

    t = open("rating.csv","r")#Mecanismo de Leitura dos ratings. Inserção na Hash.
    lines = t.readlines()

    ratingsMatrix = [[]for _ in range(300000)]#Tabela para meta-processamento das ratings.    
    mUsers = 9725
    HashTableUser = [[]for _ in range(mUsers)]#Tabela Hash utilizada para indexação dos usuários avaliadores.  
    
    #Leitura do arquivo de ratings. 
    for line in lines[1:]:
        chunks = line.split(',')           
        value = chunks[2]
        value = value[:-1] 
        ratingsMatrix[int(chunks[1])].append(value) 
        tLib.insertHashUser(HashTableUser,mUsers,int(chunks[0]),chunks[0]+","+chunks[1]+","+value)  
        
    #Etapa de pre-processamento dos ratings. Reune e salva as médias para cada jogador.
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
        
       
    #Tabela Hash Para os Ratings Globais de cada jogador.     
    mRatings = 18880
    HashTableRatings = [[]for _ in range(mRatings)]
    index = 0
    for rating in ratingsMatrix:
        if(rating):
            tLib.insertHash(HashTableRatings,mRatings,index,rating[0],rating[1])   
        index = index + 1        
    
    f.close()
    t.close()    
   
    end_time = time.time()
    total_time = end_time - start_time     
    #searchPosition(10,"ST",trPos,HashTableRatings,mRatings,nameHashTable,mNames,trNames)
    #searchPlayer("Lionel Andrés",HashTableRatings,mRatings,trNames)
    searchUser(4,HashTableUser,mUsers,nameHashTable,mNames,HashTableRatings,mRatings)
    print("Tempo(s): ", total_time)

if __name__ == "__main__":
    main()
   
    