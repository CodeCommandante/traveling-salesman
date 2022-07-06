"""    
    Program to solve the Traveling Salesman Problem.
    Copyright (C) 2021  Jim Leon

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

#! /usr/bin/python3

"""
Created on Sat Jan 23 13:23:00 2021

@author: jimleon

TSP algorithm
"""

import matplotlib.pyplot as plt
import random
import math
import time
import argparse
import ItsVSDist

def calculatePairDist(FirstPair, SecondPair):
    xSqrd = math.pow(SecondPair[0]-FirstPair[0],2)
    ySqrd = math.pow(SecondPair[1]-FirstPair[1],2)
    return math.sqrt(xSqrd + ySqrd)
    
def calculateTotalDist(CityMap):
    TotalDist = 0.0
    i = 0
    while i < (len(CityMap) - 1):
        TotalDist = TotalDist + calculatePairDist(CityMap[i], CityMap[i+1])
        i = i + 1
    TotalDist = TotalDist + calculatePairDist(CityMap[0], CityMap[len(CityMap)-1])
    return TotalDist

def createCityMap(NumOfCities):
    CityMap = {}
    for i in range(NumOfCities):
        CityMap[i] = (random.randint(1,99),random.randint(1,99))
    return CityMap

def createTestCity():
    CityMap = {}
    for i in range(50):
        #upper side of square
        if i < 13:
            CityMap[i] = (i*6+10,86)
        #lower side of square
        if i >= 13 and i < 26:
            CityMap[i] = ((i-13)*6+10,8)
        #left side of square
        if i >= 26 and i < 38:
            CityMap[i] = (10,(i-26)*6+14)
        #right side of square
        if i >= 38 and i < 50:
            CityMap[i] = (82,(i-38)*6+14)
    CityMap = mixUpCities(CityMap,49)
    return CityMap

def findOptimizedPath(plt, CityMap):
    DistTraveled = calculateTotalDist(CityMap)
    FirstDist = DistTraveled
    print("Begin ",len(CityMap)," city tour...")
    print("Initialized path:  ",round(DistTraveled, 2)," units")
    plt.pause(0.01)
    Temperature = int(len(CityMap)/2) - 1
    Attempts = 0
    Actuals = 0
    PointArray = {}
    StartTime = time.perf_counter()
    while Temperature > 1:
        TempMap = mixUpCities(CityMap, Temperature)
        NewDist = calculateTotalDist(TempMap)
        if (NewDist < DistTraveled) or (random.uniform(0,1) < math.exp((DistTraveled-NewDist)/Temperature)):
            CityMap = TempMap
            DistTraveled = NewDist
            plt.clf()
            plotCityAndConnect(CityMap)
            plt.pause(0.0001)
            PointArray[Actuals] = (Attempts,DistTraveled)
            Actuals = Actuals + 1
        Temperature = Temperature*0.999999
        Attempts = Attempts + 1
    StopTime = time.perf_counter()
    TotalTime = StopTime - StartTime
    printStats(DistTraveled, FirstDist, TotalTime, Attempts, Actuals)
    return PointArray

def initialState(CityMap):
    plotCityAndConnect(CityMap)
    plt.show()
    return

def plotLineBetweenPoints(plt, firstPair, secondPair):
    x = [firstPair[0], secondPair[0]]
    y = [firstPair[1], secondPair[1]]
    plt.plot(x, y, 'black', '-')
    return plt

def plotCityAndConnect(CityMap):
    i = 1
    plt.plot(CityMap[0][0], CityMap[0][1], 'go')
    plt.axis([0,100,0,100])
    plt.annotate(i,CityMap[0])
    while i < len(CityMap):
        plt.plot(CityMap[i][0], CityMap[i][1], 'ro')
        plt.annotate(i+1,CityMap[i])
        i = i + 1
    j = 0
    while j < (len(CityMap) - 1):
        plotLineBetweenPoints(plt, CityMap[j], CityMap[j+1])
        j = j + 1
    plotLineBetweenPoints(plt, CityMap[0], CityMap[len(CityMap)-1])
    plt.yticks([0,20,40,60,80,100],[0,20,40,60,80,100])
    plt.title('Traveling Salesman Optimization')
    return

def printStats(DistTraveled, FirstDist, TotalTime, Attempts, Actuals):
    print("Optimized path:  ", round(DistTraveled,2), " units")
    print("Optimization time:  ", round(TotalTime, 2), " seconds" )
    print("Attempts at optimization:  ", Attempts )
    print("Actual optimizations:  ", Actuals )
    print("Ratio (actuals/attempts):  ", round((Actuals/Attempts)*100,3), "%")
    print("Reduction in path length:  ", round((FirstDist/DistTraveled)*100, 1), "%") 
    return

def mixUpCities(CityMap, Intensity):
    TempMap = CityMap.copy()
    i = 0
    if Intensity < 1:
        Intensity = 1
    elif Intensity >= len(TempMap):
        Intensity = len(TempMap)
    while i < Intensity:
        first = random.randint(1, len(TempMap) - 1)
        second = random.randint(1, len(TempMap) - 1)   
        temp = TempMap[first]
        TempMap[first] = TempMap[second]
        TempMap[second] = temp
        i = i + 1
    return TempMap

def TSPmain():
    parser = argparse.ArgumentParser()
    parser.add_argument("numCities")
    args = parser.parse_args()
    CityMap = createCityMap(int(args.numCities))
    #CityMap = createTestCity()
    plotCityAndConnect(CityMap) 
    plt.show()
    PointArray = findOptimizedPath(plt, CityMap)
    plt.show()
    ItsVSDist.plotItVsDist(PointArray)
    return 0

TSPmain()
