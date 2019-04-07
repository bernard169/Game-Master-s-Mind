import game
import team
import player

region = input("Please enter a region : \n")
people = input("Please enter people : \n")
exceptionnalEvent = input ("Was this event extraordinary ? [y/N] \n")
isExceptionnal= True
if (exceptionnalEvent != "y"):
    isExceptionnal = False

witnesses = int(input("Enter the number of witnesses : \n"), base=10)
witnessImportance = int(input("Enter a value representing the importance and reputation of witnesses on 100 : \n"), base=10)
placeEvent = int(input("Enter a value representing the importance and attendance of the place where the event happened on 100 : \n"), base=10)
proofEvent = int(input("Enter a value representing the amount of proofs left by the event on 100: \n"), base=10)

multiplier = 0
impactWit = 0
if (0 < witnesses < 10):
    impactWit = 1 
elif (10 < witnesses < 20):
    impactWit = 3
elif (20 < witnesses < 50):
    impactWit = 5
elif (50 < witnesses < 200):
    impactWit = 9
elif (witnesses > 200):
    impactWit = 11
elif (witnesses > 2000):
    impactWit = 12
impactWit *= (witnessImportance/20) #max *5 => max = 60
impactPlace = placeEvent/4 # max = 25
impactProof = proofEvent/6.667 #max = 15

if (isExceptionnal):
    multiplier = 2*(impactPlace + impactProof + impactWit)
else :
    multiplier = impactPlace + impactProof + impactWit


difficulty = int(input("Enter a value representing the difficulty on 10 : \n"), base=10)
theater = int(input("Enter a value representing the theatrality on 10 : \n"), base=10)
good = int(input("Enter a value representing the goodness of the act on 10: \n"), base=10)
bad = int(input("Enter a value representing the badness of the act on 10 : \n"), base=10)
goodBehavior = int(input("Enter a value representing the good behavior of the team on the act on 10 : \n"), base=10)
badBehavior = int(input("Enter a value representing the bad behavior of the team on the act on 10 : \n"), base=10)
violence = int(input("Enter a value representing the violence of the team on the act on 10 : \n"), base=10)  
casulties = int(input("Enter a value representing the number of casulties caused by the act on 10 (high value is few casulties): \n"), base=10)
adversary = int(input("Enter a value representing the meanness of the vilain on 10 : \n"), base=10)

respect = (difficulty*6 + theater*4 + adversary*3 + goodBehavior*2 - badBehavior*3)/1.5 #values are on 100
print ("value for respect is : ")
print (respect)
fear = (violence*6 + difficulty*2 + theater*3 + badBehavior*2 - goodBehavior*3)/1.3
print ("\n value for fear is :")
print (fear)
hatred = (bad*7 + badBehavior*2 + (10-casulties)*10 + (10-adversary)*2 - 8*good - 3*goodBehavior - 2*adversary - 10*casulties)/1.5 #when 10-value, if the value is greater than 5, it has positive impact, otherwise negative impact 
print ("\n value for hatred is : " )                                                                            #=> we consider the value over 5 not 10, so we have to multiply by 2 the value 
print (hatred)
admiration = (difficulty*5 + good*3 + goodBehavior*2 + theater*4 + adversary- bad*4 -badBehavior*3)/1.5
print ("\n value for admiration is : ")
print (admiration)
love = (good*5 + casulties*3 + goodBehavior*2.5 + adversary*3 + difficulty*1.5 - bad*6 - badBehavior*3.5)/1.5
print (" \n value for love is : ")
print (love)
contempt = (badBehavior*5 + (10-difficulty)*6 + bad*4 + theater*3 - 6*goodBehavior - 6*difficulty - 5*good )
print ("value for contempt is : ")
print (contempt)