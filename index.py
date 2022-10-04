import numpy as np
import pandas as pd
import random as rd

import functions as func

columns = np.array(["Local", "", "", "Visitant"])

participantsList = []
fixture = []

def continuing():

    amountParticipantsStr = func.defineAmount()
    amountParticipants = 0

    try:
        amountParticipants = int(amountParticipantsStr)
    except:
        func.errorProg("Try to write an integer value")
        amountParticipants = continuing()

    return amountParticipants

def showPositions(df):
     print("\nPositions table:")
     print(df)
    
def actionPosition(optionPosition):
    if optionPosition == 1:
        writerPositions = pd.ExcelWriter("positions.xlsx")
        pd.DataFrame(dfPositions).to_excel(writerPositions)
        writerPositions.save()
    elif optionPosition == 2:
        columnName = func.newColumn()
        dfPositions[columnName] = 0
        showPositions(dfPositions)
        optionPosition = func.optionsPositions()
        actionPosition(optionPosition)

amountParticipants = continuing()

for i in range(0, amountParticipants):
    participant = input("Write a participant name: ")
    participantsList.append(participant)

if amountParticipants % 2 != 0:
    participantsList.insert(0, "Free")

participants = np.array(participantsList)
rd.shuffle(participants)
participantsCopy = participants.copy()

proxMain = int((len(participants) / 2) + 1)

for i in range(1, len(participants)):

    titlefixture = "Matchday {}".format(i)
    print(titlefixture)

    pivot = participants[0]
    first = participants[1]

    for j in range(0, int(len(participants) / 2)):

        combination = []

        if j == 0:
            if(i % 2 != 0):
                combination.append(participants[0])
            else:
                combination.append(participants[1])
        else:
            combination.append(participants[0])
        for k in range(0, 2):
            combination.append(" ")
        if j == 0:
            if(i % 2 != 0):
                combination.append(participants[1])
            else:
                combination.append(participants[0])
        else:
            combination.append(participants[1])

        fixture.append(combination)

        match = "{} vs {}".format(participants[0], participants[1])
        print(match)

        participants[1] = participants[len(participants) - (j+1)]
        if len(participants) > 2:
            participants[0] = participants[2+j]
        else:
            participants[0] = participants[1+j]

    participants = participantsCopy.copy()
    participants[0] = pivot

    print("")

    beforeProxMain = proxMain

    for j in range(0, int(len(participants) / 2)):
        if proxMain == len(participants):
            break
        participants[j+1] = participants[proxMain]
        participants[proxMain] = participants[j+2]
        proxMain+=1

    proxMain = beforeProxMain
    participants[proxMain - 1] = first
    participantsCopy = participants.copy()

func.com(int(len(participants)/2))
answer = func.desicion("\nDo you want continue? (y/n): ")

while answer != "Y" and answer != "y" and answer != "N" and answer != "n":
    answer = func.desicion()

if answer == "Y" or answer == "y":
    values = np.array(fixture)

    fixPd = pd.DataFrame(values, columns=columns)
    fixPd.index = np.arange(1, len(fixPd) + 1)

    writer = pd.ExcelWriter("fixt.xlsx")
    pd.DataFrame(fixPd).to_excel(writer)
    writer.save()

    # Positions table

    print("Fixture generated successfully")
    answerPositions = input("\nGenerate a positions table? (y/n): ")

    while answerPositions != "Y" and answerPositions != "y" and answerPositions != "N" and answerPositions != "n":
        answerPositions = func.desicion()

    if answerPositions == "Y" or answerPositions == "y":
        columnsPositions = np.array(["Participant", "Points"])

        valuesPositionsArr = []

        for i in range(0, len(participants)):
            dataParticipant = [participants[i], 0]
            valuesPositionsArr.append(dataParticipant)

        valuesPositions = np.array(valuesPositionsArr)
        dfPositions = pd.DataFrame(valuesPositions, columns=columnsPositions)
        dfPositions.index = np.arange(1, len(dfPositions) + 1)

        showPositions(dfPositions)
        optionPosition = func.optionsPositions()
        actionPosition(optionPosition)

        


    





