# -*- coding: utf-8 -*-
"""8_19301051_KaziMdAlWakil_CSE422_Lab 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TOcZ7zivxhdcD4r-bv_5IuedPg5GhQDT
"""

from google.colab import drive
drive.mount('/content/drive')

import random as ran
import numpy as namPie

# lab 2 Task 1
# Run Chase Problem
# Kazi Md. Al-Wakil
# 19301051

#creating enfant
def zebraCrossing (paren1, paren2):
  lenguParent = len(paren1)
  gimmeIdx = ran.randrange(0,lenguParent) #randomly ekta idx generate korlam
  enfant= []

  prothomPart = paren1[0:gimmeIdx]
  secondPart = paren2[gimmeIdx:]

  for itor in prothomPart: 
    enfant.append(itor) #prothom part nilam first paren theke 

  for itor in secondPart: 
    enfant.append(itor) #baki part nilam Second paren theke 

  

  return enfant #enfant return kortesi

# mutating the enfant 
def evolve(enfant):
  lenguEnfant = len(enfant)
  whichIdxToEvolve = ran.randrange(0,lenguEnfant)
  

  for i in range(len(enfant)):
    if i == whichIdxToEvolve:
      if enfant[i] == 1:
        enfant[i] = 0
      elif enfant[i] == 0:
        enfant[i] = 1

  return enfant

#choosing baba ma
def paireSelecteur(iqx_chromosome, SumOfIndividualList, iqx_targetRuns):
  min1 = 10000
  for i in range(len(SumOfIndividualList)): #[233, 261, 259, 284, 180, 338, 221, 71, 100, 166]
    a = abs(iqx_targetRuns-SumOfIndividualList[i]) # a = 330-233 = 97
    if a < min1: 
      min1 = a
      index1 = i 
  val1 = SumOfIndividualList[index1]
  SumOfIndividualList[index1] = 10000
  min2 =10000
  for i in range(len(SumOfIndividualList)): #[233, 261, 259, 284, 180, 338, 221, 71, 100, 166]
    a = abs(iqx_targetRuns-SumOfIndividualList[i]) # a = 330-233 = 97
    if a < min2: 
      min2 = a
      index2 = i
  return iqx_chromosome[index1], iqx_chromosome[index2]

# shera feet function
def prochurFitnessCalculator(iqx_playerRun, iqx_chromosome): 
  whoIsFitEnough = [] # iqx_chromosome er sob sample er run ekhane store hobe. nested list
  SumOfIndividualList = [] # whoIsFitEnough List er moddhe sob sample er sum ber kore ei list e append korbo
  for itor in iqx_chromosome: #fetching sample from iqx_chromosome
    tempuLisu = []
    for jtor, uporerI in zip(iqx_playerRun, itor): #gun kortesi run list er sathe
      tempuLisu.append(jtor*uporerI) #[68, 25, 70, 53, 71, 55, 66, 29] * [0, 0, 0, 0, 1, 0, 1, 0]
    whoIsFitEnough.append(tempuLisu) # appending this [0, 0, 0, 0, 71, 0, 66, 0]
  for itor in whoIsFitEnough:
    SumOfIndividualList.append(sum(itor)) # Sum of [0, 0, 0, 0, 71, 0, 66, 0] = 137 # appending 137 to the SumOfList1 list



  return SumOfIndividualList

def biyogHowaListFunc(iqx_chromosome, SumOfIndividualList, iqx_targetRuns):
  tempuLisu = []
  for itor in SumOfIndividualList:
    tempuLisu.append(abs(iqx_targetRuns - itor))
  return tempuLisu

#choto value and choto value er index dibe
def chotoValueDibeFunc(biyogHowaList):
  ekdomChotoZero = 9999
  for itor in range(len(biyogHowaList)):
    if biyogHowaList[itor] < ekdomChotoZero:
      ekdomChotoZero = biyogHowaList[itor] #biyog howa list er sobchey choto value stored
      ekdomChotoZeroIdx = itor #biyog howa list er sobchey choto value er index stored
  return ekdomChotoZero, ekdomChotoZeroIdx

def minusL(fit, runToChase):
  min1 = 10000
  for i in range(len(fit)): #[233, 261, 259, 284, 180, 338, 221, 71, 100, 166]
    a = abs(runToChase-fit[i]) # a = 330-233 = 97
    if a < min1: 
      min1 = a
      index1 = i 
  return index1

#ashol algorithm
def genAlgo(iqx_totalInputs, iqx_playerRun, iqx_chromosome, iqx_targetRuns, mutMargin, iqx_playerList):
  genMargin, genNumber = 22, 0
  boolBooliya = True

  while boolBooliya == True:
    ekdomChotoZero = 9999 #ekhane min value store korbo SumOfIndividualList er. min value 0 hoile goal peye gesi
    SumOfIndividualList = prochurFitnessCalculator(iqx_playerRun, iqx_chromosome) # fit = [258, 66, 328, 167, 270, 330, 383, 209, 355, 163]
    # fit e ekhon sumList chole asche. ekhan theke bujhte parbo, k beshi fit

    biyogHowaList = biyogHowaListFunc(iqx_chromosome, SumOfIndividualList, iqx_targetRuns) #checking if amar kache emon kono sample ache kina jeta goal er kache or goal itself
    ekdomChotoZero, ekdomChotoZeroIdx = chotoValueDibeFunc(biyogHowaList)

    if genNumber > genMargin: #genMargin maximum generation. er beshi amra r check korbo na, then break
      print(-1)
      break
    elif ekdomChotoZero == 0: #0 mane amra goal state peye gesi.  true hole print kore break
      print(iqx_playerList)
      for itor in iqx_chromosome[ekdomChotoZeroIdx]:
        print(itor,end="")
      break
    else:
      newGen = [] 
      for itor in range(len(iqx_chromosome)):
        paren1, paren2 = paireSelecteur(iqx_chromosome, SumOfIndividualList, iqx_targetRuns) #2 jon parent select kora hocche. jara best fit among all
        enfant = zebraCrossing (paren1, paren2) #enfant of the parens
        
        evolveKihobe = ran.random() #generating random number
        
        if evolveKihobe < mutMargin: #jodi random number mutation threshold theke kom hoy taile mutate hobe
          enfant = evolve(enfant)

        newGen.append(enfant) #ekta notun gen create hocche 
      
      #iqx_chromosome e new gen add kori
      for itor in newGen:
        if itor not in iqx_chromosome:
          iqx_chromosome.append(itor)
      
      genNumber = genNumber + 1
      print("GenNumber: ",genNumber)

# Storing and initializing all the values
def sovaLineup(inputLine):
  tempuLisu = [] #temporary list
  iqx_playerList = [] #player der nam store korbo
  iqx_playerRun = [] #player er run list
  iqx_totalInputs = 0 #total koyta input seta store korbo
  iqx_targetRuns = 0 #Target run ta store korbo

  for itor in range(len(inputLine)):
    if (itor == 0):
      firstLineOfTheInput = inputLine[0]
    else:
      stri = inputLine[itor]
      tempuLisu.append(stri)

  firstLineOfTheInputList= firstLineOfTheInput.split()
  iqx_totalInputs, iqx_targetRuns = int(firstLineOfTheInputList[0]), int(firstLineOfTheInputList[1])

  for itor in tempuLisu:
    tempuLisu2 = itor.split()
    iqx_playerList.append(tempuLisu2[0])
    iqx_playerRun.append(int(tempuLisu2[1]))
  return iqx_totalInputs, iqx_targetRuns, iqx_playerList, iqx_playerRun

# lab 2 Task 1

reading = open("/content/drive/MyDrive/CSE422 Labs/Lab2_T1_Input1.txt","r")
inputLine = reading.readlines() 

iqx_totalInputs, iqx_targetRuns, iqx_playerList, iqx_playerRun = sovaLineup(inputLine) # Storing and initializing all the values

initialPopu = 10 # Population size 10 ta nilam 
iqx_chromosome = [] # choromosome list e 10 ta randomly generated sample ache, 
                #sei sample e kon kon batsman pick korsi tader data ache. 
                # 1 hole batsman pick korsi, 0 hole pick kori nai
zeroList = [] #contains only zeros and nothing else


for itor1 in range(iqx_totalInputs): #zero er list banailam, jate kore only 0 list population matrix e append na hoy
  zeroList.append(0)

iqx_itor = 0
while iqx_itor < initialPopu: # total 10 ta population list banabo 
  tempchromo = []
  for jtor in range(iqx_totalInputs): 
    tempchromo.append(ran.randrange(0,2))
  if(tempchromo not in iqx_chromosome and tempchromo != zeroList):
    iqx_chromosome.append(tempchromo)
    iqx_itor +=1


mutMargin = ((((1+2)*10)+126)+(2*100)-(2*28))/1000 #mutation threshold, er upore gele mutation hobe, otherwise hobe na


genAlgo(iqx_totalInputs, iqx_playerRun, iqx_chromosome, iqx_targetRuns, mutMargin, iqx_playerList)