#This is a simple algorithm that will work using command line

points = [15,12,10,9,8,7,6,5,4,3,2,1]
#I'm assuming there is 12 players in the match.
#You are awarded points for how well you placed in a track.
#If you placed first, you gain 15 points, which translates here with points[1-1] = points[0]


#SETTING UP THE MOGI
#All of these options will probably going to end up in a form script type in the web app
print("Number of tracks ?")
print("(4, 8, 12, 24, 36 or 48)")
ntrack = input()
ntrack = int(ntrack)
print("\n")

print("Mogi type ?")
print("(You can choose between FFA, 2v2, 3v3, 4v4 and 6v6)")
mtype = input()
print("\n")

mtypelist = ["FFA", "2v2", "3v3", "4v4", "6v6"]
nteamslist = [12,6,4,3,2] #number of teams for a respective type
numteams = -1

for i in range(len(mtypelist)) : #set the number of teams in the mogi
    if mtype == mtypelist[i] :
        numteams = nteamslist[i]
        playerperteam = 12/numteams
        playerperteam = int(playerperteam)
        #will working on the "invalid format" error once i'll turn this into a web app

teamnames = []
teamplayers = []
teampoints = []
playerpoints = []


if mtype != "FFA" :
    for j in range(numteams) : #create the teams
        print(f"Name of team {j+1} :")
        name = input()
        teamnames.append(name)
        teamplayers.append([])
        teampoints.append([])
        playerpoints.append([])

        for k in range(playerperteam) : #attributes the players to the teams
            print(f"Name of player {k+1} :")
            p = input()
            teamplayers[j].append(p)
            playerpoints[j].append([])
        
        print("\n")

else :
    for j in range(numteams) : #create the teams
        teamplayers.append([])

        for k in range(playerperteam) : #attributes the players to the teams
            print(f"Name of player {j+1} :")
            p = input()
            teamplayers[j].append(p)
            playerpoints[j].append([])
        
        print("\n")

if len(teamnames) != numteams : #in case this is a FFA
    for l in range(numteams) :
        teamnames.append("")
        teampoints.append([])

for m in range(len(teamnames)) : #if the team name isn't given, takes the name of the 1st player of the team
    if teamnames[m] == "" :
        teamnames[m] = teamplayers[m][0]

#Quick test to see if everything is ok for now
print("Teams competing in the current mogi :\n")
for n in range(len(teamnames)) :
    print("Team " + teamnames[n] + " :")
    for o in range(playerperteam) :
        print(teamplayers[n][o], end=" ")
        print("\n")


print("The match will start as soon as you press Enter")
input()


#RUNNING THE MOGI
#for each track you must gave the points that each player got

for i in range(1) : #range(ntrack)
    if i == 0 :
        print(f"Enter the placement for the {i+1}st track")
    elif i == 1 :
        print(f"Enter the placement for the {i+1}nd track")
    elif i == 2 :
        print(f"Enter the placement for the {i+1}rd track")
    else :
        print(f"Enter the placement for the {i+1}th track")
    print("Please write the placement in the player order, in this format : '1 2 3 4 5 6 7 8 9 10 11 12' (with spaces used as divider)")
    print("Reminder of the player order :")
    print(teamplayers)
    placementinsaidtrack = input()


    placementlist = placementinsaidtrack.split()
    for oui in range(len(placementlist)) :
        placementlist[oui] = int(placementlist[oui])
    
    for j in range(12) :
        quotient = j//numteams #current team in the loop
        rest = j%numteams #current player in the loop
        teampoints[quotient] = teampoints[quotient] + points[placementlist[j]-1]
        playerpoints[quotient][rest] += points[placementlist[j]]
    
    print("Here is the current score :")
    for k in range(numteams) :
        print("Team " + teamnames[n] + " :" + teampoints[k])
