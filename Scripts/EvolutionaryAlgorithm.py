import numpy as np;
import math;
import random as rand;



class EvolutionaryAlgorithm:
    parameterSets = None;  #list of parameter sets the algorithm seeks to evolve
    evolutionStep = None;  #number of iterations that have passed
    valueRange = None;     #tuple which stores the range of values that each
    goalStateReached = False;   #Whether or not the search has found a satisfactory result.  Stops the search when true;
    score = {};            #dictionary that stores the fitness scores of paramSets.  Key = paramset.tobytes() Value = score  |  Currently this dictionary can grow infinitely, limit it if you are having memory problems.
    
    
    #int, int tuple, 
    def __init__(self, numParamSets, paramSetShape, valueRange):
        self.evolutionStep = 0;
        self.valueRange = valueRange;
        paramSetShape = (numParamSets,)+paramSetShape;
        self.parameterSets = np.random.uniform(valueRange[0], valueRange[1], paramSetShape);
        
    
    #todo, look into using predicted variance to guess how many paramsets to kill and skip loops
    def run(self):
        selectionLimit = self.updateScores()[0];
        while self.goalStateReached == False:
            
            
            
            
            numChanged=0;
            for p in range(self.parameterSets.shape[0]):
                pbytes=self.parameterSets[p].tobytes();
                if self.score[pbytes]<selectionLimit:
                    self.parameterSets[p]=self.replaceParamSet(self.parameterSets[p], selectionLimit);
                    numChanged+=1;
            print();
            
            scoreData = self.updateScores();
            selectionLimit = scoreData[0];
            print(scoreData[1]);
            
            if(numChanged == 0):
                self.goalStateReached = True;
                print(scoreData[3])
    
    
    def updateScores(self):
        top = -9999999
        total = 0;
        for p in self.parameterSets:
            pbytes=p.tobytes();
            if pbytes not in self.score:
                self.score[pbytes] = self.testParameters(p);
            total+=self.score[pbytes];
            if(self.score[pbytes] > top):
                top = self.score[pbytes];
        mean = total/np.size(self.parameterSets,0);
        varTot = 0;
        for p in self.parameterSets:
            pbytes=p.tobytes();
            t = self.score[pbytes]-mean;
            sqdiff = t*t;
            varTot+=sqdiff;
        variance = varTot/np.size(self.parameterSets,0);
        standardDev = math.sqrt(variance);    
        selectionLimit = mean-standardDev;
        return (selectionLimit, variance, standardDev, top,);
    
    def mutateParameters(self, paramSet, paramMin, paramMax):
        #pass
        numMutations = 1;   #number of parameters that change in each mutation
        mutationVariation = .01;
        changedParams = ();
        for s in range(numMutations):
            index = ();
            for d in range(paramSet.ndim):
                max = paramSet.shape[d];
                num = np.random.randint(0,max);
                index = index+(num,);
            changedParams=changedParams+(index,);
        
        for i in changedParams:
            modifier = rand.random()*(mutationVariation*2)-mutationVariation;
            if paramSet[i]+modifier > paramMin and paramSet[i]+modifier < paramMax:
                paramSet[i]+=modifier;
        return paramSet;
    
    def testParameters(self, paramSet):
        #pass;
        return paramSet[0,0]+paramSet[1,0];
        
    def replaceParamSet(self, paramSet, selectionLimit):
        pbytes=paramSet.tobytes();
        s = self.score[pbytes];
        targetParamSet = None;
        targetbytes = None;
        while targetbytes is None or self.score[targetbytes] is None or self.score[targetbytes] < selectionLimit or targetbytes == pbytes:
            targetParamSet = self.parameterSets[rand.randrange(np.size(self.parameterSets,0))];
            targetbytes = targetParamSet.tobytes();
            if(targetbytes not in self.score):
                self.updateScores();
        #print(paramSet)
        paramSet = self.mutateParameters(np.copy(targetParamSet), self.valueRange[0], self.valueRange[1]);
        #print(paramSet)
        return paramSet;
    
    
        
        
a = EvolutionaryAlgorithm(10000, (2,3), (0,1));
a.run();
