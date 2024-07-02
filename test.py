def toHorn(clause:str)-> list[str]:
        clausePartitionedList = clause.split(" V ")
        resultList = []
        for i in range(0,len(clausePartitionedList)):
            tmp= clausePartitionedList[i]
            for j in range(0,len(clausePartitionedList)):
                if(i==j):
                    continue
                tmp = tmp+' /\\ '+'-'+clausePartitionedList[j]
            resultList.append(tmp)
        return resultList
    
test = "P12 V P22 V P33"

print(toHorn(test)[0])