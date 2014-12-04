20044303
20035769
*****


 betterEvaluationFunction - the function takes into account these attributes:
        * score of the state
        * number of food left
        * the sum of distances from pacman to all the food left
        * number of capsules left
        * a ghost score- calculated in a seperate function

 The returned value is a linear combination of these values. We started by adding together all
 values we thought should affect the state's calculated score and then started tweaking with
 the weights. After a short while we managed to get to winning about half the times, but our scores
 averaged around 950, and weren't high enough. In a fit of despair we decided to bost the weight of
 the remaining capsules which was close to 0 up until then. We got decent result at 5, better at 10
 and we stopped looking at 200 since we had 89/100 win rate and around 1270 average score when including
 the failures!