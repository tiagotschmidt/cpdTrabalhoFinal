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

    index = 0#Sistema de feedback.
    for rating in ratingsMatrix:    
        if(rating):
            print(rating)  
            print(index) 
        index = index + 1       #-----------Mecanismo de Leitura dos Ratings---------------------------------------------- 
        
if __name__ == "__main__":
    main()
   
    