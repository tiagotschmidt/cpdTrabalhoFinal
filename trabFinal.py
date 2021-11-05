import trabFinalLib as tLib
import matplotlib.pyplot as plt

def main():
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

                                 #-----------Mecanismo de Leitura dos Ratings---------------------------------------------- 
        
    m = 40000                    #TestesProvisórios
    
    allM = [20011,21193,22123,23473,24109,25439,26399,27691,28621,29741]
    allTIndex = []
    
    #for i in range(3*10):
        #allM[i] = 10000 + (i*5000)
    
    for m in allM:
        HashTable503 = [[]for _ in range(m)]
        
        index = 0
        for rating in ratingsMatrix:
            if(rating):
                tLib.insertHash(HashTable503,m,index,rating[0],rating[1])
                
            index = index + 1
            
        #print(tLib.searchHash(258970,HashTable503,m))
        
        totalItems = 0
        totalCycles = 0
        valuesOverused = 0
        for item in HashTable503:
            if(item):
                #print(item)
                totalItems = totalItems + 1
                totalSons = 0
                for son in item:
                    totalSons = totalSons+1
                if(totalSons > 1):
                    valuesOverused = valuesOverused + 1
            totalCycles = totalCycles + 1
        
        #tIndex = float(totalItems/totalCycles) * (1-float(valuesOverused/totalItems))
        tIndex = float(10000*totalItems*totalItems*totalItems/(totalCycles*totalCycles*totalCycles*valuesOverused*valuesOverused))
        allTIndex.append(tIndex)
        #print("->"+str(m))
        #print(tIndex)
        #print(totalItems)
        #print(valuesOverused)
        #print(str(float(valuesOverused/totalItems)*100)+"%")
        #print(str(float(totalItems/totalCycles)*100)+"%")
        
    print(allM)    
    print(allTIndex)
    plt.plot(allM,allTIndex)
    plt.xlabel('Número M')
    plt.ylabel('Índice T')
    plt.show()
if __name__ == "__main__":
    main()
   
    