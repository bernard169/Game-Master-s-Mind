import team
import player

class Game():
    def __init__(self, imgAdress, localities):
        self.__mapImg = imgAdress
        self.__localities = localities
        self.__teams = []
    
    def addTeam (self, team):
        self.__teams.append(team)

    def getMap (self):
        mapInfos = {"mapImg" : self.__mapImg}
        counter = 1
        for loc in self.__localities:
            mapInfos[loc + str(counter)] = loc
        return mapInfos
    
