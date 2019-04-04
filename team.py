import game

class Team():
    def __init__(self, teamName):
        self.__name = teamName
        self.__reputation = {}
        self.__visitedLocalities = []
        self.__players = []

    def addPlayer (self, player):
        self.__players.append (player)
    
    def addLocality (self, locality):
        self.__visitedLocalities.append(locality)

    def editReputation (self, changes):
        pass