#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)This is logarithmic => O(log n) As input becomes bigger, it will slightly take more time to add numbers for 'a' before while loop stops


b) This is linearithmic -> O(n log n) as input becomes bigger, first inner loop will take same amount of time every pass but 2nd inner loop of while will increase in runtime, first loop is linear and second loop depends on n thus becoming logarithmic


c)Linear -> O(n). each recursion will take same amount of time as previous as input gets bigger, total running time is sum of each of recursive call, each call is has fixed running time of adding number and performing recursion.

## Exercise II
Algorithm = Two Variables - Number of eggs Dropped (Attempted at throwing off building without breaking) - Broken Eggs

Issues with the challenge -> N story building probably has difference between each floor, this difference combined with floors determines the where eggs will break for sure. The height is unknown, if it is constant, floor where eggs break will be same for no matter the input or if height changes thus changing which floor will cause the egg to break

Start with Finite amount of eggs and Finite size building with n - stories

Go through each floor and throw an egg

Check for the following:

if egg is broken - mark the floor as where eggs start breaking, and break out of the loop as we know going pass this floor will result eggs always breaking

else increase count of dropped eggs.

End the loop and see which floor eggs broke and how many eggs were dropped so far

Based on the information, this alogrithm have best of case O(1) where it will be same floor no matter N story building otherwise it will linear O(n) as floor needs to be calulated based on height difference of floor based on input and then find the floor

