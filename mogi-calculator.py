#This is a simple algorithm that will work using command line

points = [15,12,10,9,8,7,6,5,4,3,2,1]
#I'm assuming there is 12 players in the match.
#You are awarded points for how well you placed in a track.
#If you placed first, you gain 15 points, which translates here with points[1-1] = points[0]

print("Placement ?")
placement = input()
placement = int(placement)
print("Points you got : " + str(points[placement - 1]))
#This is a quick test because i'm planning to eat soon so i just want to see if the git depositary works