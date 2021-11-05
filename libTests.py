import trabFinalLib as tLib

def main():
    tr = tLib.trie()   
    f = open("players.csv","r")
    lines = f.readlines()

    for line in lines:        
        chunks = line.split(',')
        tr.insert(chunks[1])
    
    #result = tr.search("João")
    
    #for answer in result:
        #print(answer)         
    
if __name__ == "__main__":
    main()