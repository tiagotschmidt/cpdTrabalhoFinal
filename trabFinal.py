import trabFinalLib as tLib
import time

def searchUser(uid,hashTableUser,mUsers,hashTableName,mNames,hashTableRatings,mRatings):#Função searchUser. Executa a busca das avaliações por ID de usuário.
    result = tLib.searchHashUser(uid,hashTableUser,mUsers)#Busca as avaliações por ID do usuário.    
    tLib.quickSort(result,0,len(result) - 1)#Organiza as avaliações por rating.   
    isDone = 0 #Mecanismo de parada máxima: 20 avaliações.
    
    for rating in reversed(result):#Printa em ordem reversa, ou seja, os maiores 20 avaliações.
        if(isDone > 20):
            break         
        soFifaId = int(rating[0])#Extrai o sofifaId.
        name = tLib.searchHash(soFifaId,hashTableName,mNames)[0][1]#Resgata o nome através do sofifaId
        globalRatings = tLib.searchHash(soFifaId,hashTableRatings,mRatings)#Resgata os ratings globais por sofifaId.   
        print("SOFIFA_ID:",rating[0],". Name:",name,". Global Rating:"+str(globalRatings[0][1])+". Count:"+str(globalRatings[0][2]),". Rating:",rating[1])   
        isDone = isDone + 1

def searchPosition(maxSearch,pos,trPos,hashTableRatings,mRatings,hashTableName,mNames,trNames):#Função searchPosition. Executa a busca das posições por posições desejadas. 
    result = trPos.search(pos)#Busca na trie das Posições a posição desejada.

    playersList = result[0][1]#Filtra a lista de jogadores da Posição
    answerList = []
    for player in playersList:#Para cada jogador na lista de jogadores da Posição
        ratingInfo = tLib.searchHash(player,hashTableRatings,mRatings)#Busca a avaliação do jogador.            
        if(ratingInfo and int(ratingInfo[0][2]) > 1000):#Critérios definidos no enunciado, executa filtragem
            answerList.append([player,float(ratingInfo[0][1]),int(ratingInfo[0][2])])#Criando a lista filtrada de jogadores da posição.

    tLib.quickSort(answerList,0,len(answerList) - 1)#Ordenamento dos jogadores filtrados por rating.

    isDone = 1

    for answer in reversed(answerList):#Printa em ordem reversa, ou seja, as maiores avaliações.
        if(isDone > maxSearch):#Mecanismo de parada, escolhido pelo usuário.
            break
        name = tLib.searchHash(answer[0],hashTableName,mNames)[0][1]#Resgata o nome através do sofifaId(answer[0])
        trieNameR = trNames.search(name)#Busca o elemento do jogador na Trie de nomes.
        print("SOFIFA_ID:",answer[0],". Name:",name,". Player_positions:",trieNameR[0][2],". Rating:"+str(answer[1])+". Count:"+str(answer[2])) 
        isDone = isDone + 1

def searchTags(tagList,tr,hashTableName,mNames,trNames,hashTableRatings,mRatings):#Função searchTags. Executa a busca das tags.
    if(len(tagList) > 1):#Caso a lista de tags tenha mais de um elemento, executa:
        result = tr.search(tagList[0])[0][1]#Busca a lista de jogadores da primeira tag.
        for tag in tagList:#Iterativamente, busca a intersecção de jogadores da lista atual, com a lista dos jogadores da tag atual.
            newTagResult = tr.search(tag)[0][1]    
            result = list(set(result).intersection(set(newTagResult)))
    else:#Se não, apenas busca na trie de tags
        result = tr.search(tagList[0])   

    for answer in result:
        hashResult = tLib.searchHash(int(answer),hashTableRatings,mRatings)#Busca os ratings do jogador.s
        name = tLib.searchHash(int(answer),hashTableName,mNames)[0][1]#Busca o nome do jogador.
        trieNameR = trNames.search(name)#Busca o elemento na trie do Jogador.
        if(hashResult):            
            print("SOFIFA_ID:",answer,". Name:",name,". Player_positions:",trieNameR[0][2],". Rating:"+str(hashResult[0][1])+". Count:"+str(hashResult[0][2]))  
        else:
            print("SOFIFA_ID:",answer,". Name:",name,". Player_positions:",trieNameR[0][2]) 

def searchPlayer(name,hashTable,m,tr):#Função searchPlayer. Executa a busca do nome na trie
    result = tr.search(name)#Busca o nome na trie.
    
    for answer in result:
        hashResult = tLib.searchHash(int(answer[1]),hashTable,m)#Busca o rating global do soFifaId armazenado na trie.    
        if(hashResult):            
            print("SOFIFA_ID:",answer[1],". Name:",answer[0],". Player_positions:",answer[2],". Rating:"+str(hashResult[0][1])+". Count:"+str(hashResult[0][2]))  
        else:
            print("SOFIFA_ID:",answer[1],". Name:",answer[0],". Player_positions:",answer[2]) 

def main():#Função main. Executada ao iniciar.
    start_time = time.time()#Mecanimo de cálculo para tempo.

    mNames = 18880
    nameHashTable = [[]for _ in range(mNames)]#Tabela Hash para nomes. 

    trNames = tLib.trieNames()#Definindo a trie de Nomes.
    trPos = tLib.triePositions()#Definindo a trie de Posições.
    f = open("players.csv","r")
    lines = f.readlines()

    #Leitura do arquivo de jogadores.
    for line in lines[1:]:      
        trNames.insert(line,nameHashTable,mNames)#Grava a trie de Nomes, e a hash de nomes.
        trPos.insert(line)#Grava a trie de Posições

    trTags = tLib.trieTags()#Definindo a trie de tags. 
    w = open("tags.csv","r")
    lines = w.readlines()

    #Leitura do arquivo de tags.
    for line in lines[1:]:      
        trTags.insert(line)#Grava a trie de tags.        

    t = open("rating.csv","r")#Leitura do arquivo de ratings.
    lines = t.readlines()

    ratingsMatrix = [[]for _ in range(300000)]#Tabela para meta-processamento das ratings.    
    mUsers = 9725
    HashTableUser = [[]for _ in range(mUsers)]#Tabela Hash utilizada para indexação dos usuários avaliadores.  
    
    #Leitura do arquivo de ratings. 
    for line in lines[1:]:
        chunks = line.split(',')           
        value = chunks[2]
        value = value[:-1] 
        ratingsMatrix[int(chunks[1])].append(value)#Grava a tabela intermediária dos ratings.
        tLib.insertHashUser(HashTableUser,mUsers,int(chunks[0]),chunks[0]+","+chunks[1]+","+value)#Grava a hash do usuários.
        
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
    w.close()    
   
    end_time = time.time()
    total_time = end_time - start_time     
    print("Tempo(s): ", total_time)


    #searchTags(["Brazil","Dribbler"],trTags,nameHashTable,mNames,trNames,HashTableRatings,mRatings)
    #searchPosition(10,"ST",trPos,HashTableRatings,mRatings,nameHashTable,mNames,trNames)    
    #searchUser(4,HashTableUser,mUsers,nameHashTable,mNames,HashTableRatings,mRatings)
    #searchPlayer("Fer",HashTableRatings,mRatings,trNames)

    while(True):
        entryLine = input("$")
        copyEntry = entryLine
        chunks = entryLine.split(' ')

        if(chunks[0] == "player"):
            searchName = ""            
            for chunk in chunks[1:]:
                searchName = searchName + " " + chunk
            if(searchName[0] == " "):
                searchName = searchName[1:]
            searchPlayer(searchName,HashTableRatings,mRatings,trNames)         
        elif(chunks[0] == "user"):
            searchUser(int(chunks[1]),HashTableUser,mUsers,nameHashTable,mNames,HashTableRatings,mRatings)
        elif(chunks[0] == "tags"):
            copyChunks = entryLine.split('\'')
            copyChunks.remove(copyChunks[0])
            for chunk in copyChunks:
                if(chunk == "" or chunk == " "):
                    copyChunks.remove(chunk) 
                else:                   
                    chunk = chunk[:-1] 
                    chunk = chunk[1:]     
            searchTags(copyChunks,trTags,nameHashTable,mNames,trNames,HashTableRatings,mRatings)
        elif(chunks[0] == "exit"):
            exit()              
        else:
            firstWord = chunks[0]
            if(firstWord[0] == 't' and firstWord[1] == 'o' and firstWord[2] == 'p'):
                totalN = firstWord[3:]
                copyChunks = entryLine.split('\'')
                copyChunks.remove(copyChunks[0])               
                searchPosition(int(totalN),copyChunks[0],trPos,HashTableRatings,mRatings,nameHashTable,mNames,trNames)    
            else:
                print("Comando desconhecido.") 

    

if __name__ == "__main__":
    main()
   
    