def solution(x):
    fp = open(x)
    filedata = fp.readlines()
    ingridientsDict = {}
    noOfIngredientsDict = {}
    pizzasDeliveredToFourmembersTeam = []
    pizzasDeliveredToThreemembersTeam = []
    pizzasDeliveredToTwomembersTeam = []


    # Taking input from the file
    no_of_pizzas, no_of_two_members_team, no_of_three_members_team, no_of_four_members_team = filedata[0].rstrip().split(" ")

    no_of_pizzas = int(no_of_pizzas)
    no_of_two_members_team = int(no_of_two_members_team)
    no_of_three_members_team = int(no_of_three_members_team)
    no_of_four_members_team = int(no_of_four_members_team)


    total_members = (2*no_of_two_members_team) + (3*no_of_three_members_team) + (4*no_of_four_members_team)
    print(total_members)
    for i in range(1,no_of_pizzas + 1):
        noOfIngredientsDict[i] = filedata[i].rstrip()[0]
        ingridientsDict[i] = list(map(str, filedata[i].rstrip()[2:].split(" ")))

    #Calculating the solution for the problem



    deliverCounter = 0

    if 4 * no_of_four_members_team < no_of_pizzas:
        for i in range(1, no_of_four_members_team + 1):
            tempList = []
            for j in range(1,5):
                tempList.append(deliverCounter)
                deliverCounter = deliverCounter + 1
            pizzasDeliveredToFourmembersTeam.append(tempList)
        no_of_pizzas = no_of_pizzas - 4 * no_of_four_members_team
    if 3 * no_of_three_members_team < no_of_pizzas:
        for i in range(1, no_of_three_members_team + 1):
            tempList = []
            for j in range(1,4):
                tempList.append(deliverCounter)
                deliverCounter = deliverCounter + 1
            pizzasDeliveredToThreemembersTeam.append(tempList)
        no_of_pizzas = no_of_pizzas - 3 * no_of_four_members_team
    if 2 * no_of_two_members_team < no_of_pizzas:
        print("locho")
        for i in range(1, no_of_two_members_team + 1):
            tempList = []
            for j in range(1,3):
                tempList.append(deliverCounter)
                deliverCounter = deliverCounter + 1
            pizzasDeliveredToTwomembersTeam.append(tempList)
        no_of_pizzas = no_of_pizzas - 2 * no_of_four_members_team
    else:
        print(no_of_pizzas)
        print(no_of_two_members_team)
        no_of_two_members_team = no_of_two_members_team - (no_of_two_members_team - (no_of_pizzas//2))
        print(no_of_two_members_team)
        for i in range(1, no_of_two_members_team + 1):
            tempList = []
            for j in range(1, 3):
                tempList.append(deliverCounter)
                deliverCounter = deliverCounter + 1
            pizzasDeliveredToTwomembersTeam.append(tempList)

    noOfTeamsGettingPizza = len(pizzasDeliveredToTwomembersTeam) + len(pizzasDeliveredToThreemembersTeam) + len(pizzasDeliveredToFourmembersTeam)

    outputfile = open("output_"+x,"w+")
    outputfile.write(str(noOfTeamsGettingPizza) + "\n")
    for i in range(len(pizzasDeliveredToFourmembersTeam)):
        tempstring = ''
        for j in pizzasDeliveredToFourmembersTeam[i]:
            tempstring = tempstring + str(j) + " "
        outputfile.write("4 " + tempstring.rstrip() + "\n")

    for i in range(len(pizzasDeliveredToThreemembersTeam)):
        tempstring = ''
        for j in pizzasDeliveredToThreemembersTeam[i]:
            tempstring = tempstring + str(j) + " "
        outputfile.write("3 " + tempstring.rstrip()+ "\n")

    for i in range(len(pizzasDeliveredToTwomembersTeam)):
        tempstring = ''
        for j in pizzasDeliveredToTwomembersTeam[i]:
            tempstring = tempstring + str(j) + " "
        outputfile.write("2 " + tempstring.rstrip() + "\n")



    print(pizzasDeliveredToFourmembersTeam)
    print(pizzasDeliveredToThreemembersTeam)
    print(pizzasDeliveredToTwomembersTeam)



solution('a_example')
solution('b_little_bit_of_everything (1).in')
solution('c_many_ingredients.in')
solution('d_many_pizzas.in')
solution('e_many_teams.in')


