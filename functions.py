def errorProg(content):
    print("{}".format(content))

def defineAmount():
    amountParticipantsStr = input("Write the amount of participants: ")
    return amountParticipantsStr

def desicion(q):
    answerDesicion = input(q)
    return answerDesicion

def com(amount):
    print("The following fixture will be generated in an Excel File")
    matches = "There are {} games per matchday".format(amount)
    print(matches)

def optionsPositions():

    optionPosition = 0

    while optionPosition < 1 or optionPosition > 3:
        print("\n1: Generate")
        print("2: Add a column")
        print("3: Cancel")
        optionPositionStr = input("Select an option: ")

        try:
            optionPosition = int(optionPositionStr)
        except:
            errorProg("Try to select an option")
            optionPosition = optionsPositions()

    return optionPosition

def newColumn():
    name = input("Column name: ")
    return name

    
