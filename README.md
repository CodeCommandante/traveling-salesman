# Traveling Salesman Problem
***
## Purpose of Program
---
This program uses the simulated annealing algorithm to find an approximation of the optimal route.   It demonstrates uses the normal distance function and shows the initial tour, final tour, iteration count and details on restarts.

## Methodology
---
The simulated annealing process uses a "cooling" function of the form _T' = 0.99T_; however, for the trials in this problem, rather than increase the initial temperature, the "cooling" function was modified for each subsequent pair of trials _(See the table in the **Results** section for details.)_.

_R_ is again a randomly generated real number between 0 and 1 (inclusive).  However, notice here that the position of _Eval(x)_ and _Eval(x')_ are switched.  The evaluation for what is considered optimal in this problem differs from the hill-climbing problem in that we intend to find the _shortest_ overall path from the departure city to the arrival city, rather than a global _maximum_.  Although, the evalution is different, the general idea of searching a wider space in the beginning of the simulation and narrowing the criteria for what is acceptable as we go along remains fundamentally the same as in Problem 1.

The perturbation procedure for this problem is considerably more complex.  Instead of deviating one coordinate on the _x-y_ plane and evaluating the other coordinate at said location _(x' in Problem 1)_, here the perturbation consists of "shuffling" the order of a list of cities.  The initial list can be understood as the stops _in order_ that the traveling saleman will visit all 50 cities.  To shuffle that order, I used a simple pair-swap of two randomly chosen cities in the list; with the caveat that those pair swaps can occur _multiple_ times - thus, simulating a larger shuffle of more than only two cities.

To better demonstrate, the psuedo-code for the shuffling function is as follows:
```
i=0
Initialize Intensity
while i < Intensity:
	FirstCity = rand(1,49)
	SecondCity = rand(1,49)
	Swap FirstCity & SecondCity
	i++
```
Here, "Intensity" an integer that tells the function how many random pairs to swap.

Displayed below in the **Results** section is a table demonstrating 8 consecutive trials run on the algorithm.  I again paired up like trials.  Here, each pair of trials differ from the subsequent pair by the precision of the scalar _0.99_ in the Temperature function.  An increase in precision from _0.99_ to _0.999_ to _0.9999_, for example, affect both the number of iterations (and, therefore, time) the algorithm will need to complete and the _Intensity_ of the perturbation (shuffling of cities) as well.  See the **Code** section below for details on my implementation.

Along with the table are three plots:  the initial randomly generated tour, the final optimization of the tour, and a plot depicting the accepted optimizations (or sub-optimizations) over iterations.  This last plot is essentially the same evalution/data tool used in Problem 1, but is tailored for this problem where the optimization means _minimizing_ the tour distance.

I also tracked what I refer to in the table as the "Optimization Rate" (labeled _Opt Rate_ in the Table below).  This is the percent reduction in the overall path from the start to the end of the tour.  For comparison, I created a 50 city tour that was laid out in a rectangle with each city being equidistant from it's neighbors on either side.  I calculated the absolute optimized path of this tour to be exactly 300 units from start to finish (including the distance from City 50 to City 1).  With this tour, I ran tests to gauge what kind of optimization was realistically possible using the simulated annealing algorithm, and was surprised to find that in a handful of cases, I was able to come extremely close to the optimum.  In one case, I was able to reach full optimization.  This, of course, does not constitute a proof.  However, given that finding _the_ optimum for a randomized 50-city tour is practically infeasible, this bit of testing convinced me that the method is sufficient to find _an_ optimum. 

Initial Temperature was set to start at 24 units (half the total number of cities minus 1) and terminates at 1.  Terminating the Temperature at any value below one is liable to crash the program and throw an overflow error.

## Results
---
Here is the sequence of trial runs for the Traveling Saleman problem.  The increase in "cooling" precision corresponds to a tenfold increase in iterations.

|Trial|Cool Rate|Iterations|Init Tour|Final Tour|Opt Rate| 
|-----|---------|----------|---------|----------|--------|
|1|0.999|3177|2463.95|1271.31|93.81| 
|2|0.999|3177|2419.83|1073.75|125.36|
|3|0.9999|31779|2738.76|925.34|195.97|
|4|0.9999|31779|2798.87|900.37|210.86|
|5|0.99999|317804|2622.47|726.87|260.79| 
|6|0.99999|317804|2283.43|686.55|232.58|
|7|0.999999|3178053|2407.93|636.24|278.46|
|8|0.999999|3178053|2576.23|753.59|241.86|

Here is the initialized 50-city tour for Trial 7.  Throughout the tours, City 1 remains stationary.  The labels for the other cities change to correspond to the order in which they would be visited.
![TSP](https://github.com/CodeCommandante/ThePeoplesRepo/tree/main/Natural%20Computing/Traveling%20Salesman%20Problem/plots/TSP.png)

Here is the finished tour for Trial 7.
![TSP_end](https://github.com/CodeCommandante/ThePeoplesRepo/tree/main/Natural%20Computing/Traveling%20Salesman%20Problem/plots/TSP_end.png)

Shows the change in total tour distance over the course of Trial 7.
![Iterations vs Distance](https://github.com/CodeCommandante/ThePeoplesRepo/tree/main/Natural%20Computing/Traveling%20Salesman%20Problem/plots/ItsVSDist_rand.png)

## Credits
Additional credit to Dr. Jeff McGough from South Dakota School of Mines and Technology for providing his students with these fun and challenging problems.
