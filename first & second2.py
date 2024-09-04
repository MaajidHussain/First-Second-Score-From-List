
def first_second(my_list):
    first_score=float('-inf')
    second_score=float('-inf')
    
    for score in my_list:
        if score>first_score:
            second_score=first_score
            first_score=score
        elif score>second_score and score!=first_score:
            second_score=score
    
    return first_score,second_score
        
    
score_list=[84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(first_second(score_list))
