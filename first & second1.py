def first_second(myList):
    unique_list=list(set(myList))
    sorted_list=sorted(unique_list)
    
    first_score=sorted_list[-1]
    second_score=sorted_list[-2]
    
    combined_score=(first_score,second_score)
    return combined_score
    
myList=[84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(first_second(myList))