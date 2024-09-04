# First-Second-Score-From-List
Best Score:- Given a list, write a function to get first, second best scores from the list. 
List may contain duplicates.
--> 2 Approaches;

Approach 1: Using in-built functions like list(),set(),sorted()
            This is not so effiecient but good for conceptual understanding.
            TIme Complexity: O(n logn)
            Space Complexity: O(n)

Approach 2: Using logical building, Loopings, conditional statements.
            This is efficient code.
            Time Complexity: O(n)
            Space Complexity: O(1)
Note:- float('-inf'): 
                     If you are trying to find the maximum and second maximum values in a list that may include both positive and negative numbers, initializing                           to negative infinity ensures that any number from the list will be larger.
                     This is critical for correctly identifying the largest and second-largest values, even if they are negative.
