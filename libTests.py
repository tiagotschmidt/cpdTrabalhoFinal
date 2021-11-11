import trabFinalLib as tLib
import matplotlib.pyplot as plt

def hashingsTests():
    f = open("rating.csv","r")#-----------Mecanismo de Leitura dos Ratings----------------------------------------------
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

                                  #-----------Mecanismo de Leitura dos Ratings---------------------------------------------- 
        
    m = 40000#TestesProvisórios    
    
    allTIndex = []
    allN = []
    allH = []
    allM = [[]for _ in range(3000)]  

    for i in range(3000):
        allM[i] = 17000 + (i)  
    
    for m in allM:
        HashTable503 = [[]for _ in range(m)]
        #print(m)
        
        index = 0
        totalEntrys = 0
        for rating in ratingsMatrix:
            if(rating):
                tLib.insertHash(HashTable503,m,index,rating[0],rating[1])
                totalEntrys = totalEntrys + 1
            index = index + 1
            
        #print(tLib.searchHash(258970,HashTable503,m))
        
        totalItems = 0
        totalCycles = 0
        valuesOverused = 0
        for item in HashTable503:
            if(item):                
                totalItems = totalItems + 1
                totalSons = 0
                for son in item:
                    totalSons = totalSons+1
                if(totalSons > 1):
                    valuesOverused = valuesOverused + 1
            totalCycles = totalCycles + 1        
       
        tIndex = float(totalItems/totalCycles)*(1-float(valuesOverused/totalItems))
        allTIndex.append(tIndex)  
        #print(totalCycles)
        #print(totalItems)
        #print(valuesOverused)      
        #print("->"+str(m))
        #print(tIndex)      
        #print("Hits/TotalCélulasUsadas: "+str(float(valuesOverused/totalItems)*100)+"%")
        #print("TotalCélulasUsadas/TotalCélulas: "+str(float(totalItems/totalCycles)*100)+"%")
        allN.append(float(totalItems/totalCycles))
        allH.append(1-float(valuesOverused/totalItems))
        
    #print("Total de entradas")    
    #print(totalEntrys)    

    #print("Elenco de M")
    #print(allM)  
    #print("Elenco de N")
    #print(allN)  
    #print("Elenco de H")
    #print(allH)    
    #print("Elenco de T")
    #print(allTIndex)
    maxItem = max(allTIndex)
    print("Número T máximo: ", maxItem)
    index = allTIndex.index(maxItem)
    print("Configuração M:", allM[index])
    plt.plot(allM,allN)
    plt.plot(allM,allH)
    plt.plot(allM,allTIndex)
    plt.scatter(allM[index],maxItem)
    plt.xlabel('Número M')
    plt.ylabel('Índice N')
    plt.show()

def nameHashTest():
    tr = tLib.trie()#Sistema de teste da árvore trie  
    f = open("players.csv","r")
    lines = f.readlines()
    nameTable = [[]for _ in range(300000)]

    for line in lines[1:]:        
        tr.insert(line,nameTable)

    allTIndex = []
    allN = []
    allH = []
    allM = [[]for _ in range(10000)]

    for i in range(10000):
        allM[i] = 15000 + (i) 

    for m in allM:
        HashTableName = [[]for _ in range(m)]
        #print(m)
        
        index = 0
        totalEntrys = 0
        for player in nameTable:
            if(player):
                tLib.insertHashName(HashTableName,m,index,player[0][1])   
                totalEntrys = totalEntrys + 1
            index = index + 1
            
        #print(tLib.searchHash(258970,HashTable503,m))
        
        totalItems = 0
        totalCycles = 0
        valuesOverused = 0
        for item in HashTableName:
            if(item):                
                totalItems = totalItems + 1
                totalSons = 0
                for son in item:
                    totalSons = totalSons+1
                if(totalSons > 1):
                    valuesOverused = valuesOverused + 1
            totalCycles = totalCycles + 1        
       
        tIndex = float(totalItems/totalCycles)*(1-float(valuesOverused/totalItems))
        allTIndex.append(tIndex)  
        #print(totalCycles)
        #print(totalItems)
        #print(valuesOverused)      
        #print("->"+str(m))
        #print(tIndex)      
        #print("Hits/TotalCélulasUsadas: "+str(float(valuesOverused/totalItems)*100)+"%")
        #print("TotalCélulasUsadas/TotalCélulas: "+str(float(totalItems/totalCycles)*100)+"%")
        allN.append(float(totalItems/totalCycles))
        allH.append(1-float(valuesOverused/totalItems)) 

    maxItem = max(allTIndex)
    print("Número T máximo: ", maxItem)
    index = allTIndex.index(maxItem)
    print("Configuração M:", allM[index])
    plt.plot(allM,allN)
    plt.plot(allM,allH)
    plt.plot(allM,allTIndex)
    plt.scatter(allM[index],maxItem)
    plt.xlabel('Número M')
    plt.ylabel('Índice N')
    plt.show()


def userHashTest():
    t = open("rating.csv","r")#Mecanismo de Leitura dos ratings. Inserção na Hash.
    lines = t.readlines()
    
    userMatrix = [[]for _ in range(140000)]#Tabela para meta-processamento das ratings.
    
    for line in lines[1:]:
        chunks = line.split(',')           
        value = chunks[2]
        value = value[:-1] 
        userMatrix[int(chunks[0])].append([chunks[1],value])            
    

    allTIndex = []
    allN = []
    allH = []
    allM = [[]for _ in range(50)]

    for i in range(50):
        allM[i] = 1000 + (i*1000) 

    for m in allM:
        HashTableUser = [[]for _ in range(m)]
        #print(m)
        
        index = 0
        totalEntrys = 0
        for user in userMatrix:
            if(user):
                tLib.insertHashUser(HashTableUser,m,index,user)
            index = index + 1           
        
        totalItems = 0
        totalCycles = 0
        valuesOverused = 0
        for item in HashTableUser:
            if(item):                
                totalItems = totalItems + 1
                totalSons = 0
                for son in item:
                    totalSons = totalSons+1
                if(totalSons > 1):
                    valuesOverused = valuesOverused + 1
            totalCycles = totalCycles + 1        
       
        tIndex = float(totalItems/totalCycles)*(1-float(valuesOverused/totalItems))
        allTIndex.append(tIndex)  
        #print(totalCycles)
        #print(totalItems)
        #print(valuesOverused)      
        #print("->"+str(m))
        #print(tIndex)      
        #print("Hits/TotalCélulasUsadas: "+str(float(valuesOverused/totalItems)*100)+"%")
        #print("TotalCélulasUsadas/TotalCélulas: "+str(float(totalItems/totalCycles)*100)+"%")
        allN.append(float(totalItems/totalCycles))
        allH.append(1-float(valuesOverused/totalItems)) 

    maxItem = max(allTIndex)
    print("Número T máximo: ", maxItem)
    index = allTIndex.index(maxItem)
    print("Configuração M:", allM[index])
    plt.plot(allM,allN)
    plt.plot(allM,allH)
    plt.plot(allM,allTIndex)
    plt.scatter(allM[index],maxItem)
    plt.xlabel('Número M')
    plt.ylabel('Índice N')
    plt.show()

def trieTest():
    tr = tLib.trie()#Sistema de teste da árvore trie  
    f = open("players.csv","r")
    lines = f.readlines()

    for line in lines:        
        chunks = line.split(',')
        tr.insert(chunks[1],chunks[0])
    
    result = tr.search("Tiago")
    
    for answer in result:
        print(answer)    

def main():
    userHashTest()
    
    
if __name__ == "__main__":
    main()

    

    
