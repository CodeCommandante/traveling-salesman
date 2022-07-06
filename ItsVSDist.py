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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 11:26:47 2021

@author: jimleon

Estimate vs iteration plot for simAnnealing
"""

import matplotlib.pyplot as plt

def plotItVsDist(pointArray):
    i = 0
    while i < (len(pointArray)-1):
        x = [pointArray[i][0],pointArray[i+1][0]]
        y = [pointArray[i][1],pointArray[i+1][1]]
        plt.plot(x,y,'black','-')
        i = i + 1
    plt.grid()
    plt.axis([0,pointArray[len(pointArray)-1][0],0.0,3500])
    plt.yticks([0,1000,1500,2000,2500,3000,3500],[0,1000,1500,2000,2500,3000,3500])
    plt.xlabel('Iterations')
    plt.ylabel('Overall Distance')
    plt.title('Distance vs Iterations')
    plt.show()
    return